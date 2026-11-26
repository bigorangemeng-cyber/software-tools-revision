# Software Tools 复习笔记 · Revision notes (Weeks 0–10)

Bilingual (中文 / English) structured revision notes for COMS10012 / COMSM0085 Software Tools, University of Bristol — TB1 material (lectures 0–10).
中英对照的 Software Tools 第 0–10 讲系统化复习笔记。

- `index.html`: mind map preview, learning route (one core question per lecture) and the threads across the unit (知识主线)
- `mindmap.html`: interactive mind map of the whole unit (全课程思维导图): course → modules → lectures → sections → notes; fold/unfold, zoom, drag
- `w00.html` … `w10.html`: one page per lecture: core question (核心问题), logic chain (逻辑链), the lecture's own mind map, then every concept is an anchored card with cross-links, see-also and auto-generated "referenced by" links
- `glossary.html`: every concept A–Z, filterable (术语表)
- `commands.html`: command cheatsheet by week (命令速查)
- `all.html`: everything on one page, for Ctrl+F and printing (open-book exam)

Language switch top-right: 中文 / 对照 / EN (remembered per browser; also `?lang=zh|en|both` in the URL).

## Edit & rebuild 修改与重新生成

All pages are generated from the Python files in `src/` (no dependencies, Python 3.8+):

```
src/c_weeks.py   weeks, modules, threads, exam checklists
src/c_logic.py   core question per lecture, one-line logic per section
src/c_unix.py    W0–W3     src/c_git.py  W4–W5
src/c_dev.py     W6–W7     src/c_db.py   W8–W10
```

Each concept is a `c("id", "English term", "中文术语", en="""…""", zh="""…""", code="""…""", see=[…])` call. In the text, `[[id]]` links to another concept; `- ` bullets, `| a | b |` tables, `! ` highlighted note, `` `code` ``, `**bold**`.

```
python3 src/build.py
```

The build stops and lists any broken `[[link]]`.

## Publish on GitHub Pages 发布

1. Create a new GitHub repository and push this folder's contents to it (the `.nojekyll` file stays):
   ```
   git init && git add . && git commit -m "Software Tools revision site"
   git branch -M main
   git remote add origin git@github.com:USERNAME/REPO.git
   git push -u origin main
   ```
2. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main` / `(root)`** → Save.
3. After a minute the site is at `https://USERNAME.github.io/REPO/`.

All links are relative, so the site also works when opened straight from disk.

---
Personal study notes built from the public course repository (github.com/cs-uob/software-tools); not official course material.
