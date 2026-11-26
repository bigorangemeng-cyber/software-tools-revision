#!/usr/bin/env python3
"""Build the static revision site.  Usage:  python3 src/build.py
Writes HTML pages into the folder above src/ (the site root)."""
import html
import re
import sys
import textwrap
from collections import defaultdict
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent
sys.path.insert(0, str(SRC))

import model as M                     # noqa: E402
import c_weeks                        # noqa: E402,F401  (declares weeks)
import c_unix                         # noqa: E402,F401  W0-W3
import c_git                          # noqa: E402,F401  W4-W5
import c_dev                          # noqa: E402,F401  W6-W7
import c_db                           # noqa: E402,F401  W8-W10
from c_weeks import MODULES, THREADS  # noqa: E402
from c_logic import QUESTION, SECTION  # noqa: E402
import json  # noqa: E402

UPSTREAM = "https://github.com/cs-uob/software-tools/tree/main/"
REFS = defaultdict(set)   # target id -> set(source ids)
ERRORS = []
_src = {"id": None}


def esc(s):
    return html.escape(s, quote=True)


def bi(en, zh, cls=""):
    c = f" {cls}" if cls else ""
    return (f'<span class="l-en{c}" lang="en">{en}</span>'
            f'<span class="l-zh{c}" lang="zh-CN">{zh}</span>')


def href(cid):
    d = M.BY_ID[cid]
    return f"{M.WEEKS[d['week']]['slug']}.html#c-{cid}"


# ---------------------------------------------------------------- markup
def inline(s, lang):
    s = html.escape(s, quote=False)
    codes = []

    def keep(m):
        codes.append(m.group(1))
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"`([^`]+)`", keep, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)

    def link(m):
        cid, label = m.group(1), m.group(2)
        if cid not in M.BY_ID:
            ERRORS.append(f"[{_src['id']}] broken link [[{cid}]]")
            return label or cid
        d = M.BY_ID[cid]
        if _src["id"] and _src["id"] != cid:
            REFS[cid].add(_src["id"])
        if not label:
            label = d["t_en"] if lang == "en" else d["t_zh"]
        tip = esc(f"{d['t_en']} · {d['t_zh']} (W{d['week']})")
        return f'<a class="xref" href="{href(cid)}" title="{tip}" data-code="{CODE.get(cid, "")}">{label}</a>'

    s = re.sub(r"\[\[([\w-]+)(?:\|([^\]]+))?\]\]", link, s)
    s = re.sub(r"\x00(\d+)\x00", lambda m: f"<code>{codes[int(m.group(1))]}</code>", s)
    return s


def md(text, lang):
    if not text:
        return ""
    lines = textwrap.dedent(text).strip("\n").split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i].rstrip()
        st = ln.strip()
        if not st:
            i += 1
            continue
        if st.startswith("```"):
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append(f'<pre class="code">{esc(textwrap.dedent(chr(10).join(buf)))}</pre>')
            continue
        if st.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(inline(lines[i].strip()[2:], lang))
                i += 1
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>")
            continue
        if st.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                r = lines[i].strip()
                i += 1
                if re.fullmatch(r"\|[\s:|-]+\|", r):
                    continue
                cells = re.split(r"(?<!\\)\|", r.strip()[1:-1])
                rows.append([x.strip().replace("\\|", "|") for x in cells])
            h = "".join(f"<th>{inline(x, lang)}</th>" for x in rows[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(x, lang)}</td>" for x in r) + "</tr>"
                        for r in rows[1:])
            out.append(f'<div class="tbl"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>')
            continue
        if st.startswith("! "):
            out.append(f'<p class="note">{inline(st[2:], lang)}</p>')
            i += 1
            continue
        if st.startswith("## "):
            out.append(f"<h4>{inline(st[3:], lang)}</h4>")
            i += 1
            continue
        buf = []
        while i < len(lines):
            s2 = lines[i].strip()
            if not s2 or s2[:2] in ("- ", "! ", "##") or s2.startswith("|") or s2.startswith("```"):
                break
            buf.append(s2)
            i += 1
        sep = " " if lang == "en" else ""
        out.append(f"<p>{inline(sep.join(buf), lang)}</p>")
    return "\n".join(out)


# ---------------------------------------------------------------- page shell
HEAD_JS = ("(function(){var m='both';try{var p=new URLSearchParams(location.search).get('lang');"
           "m=p||localStorage.getItem('st-lang')||'both'}catch(e){}"
           "if(!/^(en|zh|both)$/.test(m))m='both';document.documentElement.className='mode-'+m})()")


def sidebar(active=None):
    parts = []
    for mod in MODULES:
        weeks = [w for w in sorted(M.WEEKS) if M.WEEKS[w]["module"] == mod["id"]]
        li = []
        for n in weeks:
            w = M.WEEKS[n]
            cur = ' aria-current="page"' if active == n else ""
            li.append(f'<li><a href="{w["slug"]}.html"{cur}><span class="wn">W{n}</span>'
                      f'{bi(w["en"], w["zh"])}</a></li>')
        parts.append(f'<div class="navmod m-{mod["id"]}"><div class="navmod-t">'
                     f'{bi(mod["en"], mod["zh"])}</div><ul>{"".join(li)}</ul></div>')
    return f'<nav class="sidebar" aria-label="weeks">{"".join(parts)}</nav>'


def page(title, body, active=None, wide=False, side=True):
    top = f'''<header class="topbar">
  <a class="brand" href="index.html"><span class="logo">$_</span>{bi("Software Tools · Revision", "Software Tools 复习笔记")}</a>
  <nav class="topnav">
    <a href="index.html">{bi("Home", "首页", "ui")}</a>
    <a href="mindmap.html">{bi("Mind map", "思维导图", "ui")}</a>
    <a href="glossary.html">{bi("Glossary", "术语表", "ui")}</a>
    <a href="commands.html">{bi("Commands", "命令速查", "ui")}</a>
    <a href="all.html">{bi("All-in-one", "全文", "ui")}</a>
    <a class="nav-print" href="print.html">{bi("Exam print", "开卷打印包", "ui")}</a>
  </nav>
  <div class="langs" role="group" aria-label="language">
    <button data-mode="zh" type="button">中文</button><button data-mode="both" type="button">对照</button><button data-mode="en" type="button">EN</button>
  </div>
</header>'''
    layout = (f'<div class="layout">{sidebar(active)}<main class="main{" wide" if wide else ""}">{body}</main></div>'
              if side else f'<main class="main solo">{body}</main>')
    foot = ('<footer class="foot">' + bi(
        "Personal revision notes for COMS10012 / COMSM0085 Software Tools (University of Bristol), weeks 0–10. "
        "Built from the public course repository; not official course material.",
        "个人复习笔记：布里斯托大学 COMS10012 / COMSM0085 Software Tools 第 0–10 讲。根据公开课程仓库整理，非官方资料。")
        + '</footer>')
    return f'''<!DOCTYPE html>
<html lang="zh-CN" class="mode-both">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<script>{HEAD_JS}</script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{top}
{layout}
{foot}
<script src="assets/app.js"></script>
<script src="assets/mindmap.js"></script>
</body>
</html>
'''


# ---------------------------------------------------------------- pieces
def chip(cid, here_week=None):
    d = M.BY_ID[cid]
    wk = f'<span class="cw">W{d["week"]}</span>' if d["week"] != here_week else ""
    return (f'<a class="chip m-{M.WEEKS[d["week"]]["module"]}" href="{href(cid)}" '
            f'title="{esc(d["t_en"] + " · " + d["t_zh"])}">{wk}<b>{esc(d["t_en"])}</b>'
            f'<small class="l-zh">{esc(d["t_zh"])}</small></a>')


def render_concept(d):
    _src["id"] = d["id"]
    en, zh = md(d["en"], "en"), md(d["zh"], "zh")
    _src["id"] = None
    code = f'<pre class="code">{esc(textwrap.dedent(d["code"]).strip(chr(10)))}</pre>' if d["code"] else ""
    for s in d["see"]:
        if s not in M.BY_ID:
            ERRORS.append(f"[{d['id']}] broken see-also {s}")
        else:
            REFS[s].add(d["id"])
    return d, en, zh, code


def concept_html(d, en, zh, code, here_week):
    see = [s for s in d["see"] if s in M.BY_ID]
    back = sorted((r for r in REFS[d["id"]] if r not in see and r != d["id"]),
                  key=lambda x: (M.BY_ID[x]["week"], x))
    rel = ""
    if see:
        rel += f'<div class="rel-row"><span class="rel-k">{bi("See also", "相关")}</span>{"".join(chip(s, here_week) for s in see)}</div>'
    if back:
        rel += f'<div class="rel-row"><span class="rel-k">{bi("Referenced by", "被引用")}</span>{"".join(chip(s, here_week) for s in back)}</div>'
    rel = f'<footer class="rel">{rel}</footer>' if rel else ""
    ex = f'<span class="badge exam">{bi("exam focus", "重点")}</span>' if d["exam"] else ""
    return f'''<article class="concept" id="c-{d["id"]}">
<h3><a class="anchor" href="#c-{d["id"]}" aria-label="link">#</a><span class="term-en">{esc(d["t_en"])}</span><span class="term-zh l-zh">{esc(d["t_zh"])}</span>{ex}</h3>
<div class="bi-body"><div class="l-en" lang="en">{en}</div><div class="l-zh" lang="zh-CN">{zh}</div></div>
{code}
{rel}
</article>'''


# ---------------------------------------------------------------- mind map data
def node(en, zh, k, m=None, h=None, c=None):
    d = {"en": en, "zh": zh, "k": k}
    if m:
        d["m"] = m
    if h:
        d["h"] = h
    if c:
        d["c"] = c
    return d


def week_tree(n, as_root=False):
    w = M.WEEKS[n]
    secs = []
    for i, s in enumerate(w["sections"], 1):
        kids = [node(d["t_en"], d["t_zh"], "concept", w["module"], href(d["id"])) for d in s["concepts"]]
        secs.append(node(f'{n}.{i} {s["en"]}', f'{n}.{i} {s["zh"]}', "section", w["module"],
                         f'{w["slug"]}.html#s-{n}-{s["id"]}', kids))
    return node(f'W{n} {w["en"]}', f'W{n} {w["zh"]}', "root" if as_root else "week", w["module"],
                f'{w["slug"]}.html', secs)


def course_tree():
    mods = []
    for mod in MODULES:
        weeks = [week_tree(k) for k in sorted(M.WEEKS) if M.WEEKS[k]["module"] == mod["id"]]
        mods.append(node(mod["en"], mod["zh"], "module", mod["id"], None, weeks))
    return node("Software Tools (TB1)", "Software Tools 第 0–10 讲", "root", None, None, mods)


def mindmap(mid, tree, open_depth, tools=False, cls=""):
    data = json.dumps(tree, ensure_ascii=False).replace("</", "<\\/")
    t = " data-tools" if tools else ""
    return (f'<div class="mm {cls}" data-src="{mid}" data-open="{open_depth}"{t}></div>'
            f'<script type="application/json" id="{mid}">{data}</script>')


def week_main(n, rendered, level="h1"):
    w = M.WEEKS[n]
    mod = next(m for m in MODULES if m["id"] == w["module"])

    def wlink(k):
        x = M.WEEKS[k]
        return f'<a class="wk-link m-{x["module"]}" href="{x["slug"]}.html"><b>W{k}</b> {bi(x["en"], x["zh"])}</a>'
    builds = "".join(wlink(k) for k in w["builds"])
    leads = "".join(wlink(k) for k in w["leads"])
    flow = '<div class="flow">'
    if builds:
        flow += f'<div><span class="rel-k">{bi("Builds on", "前置")}</span>{builds}</div>'
    if leads:
        flow += f'<div><span class="rel-k">{bi("Leads to", "后续")}</span>{leads}</div>'
    flow += "</div>"
    src = (f'<a class="src" href="{UPSTREAM}{w["folder"]}" rel="noopener">{bi("Original materials on GitHub ↗", "课程原始资料 ↗")}</a>'
           if w["folder"] else "")
    q_en, q_zh = QUESTION[n]
    question = (f'<div class="cq"><div class="cq-k">{bi("Core question", "核心问题")}</div>'
                f'<div class="cq-q">{bi(esc(q_en), esc(q_zh))}</div></div>')
    steps = []
    for i, s in enumerate(w["sections"], 1):
        se, sz = SECTION.get((n, s["id"]), ("", ""))
        steps.append(f'<li><span class="step-n">{i}</span><div><a class="step-t" href="#s-{n}-{s["id"]}">{bi(s["en"], s["zh"])}</a>'
                     f'<p class="step-d">{bi(esc(se), esc(sz))}</p></div></li>')
    hint = bi("click a node to fold · ↗ and leaves open the note", "点击节点折叠/展开 · ↗ 与末端节点跳到笔记")
    structure = (
        '<section class="structure">'
        f'<div class="st-chain card"><h2>{bi("Logic chain", "逻辑链")}</h2><ol class="chain-steps">{"".join(steps)}</ol></div>'
        f'<div class="st-map card"><h2>{bi("Mind map", "本讲思维导图")}<span class="hint">{hint}</span></h2>'
        f'{mindmap(f"mm-w{n:02d}", week_tree(n, True), 9, False, "mm-week")}</div>'
        '</section>')
    secs = []
    for i, s in enumerate(w["sections"], 1):
        se, sz = SECTION.get((n, s["id"]), ("", ""))
        cards = "".join(concept_html(*rendered[d["id"]], n) for d in s["concepts"])
        secs.append(f'<section class="sec" id="s-{n}-{s["id"]}"><header class="sec-h"><span class="sec-n">{n}.{i}</span>'
                    f'<div><h2>{bi(s["en"], s["zh"])}</h2><p class="sec-d">{bi(esc(se), esc(sz))}</p></div></header>{cards}</section>')
    recap = ""
    if w["recap_en"] or w["recap_zh"]:
        _src["id"] = None
        recap = (f'<section class="recap" id="recap-{n}"><h2>{bi("Exam checklist", "考点速记")}</h2>'
                 f'<div class="bi-body"><div class="l-en" lang="en">{md(w["recap_en"], "en")}</div>'
                 f'<div class="l-zh" lang="zh-CN">{md(w["recap_zh"], "zh")}</div></div></section>')
    h = level
    head = (f'<header class="wk-head"><div class="wk-badge">W{n}</div>'
            f'<div class="kicker">Week {n:02d} · {bi(mod["en"], mod["zh"])}</div>'
            f'<{h}>{bi(w["en"], w["zh"])}</{h}>{question}'
            f'<div class="bi-body lede"><p class="l-en" lang="en">{inline(w["sum_en"], "en")}</p>'
            f'<p class="l-zh" lang="zh-CN">{inline(w["sum_zh"], "zh")}</p></div>{flow}{src}</header>')
    return f'<div class="wk m-{w["module"]}" id="week-{n}">{head}{structure}{"".join(secs)}{recap}</div>'


def prevnext(n):
    ks = sorted(M.WEEKS)
    i = ks.index(n)
    out = '<nav class="pn">'
    if i > 0:
        p = M.WEEKS[ks[i - 1]]
        out += f'<a href="{p["slug"]}.html">← W{p["n"]} {bi(p["en"], p["zh"])}</a>'
    else:
        out += "<span></span>"
    if i < len(ks) - 1:
        q = M.WEEKS[ks[i + 1]]
        out += f'<a href="{q["slug"]}.html">W{q["n"]} {bi(q["en"], q["zh"])} →</a>'
    return out + "</nav>"


# ---------------------------------------------------------------- special pages
def index_page():
    n_links = sum(len(v) for v in REFS.values())
    stats = (f'<div class="stats"><div><b>{len(M.WEEKS)}</b>{bi("lectures", "讲")}</div>'
             f'<div><b>{sum(len(w["sections"]) for w in M.WEEKS.values())}</b>{bi("sections", "小节")}</div>'
             f'<div><b>{len(M.CONCEPTS)}</b>{bi("concepts", "知识点")}</div>'
             f'<div><b>{len(M.CMDS)}</b>{bi("commands", "命令")}</div>'
             f'<div><b>{n_links}</b>{bi("cross-links", "概念互链")}</div></div>')
    # route: modules in order, each week = its core question
    rows = []
    for mod in MODULES:
        cards = []
        for n in sorted(M.WEEKS):
            w = M.WEEKS[n]
            if w["module"] != mod["id"]:
                continue
            q_en, q_zh = QUESTION[n]
            secs = "".join(f'<li>{bi(esc(s["en"]), esc(s["zh"]))}</li>' for s in w["sections"])
            cards.append(f'<a class="rcard" href="{w["slug"]}.html"><span class="rc-w">W{n}</span>'
                         f'<span class="rc-t">{bi(esc(w["en"]), esc(w["zh"]))}</span>'
                         f'<span class="rc-q">{bi(esc(q_en), esc(q_zh))}</span>'
                         f'<ol class="rc-s">{secs}</ol></a>')
        rows.append(f'<div class="rrow m-{mod["id"]}"><div class="rr-h"><h3>{bi(mod["en"], mod["zh"])}</h3>'
                    f'<p>{bi(mod["d_en"], mod["d_zh"])}</p></div><div class="rr-cards">{"".join(cards)}</div></div>')
    threads = []
    for t in THREADS:
        for cid in t["chain"]:
            if cid not in M.BY_ID:
                ERRORS.append(f"[thread {t['id']}] unknown {cid}")
        stops = "".join(f'<li>{chip(cid)}</li>' for cid in t["chain"] if cid in M.BY_ID)
        threads.append(f'<div class="thread"><div class="th-h"><h3>{bi(t["en"], t["zh"])}</h3><p>{bi(t["d_en"], t["d_zh"])}</p></div>'
                       f'<ol class="metro">{stops}</ol></div>')
    body = f'''<section class="hero">
<div class="hero-txt">
<div class="kicker">COMS10012 / COMSM0085 · Weeks 0–10 · TB1</div>
<h1>{bi("Software Tools", "Software Tools")}<span class="h1-sub">{bi("structured revision notes", "系统化复习笔记")}</span></h1>
<p class="lede">{bi("Four modules, eleven lectures, one question per lecture. Start from the mind map, follow the route, then use the threads to connect ideas across weeks.",
                     "四个模块、十一讲、每讲一个核心问题。先看思维导图建立全局，再按学习路线逐讲复习，最后用知识主线把不同讲的概念串起来。")}</p>
<div class="hero-cta"><a class="btn primary" href="mindmap.html">{bi("Open the mind map", "打开思维导图")} →</a><a class="btn" href="w01.html">{bi("Start at Week 1", "从第 1 讲开始")}</a><a class="btn" href="print.html">{bi("Open-book print pack", "开卷打印包")}</a></div>
</div>
{stats}
</section>
<section class="home-map card"><div class="sec-title"><span class="sec-num">01</span><h2>{bi("Mind map", "思维导图")}</h2>
<span class="hint">{bi("click to unfold weeks → sections → notes · drag to move", "点击展开 讲 → 小节 → 知识点 · 拖动平移")}</span><a class="more" href="mindmap.html">{bi("Full screen", "全屏查看")} →</a></div>
{mindmap("mm-home", course_tree(), 2, True, "mm-home")}</section>
<section class="route"><div class="sec-title"><span class="sec-num">02</span><h2>{bi("Learning route", "学习路线")}</h2><span class="hint">{bi("each lecture answers one question", "每一讲回答一个问题")}</span></div>{"".join(rows)}</section>
<section class="threads"><div class="sec-title"><span class="sec-num">03</span><h2>{bi("Threads across the unit", "贯穿全课的知识主线")}</h2><span class="hint">{bi("the same idea, met again in later weeks", "同一个思想，在后面的讲里再次出现")}</span></div>{"".join(threads)}</section>
<section class="howto">{bi("Language switch (top right): 中文 / 对照 / EN. English terms always stay visible because the exam is in English. Chips are links; <b>W3</b> marks a concept from another week.",
                       "右上角切换 中文 / 对照 / EN。考试是英文的，所以英文术语始终显示。小标签都是链接，带 <b>W3</b> 的来自其它讲。")}</section>'''
    return page("Software Tools 复习笔记 · Revision", body, side=False)


def mindmap_page():
    body = (f'<div class="mm-page-h"><h1>{bi("Mind map of the whole unit", "全课程思维导图")}</h1>'
            f'<p class="lede">{bi("Course → modules → lectures → sections → notes. Click a node to fold or unfold it; ↗ and the last level open the note. Drag to move, use − / + / ⤢ to zoom.", "课程 → 模块 → 讲 → 小节 → 知识点。点击节点折叠/展开；↗ 与最末一级打开对应笔记。拖动平移，用 − / + / ⤢ 缩放。")}</p></div>'
            + mindmap("mm-full", course_tree(), 2, True, "mm-full"))
    return page("Mind map 思维导图 · Software Tools", body, side=False)


def glossary_page():
    rows = []
    for d in sorted(M.CONCEPTS, key=lambda x: x["t_en"].lower().lstrip("$.-`/")):
        w = M.WEEKS[d["week"]]
        sec = next(s for s in w["sections"] if s["id"] == d["sec"])
        rows.append(f'<tr><td><a href="{href(d["id"])}"><b>{esc(d["t_en"])}</b></a></td><td>{esc(d["t_zh"])}</td>'
                    f'<td><span class="cw m-{w["module"]}">W{d["week"]}</span></td><td>{bi(esc(sec["en"]), esc(sec["zh"]))}</td></tr>')
    body = f'''<h1>{bi("Glossary", "术语表")}</h1>
<p class="lede">{bi(f"All {len(M.CONCEPTS)} concepts, A–Z by English term. Type to filter (English or Chinese).", f"全部 {len(M.CONCEPTS)} 个知识点，按英文术语排序。输入中英文均可筛选。")}</p>
<input id="q" class="search" type="search" placeholder="filter… 例如 rebase / 外键 / setuid" autocomplete="off">
<div class="tbl"><table class="gloss filterable"><thead><tr><th>Term</th><th>中文</th><th>Week</th><th>{bi("Section", "小节")}</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'''
    return page("Glossary 术语表 · Software Tools", body)


def commands_page():
    blocks = []
    for n in sorted(M.WEEKS):
        cs = [x for x in M.CMDS if x["week"] == n]
        if not cs:
            continue
        w = M.WEEKS[n]
        rows = []
        for x in cs:
            if x["cid"] and x["cid"] not in M.BY_ID:
                ERRORS.append(f"[cmd {x['name']}] unknown concept {x['cid']}")
            link = chip(x["cid"]) if x["cid"] in M.BY_ID else ""
            rows.append(f'<tr><td><code>{esc(x["name"])}</code></td><td>{bi(inline(x["en"], "en"), inline(x["zh"], "zh"))}</td><td>{link}</td></tr>')
        blocks.append(f'<section class="cmdblock m-{w["module"]}"><h2><a href="{w["slug"]}.html">W{n} · {bi(w["en"], w["zh"])}</a></h2>'
                      f'<div class="tbl"><table class="cmds filterable"><tbody>{"".join(rows)}</tbody></table></div></section>')
    body = f'''<h1>{bi("Command cheatsheet", "命令速查表")}</h1>
<p class="lede">{bi(f"{len(M.CMDS)} commands, options and syntax forms, grouped by week. Each links to the concept note where it is explained.", f"共 {len(M.CMDS)} 条命令、选项与语法，按讲分组，每条都链接到对应的知识点笔记。")}</p>
<input id="q" class="search" type="search" placeholder="filter… 例如 chmod / journalctl / JOIN" autocomplete="off">
{"".join(blocks)}'''
    return page("Commands 命令速查 · Software Tools", body)


# ---------------------------------------------------------------- main
CODE = {}


def assign_codes():
    for n in sorted(M.WEEKS):
        for si, s in enumerate(M.WEEKS[n]["sections"], 1):
            for ci, d in enumerate(s["concepts"], 1):
                CODE[d["id"]] = f"{n}.{si}.{ci}"


def print_page(rendered):
    weeks = sorted(M.WEEKS)
    # ---- cover
    toc = "".join(
        f'<li><a href="#pw-{n}"><b>W{n}</b> {bi(esc(M.WEEKS[n]["en"]), esc(M.WEEKS[n]["zh"]))}</a></li>' for n in weeks)
    exam = M.BY_ID["tb1-exam"]
    cover = f'''<section class="pp-cover">
<div class="kicker">COMS10012 / COMSM0085 · TB1 · Weeks 0–10</div>
<h1>{bi("Software Tools — open-book exam pack", "Software Tools 开卷考试打印包")}</h1>
<p class="pp-lede">{bi(f"{len(M.CONCEPTS)} notes, {len(M.CMDS)} commands, every lecture's checklist, and an A–Z index. Every note has a code <b>week.section.item</b> (e.g. <b>2.3.4</b>); arrows like <b>[2.3.4]</b> inside a note point to the related note.",
                       f"共 {len(M.CONCEPTS)} 个知识点、{len(M.CMDS)} 条命令、每讲考点速记，以及 A–Z 术语索引。每个知识点都有编号 <b>讲.小节.条目</b>（如 <b>2.3.4</b>）；笔记中的 <b>[2.3.4]</b> 表示相关知识点的位置。")}</p>
<div class="pp-howto"><b>{bi("How to use in the exam", "考场用法")}</b><ol>
<li>{bi("Know the term? Part D index → code → find it in Part C.", "知道英文术语 → 查 D 部分索引 → 按编号在 C 部分找到笔记。")}</li>
<li>{bi("Question names a command? Part B.", "题目里出现命令/选项 → 查 B 部分命令速查。")}</li>
<li>{bi("Need the big picture of a topic? Part A (one block per lecture).", "需要快速回忆某讲要点 → 查 A 部分考点速记。")}</li>
</ol></div>
<div class="pp-parts"><div><b>A</b>{bi("Exam checklists", "考点速记")}</div><div><b>B</b>{bi("Command cheatsheet", "命令速查")}</div><div><b>C</b>{bi("All notes by lecture", "全部知识点（按讲）")}</div><div><b>D</b>{bi("A–Z term index", "A–Z 术语索引")}</div></div>
<h3>{bi("Lectures", "目录")}</h3><ol class="pp-toc">{toc}</ol>
<div class="pp-c pp-exam"><div class="pp-cb"><div class="l-en" lang="en">{rendered["tb1-exam"][1]}</div><div class="l-zh" lang="zh-CN">{rendered["tb1-exam"][2]}</div></div></div>
</section>'''
    # ---- A: checklists
    recaps = []
    for n in weeks:
        w = M.WEEKS[n]
        if not (w["recap_en"] or w["recap_zh"]):
            continue
        recaps.append(f'<div class="pp-recap m-{w["module"]}"><h3><span class="pp-wn">W{n}</span>{bi(esc(w["en"]), esc(w["zh"]))}</h3>'
                      f'<div class="pp-cb"><div class="l-en" lang="en">{md(w["recap_en"], "en")}</div><div class="l-zh" lang="zh-CN">{md(w["recap_zh"], "zh")}</div></div></div>')
    part_a = f'<section class="pp-part" id="pa"><h2 class="pp-h"><span>A</span>{bi("Exam checklists", "考点速记")}</h2>{"".join(recaps)}</section>'
    # ---- B: commands
    cblocks = []
    for n in weeks:
        cs = [x for x in M.CMDS if x["week"] == n]
        if not cs:
            continue
        rows = "".join(f'<tr><td><code>{esc(x["name"])}</code></td><td class="l-en">{inline(x["en"], "en")}</td>'
                       f'<td class="l-zh">{inline(x["zh"], "zh")}</td><td class="pp-ref">{CODE.get(x["cid"], "")}</td></tr>' for x in cs)
        cblocks.append(f'<tr class="pp-tr-h m-{M.WEEKS[n]["module"]}"><th colspan="4">W{n} · {bi(esc(M.WEEKS[n]["en"]), esc(M.WEEKS[n]["zh"]))}</th></tr>{rows}')
    part_b = (f'<section class="pp-part" id="pb"><h2 class="pp-h"><span>B</span>{bi("Command cheatsheet", "命令速查")}</h2>'
              f'<table class="pp-cmds"><tbody>{"".join(cblocks)}</tbody></table></section>')
    # ---- C: notes
    wk_html = []
    for n in weeks:
        w = M.WEEKS[n]
        q_en, q_zh = QUESTION[n]
        chain = " → ".join(f'{i}. {bi(esc(s["en"]), esc(s["zh"]))}' for i, s in enumerate(w["sections"], 1))
        parts = [f'<div class="pp-week m-{w["module"]}" id="pw-{n}"><div class="pp-wh"><span class="pp-wn">W{n}</span>'
                 f'<div><h2>{bi(esc(w["en"]), esc(w["zh"]))}</h2>'
                 f'<p class="pp-q"><b>Q</b> {bi(esc(q_en), esc(q_zh))}</p><p class="pp-chain">{chain}</p></div></div>']
        for si, s in enumerate(w["sections"], 1):
            parts.append(f'<h3 class="pp-sh"><span>{n}.{si}</span>{bi(esc(s["en"]), esc(s["zh"]))}</h3>')
            for d in s["concepts"]:
                _, en, zh, code = rendered[d["id"]]
                star = '<span class="pp-star">★</span>' if d["exam"] else ""
                parts.append(f'<div class="pp-c" id="p-{d["id"]}"><div class="pp-ct"><span class="pp-code">{CODE[d["id"]]}</span>'
                             f'<b>{esc(d["t_en"])}</b><span class="pp-tz l-zh">{esc(d["t_zh"])}</span>{star}</div>'
                             f'<div class="pp-cb"><div class="l-en" lang="en">{en}</div><div class="l-zh" lang="zh-CN">{zh}</div></div>{code}</div>')
        parts.append("</div>")
        wk_html.append("".join(parts))
    part_c = f'<section class="pp-part" id="pc"><h2 class="pp-h"><span>C</span>{bi("All notes by lecture", "全部知识点（按讲）")}</h2>{"".join(wk_html)}</section>'
    # ---- D: index
    items = "".join(
        f'<li><span class="ix-t"><a href="#p-{d["id"]}"><b>{esc(d["t_en"])}</b></a> <span class="l-zh">{esc(d["t_zh"])}</span></span><span class="pp-ref">{CODE[d["id"]]}</span></li>'
        for d in sorted(M.CONCEPTS, key=lambda x: x["t_en"].lower().lstrip("$.-`/~<")))
    part_d = f'<section class="pp-part" id="pd"><h2 class="pp-h"><span>D</span>{bi("A–Z term index", "A–Z 术语索引")}</h2><ul class="pp-index">{items}</ul></section>'
    bar = (f'<div class="pp-bar"><button type="button" onclick="window.print()">{bi("Print / Save as PDF", "打印 / 另存为 PDF")}</button>'
           f'<a class="pp-dl" href="exam-pack-bilingual.pdf" download>{bi("Ready-made PDF (bilingual)", "下载现成 PDF（中英对照）")}</a>'
           f'<span>{bi("Tip: A4, scale 100%, tick “Background graphics”. Choose 对照 / 中文 / EN first; English terms are kept in every mode.", "提示：A4 纸、缩放 100%、勾选“背景图形”。先在右上角选 对照 / 中文 / EN；任何模式下英文术语都会保留。")}</span></div>')
    body = f'<div class="pp">{bar}{cover}{part_a}{part_b}{part_c}{part_d}</div>'
    body = re.sub(r'href="w\d\d\.html#c-([\w-]+)"', r'href="#p-\1"', body)
    return page("Open-book exam pack 开卷打印包 — Software Tools", body, side=False)


def main():
    assign_codes()
    rendered = {d["id"]: render_concept(d) for d in M.CONCEPTS}   # first pass fills REFS
    pages = {}
    for n in sorted(M.WEEKS):
        w = M.WEEKS[n]
        pages[f'{w["slug"]}.html'] = page(f'W{n} {w["en"]} · {w["zh"]} — Software Tools',
                                          week_main(n, rendered) + prevnext(n), active=n)
    allbody = (f'<h1>{bi("All lectures in one page", "全部内容（单页 / 打印版）")}</h1>'
               f'<p class="lede">{bi("Everything on one page: handy for Ctrl+F and for printing notes for the open-book exam.", "全部内容在一页：方便 Ctrl+F 搜索，也方便打印成开卷考试用的笔记。")}</p>'
               + "".join(week_main(n, rendered, "h1") for n in sorted(M.WEEKS)))
    # on all.html, links should stay on the page
    allbody = re.sub(r'href="w\d\d\.html#', 'href="#', allbody)
    allbody = re.sub(r'"h": "w\d\d\.html#', '"h": "#', allbody)
    pages["all.html"] = page("All-in-one 全部内容 — Software Tools", allbody)
    pages["glossary.html"] = glossary_page()
    pages["commands.html"] = commands_page()
    pages["index.html"] = index_page()
    pages["mindmap.html"] = mindmap_page()
    pages["print.html"] = print_page(rendered)
    if ERRORS:
        print("\n".join(ERRORS))
        sys.exit(1)
    for name, text in pages.items():
        (OUT / name).write_text(text, encoding="utf-8")
    print(f"ok: {len(pages)} pages, {len(M.CONCEPTS)} concepts, {len(M.CMDS)} commands, "
          f"{sum(len(v) for v in REFS.values())} cross-links")


if __name__ == "__main__":
    main()
