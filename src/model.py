"""Tiny content model for the revision site.

Content files call W(), S(), c() and cmd() in order:
    W(3)                                  # switch to week 3 (week must be declared first)
    S("grep", "grep: search", "grep：搜索")  # start a section
    c("grep", "grep", "全局正则搜索", en=..., zh=..., code=..., see=[...])
    cmd("grep", "print lines matching a regex", "打印匹配正则的行", "grep")

Body markup (en= / zh=):
    - item            bullet list
    | a | b |         table (first row = header, |---| rows skipped)
    ! text            highlighted note / exam point
    ## Heading        small sub-heading
    ```  ...  ```     verbatim block
    `code`  **bold**  [[concept-id]]  [[concept-id|custom label]]
"""

WEEKS = {}      # n -> dict
CONCEPTS = []   # ordered list of dicts
BY_ID = {}
CMDS = []       # dicts
_cur = {"w": None, "s": None}


def week(n, module, en, zh, sum_en, sum_zh, builds=(), leads=(),
         recap_en="", recap_zh="", folder=""):
    WEEKS[n] = dict(n=n, slug=f"w{n:02d}", module=module, en=en, zh=zh,
                    sum_en=sum_en, sum_zh=sum_zh, builds=list(builds),
                    leads=list(leads), recap_en=recap_en, recap_zh=recap_zh,
                    folder=folder, sections=[])


def W(n):
    _cur["w"] = n
    _cur["s"] = None


def S(sid, en, zh):
    w = WEEKS[_cur["w"]]
    sec = dict(id=sid, en=en, zh=zh, concepts=[])
    w["sections"].append(sec)
    _cur["s"] = sec


def c(cid, t_en, t_zh, en="", zh="", code="", see=(), exam=False):
    if cid in BY_ID:
        raise ValueError(f"duplicate concept id {cid}")
    d = dict(id=cid, week=_cur["w"], sec=_cur["s"]["id"], t_en=t_en, t_zh=t_zh,
             en=en, zh=zh, code=code, see=list(see), exam=exam)
    CONCEPTS.append(d)
    BY_ID[cid] = d
    _cur["s"]["concepts"].append(d)
    return d


def cmd(name, en, zh, cid=None):
    CMDS.append(dict(name=name, en=en, zh=zh, cid=cid, week=_cur["w"]))
