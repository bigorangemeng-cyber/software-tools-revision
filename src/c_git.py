from model import W, S, c, cmd

# =====================================================================  W4
W(4)
S("why", "Why version control", "为什么要版本控制")
c("version-control", "Version control", "版本控制", exam=True,
  en=r"""
- Tracking and managing different versions of files; software automates recording the **differences** between versions, viewing history and **reverting**. (Ends `final_v2_final_REALFINAL.c`.)
- For one person: a backup / undo button, a record of how and why decisions were made, freedom to experiment, knowing exactly which version was released.
- Most valuable with **collaboration**: several people improve the *same original* code independently (xrealloc fix, longest_ext, asserts, comments) → someone must **merge** them ([[merge]]).
- Also: hotfix v1.0 while developing v2.0; two friends on separate features; trace exactly which edits one (malicious) contributor made (`git blame`).
""",
  zh=r"""
- 跟踪和管理文件的不同版本；软件自动记录版本之间的**差异**、查看历史、**回退**。（告别 `final_v2_final_REALFINAL.c`。）
- 对个人：备份 / 撤销按钮、记录决策的来龙去脉、放心尝试新想法、确切知道发布的是哪个版本。
- 最大价值在**协作**：多人各自基于*同一份原始*代码改进（xrealloc 修复、longest_ext、断言、注释）→ 必须有人把它们**合并**（[[merge]]）。
- 还有：一边开发 v2.0 一边紧急修 v1.0；两个朋友各开发一个功能；精确追查某个（恶意）贡献者改了哪些地方（`git blame`）。
""",
  see=["vcs-landscape", "merge", "branch"])

c("vcs-landscape", "VCS landscape & Git's origin", "版本控制系统概览与 Git 起源",
  en=r"""
- Others: RCS, CVS, Subversion (`svn`), Darcs, Mercurial (`hg`), Fossil. Git dominates (~94% of developers, 2025 survey).
- Created by Linus Torvalds in 2005 for the Linux kernel: "a stupid (but extremely fast) directory content manager". Git tracks **directory contents**.
""",
  zh=r"""
- 其它系统：RCS、CVS、Subversion（`svn`）、Darcs、Mercurial（`hg`）、Fossil。Git 占绝对主导（2025 年调查约 94% 开发者使用）。
- 2005 年 Linus Torvalds 为管理 Linux 内核开发而写：“一个愚蠢（但极快）的目录内容管理器”。Git 跟踪的是**目录内容**。
""",
  see=["version-control", "git-vs-github"])

S("local", "The local loop", "本地工作循环")
c("git-config", "git config & identity", "git config 与身份", exam=True,
  en=r"""
- Once per installation: `git config --global user.name "NAME"` and `user.email "EMAIL"` — recorded on every commit (who to blame, `man git-blame`). Not verified or used to send mail.
- `--global` = all your repositories (`~/.gitconfig`); drop it inside a repo for per-repository settings (separate work/personal identities).
- Commit message editor = `$EDITOR` (default often vim: Esc `ZZ` to save and quit). `export EDITOR=nano` in `~/.profile`.
- On lab-machine VMs, put the config in the Vagrantfile provision block with `privileged: false`.
- Later: `git config --global pull.rebase false|true` ([[pull-rebase]]).
""",
  zh=r"""
- 安装后设置一次：`git config --global user.name "名字"` 与 `user.email "邮箱"`——会记录在每次提交上（出问题找谁，`man git-blame`）。不会被验证，也不会用来发邮件。
- `--global` = 你所有的仓库（`~/.gitconfig`）；在仓库内去掉它则只对该仓库生效（区分工作/个人身份）。
- 写提交说明的编辑器 = `$EDITOR`（默认常是 vim：Esc 后 `ZZ` 保存退出）。在 `~/.profile` 中 `export EDITOR=nano`。
- 实验室机器上的虚拟机：把配置写进 Vagrantfile 的 provision 块，并加 `privileged: false`。
- 之后还会用到：`git config --global pull.rebase false|true`（[[pull-rebase]]）。
""",
  see=["vagrant", "editors", "startup-files"])

c("git-init", "Repository: git init", "仓库：git init", exam=True,
  en=r"""
- `git init` (in a directory) creates an empty repository in the hidden subfolder `.git` — the "official memory" of what the directory contained and how it changed.
- `git status` reports the directory relative to that memory; at first: "nothing to commit".
- Documentation: `man gittutorial`, `man giteveryday` ([[git-docs]]).
""",
  zh=r"""
- 在目录中执行 `git init`，会在隐藏子目录 `.git` 里创建空仓库——它是该目录内容及其变化的“官方记忆”。
- `git status` 报告目录相对于这份记忆的状态；一开始是 “nothing to commit”。
- 文档：`man gittutorial`、`man giteveryday`（[[git-docs]]）。
""",
  code=r"""
mkdir project1 && cd project1
git init
git status
""",
  see=["three-states", "git-docs"])

c("three-states", "Working tree, staging area, repository", "工作区、暂存区、仓库", exam=True,
  en=r"""
| State | Where | Shown by `git status` as |
|---|---|---|
| untracked | new file Git doesn't know | red, "Untracked files" |
| modified | tracked file changed in the working tree | red, "Changes not staged" |
| **staged** | queued for the next commit (index) | green, "Changes to be committed" |
| committed | stored in history | "working tree clean" |
- `git add` moves changes into the staging area; `git commit` records the staged snapshot. You can stage several files, edit again, then commit.
- Only **tracked** files are affected by checkout/restore.
""",
  zh=r"""
| 状态 | 含义 | `git status` 中显示为 |
|---|---|---|
| 未跟踪 untracked | Git 不认识的新文件 | 红色，“Untracked files” |
| 已修改 modified | 已跟踪文件在工作区被改动 | 红色，“Changes not staged” |
| **已暂存 staged** | 排队进入下一次提交（索引） | 绿色，“Changes to be committed” |
| 已提交 committed | 已存入历史 | “working tree clean” |
- `git add` 把改动放进暂存区；`git commit` 把暂存的快照记录下来。可以先暂存几个文件，再改，再提交。
- checkout/restore 只影响**已跟踪**的文件。
""",
  code=r"""
 working tree --git add--> staging area --git commit--> repository (.git)
      ^                                                     |
      +------------- git restore / git checkout ------------+
""",
  see=["commit", "git-status", "gitignore"])

c("commit", "git add & git commit", "git add 与 git commit", exam=True,
  en=r"""
- `git add FILE` stages a new or modified file (still needed for already-tracked files!). `git add .` stages everything new/changed here (careful: picks up stray files).
- `git commit` opens the editor for a **commit message**; `git commit -m "msg"` gives it inline (quotes for spaces). Every commit must have a message.
- `git commit -a` auto-stages all changes to **tracked** files (still `git add` new ones).
- Good messages: short one-line summary, then a detailed explanation for serious changes. Code, commit, repeat — small commits.
""",
  zh=r"""
- `git add 文件` 暂存新文件或修改（已跟踪的文件修改后也要再 add！）。`git add .` 暂存当前目录下所有新增/改动（小心带上无关文件）。
- `git commit` 打开编辑器写**提交说明**；`git commit -m "说明"` 直接给出（有空格要加引号）。每次提交必须有说明。
- `git commit -a` 自动暂存所有**已跟踪**文件的修改（新文件仍需 `git add`）。
- 好的说明：一行简短摘要，重要改动再附详细解释。写代码、提交、重复——小步提交。
""",
  code=r"""
git add main.c
git commit -m "first file"
git commit -a -m "Hi -> Hello"
""",
  see=["three-states", "git-log", "git-hooks"])

c("git-status", "git status", "git status",
  en=r"""
- Shows the current branch, staged / unstaged / untracked files, and whether you are ahead/behind a remote.
- Also tells you what to do next (in conflicts, rebases, detached HEAD) — **read the output**.
""",
  zh=r"""
- 显示当前分支、已暂存/未暂存/未跟踪的文件，以及与远程相比领先/落后。
- 还会提示下一步该怎么做（冲突、rebase、分离 HEAD 时）——**认真读输出**。
""",
  see=["three-states", "merge-conflict"])

c("git-log", "git log & commit hashes", "git log 与提交哈希", exam=True,
  en=r"""
- `git log` shows history: commit ID (SHA hash), author, date, message. `git log | less` to scroll (q quits); `git log --oneline --graph --all` for a branch picture.
- Refer to a commit by the first ~6+ characters of its hash — enough to be unambiguous.
""",
  zh=r"""
- `git log` 显示历史：提交 ID（SHA 哈希）、作者、时间、说明。`git log | less` 滚动查看（q 退出）；`git log --oneline --graph --all` 画出分支图。
- 引用某个提交时用哈希的前 6 位以上即可——只要不产生歧义。
""",
  see=["commit", "git-diff", "reflog"])

c("gitignore", ".gitignore", ".gitignore 忽略文件", exam=True,
  en=r"""
- Don't commit generated files (executables, `.o`, logs, outputs): they change constantly, aren't meaningful, and are platform-specific — others build from source. Large binaries (videos) can't be diffed meaningfully.
- `.gitignore` in the repo root: one pattern per line (`program`, `*.o`, `a.out`, `notes/`). Ignored files no longer appear as untracked.
- The `.gitignore` itself **should** be added and committed.
""",
  zh=r"""
- 不要提交生成的文件（可执行文件、`.o`、日志、输出）：它们一直变、没有意义、还与平台相关——别人应从源码自行构建。大型二进制（视频）也无法有意义地 diff。
- 仓库根目录的 `.gitignore`：每行一个模式（`program`、`*.o`、`a.out`、`notes/`）。被忽略的文件不再显示为未跟踪。
- `.gitignore` 本身**应该**被 add 并提交。
""",
  code=r"""
# .gitignore
program
*.o
a.out
notes/
""",
  see=["three-states", "globbing"])

S("history", "Using history: compare & undo", "利用历史：比较与撤销")
c("git-diff", "git diff", "git diff 比较差异", exam=True,
  en=r"""
- `git diff` = working tree vs last commit (what you haven't committed). `git diff HASH` = now vs that commit. `git diff HASH file` for one file. `git diff --staged` = staged vs last commit.
- Output: `-` lines removed, `+` lines added, `@@` hunk headers with line numbers.
""",
  zh=r"""
- `git diff` = 工作区 vs 最新提交（还没提交的改动）。`git diff HASH` = 当前 vs 某次提交。`git diff HASH 文件` 只看一个文件。`git diff --staged` = 暂存区 vs 最新提交。
- 输出：`-` 删除的行，`+` 新增的行，`@@` 是带行号的块头。
""",
  see=["git-restore", "patches"])

c("git-restore", "git restore", "git restore 恢复文件", exam=True,
  en=r"""
- `git restore FILE` discards uncommitted changes: file back to the last committed version.
- `git restore -s HASH FILE` sets your **working copy** of FILE to its version at HASH. `git status` then shows FILE as modified — you changed the file, not *where* you are in history.
- `git restore --staged FILE` unstages.
""",
  zh=r"""
- `git restore 文件` 丢弃未提交的修改：文件恢复为最近一次提交的版本。
- `git restore -s HASH 文件` 把文件的**工作副本**设为它在 HASH 时的版本。此后 `git status` 显示该文件已修改——你改的是文件，而不是你在历史中的*位置*。
- `git restore --staged 文件` 取消暂存。
""",
  see=["git-checkout", "three-states"])

c("git-checkout", "git checkout & detached HEAD", "git checkout 与分离 HEAD", exam=True,
  en=r"""
- **HEAD** = pointer to "where you are": normally the tip of the current branch.
- `git checkout HASH` = time travel: the whole working tree becomes that commit and HEAD points at it directly → **detached HEAD**. `git status` says "working tree clean" (files match where HEAD is).
- Back to the future: `git checkout main` (or `master`) re-attaches HEAD.
- restore vs checkout: restore changes file contents; checkout changes **Git's notion of when you are**. Watch out for losing uncommitted changes.
""",
  zh=r"""
- **HEAD** = 指向“你现在在哪”的指针：通常是当前分支的最新提交。
- `git checkout HASH` = 时间旅行：整个工作区变成那次提交，HEAD 直接指向它 → **分离 HEAD（detached HEAD）**。`git status` 显示 “working tree clean”（文件与 HEAD 所在位置一致）。
- 回到未来：`git checkout main`（或 `master`）让 HEAD 重新挂回分支。
- restore 与 checkout：restore 改文件内容；checkout 改变 **Git 认为你处于哪个时间点**。注意别丢了未提交的修改。
""",
  see=["git-restore", "branch", "revert-reset"])

c("revert-reset", "git revert vs git reset", "git revert 与 git reset", exam=True,
  en=r"""
| | `git revert HASH` | `git reset HASH` |
|---|---|---|
| How | adds a **new commit** that undoes HASH | moves the branch/HEAD pointer **back** to HASH |
| History | A, B → A, B, C (C's files = A's) | later commits disappear from the branch |
| Working tree | updated by the new commit | untouched (default); `--hard` resets files too |
| Shared/pushed history | **safe** | breaks others' copies; only for unpushed work |
""",
  zh=r"""
| | `git revert HASH` | `git reset HASH` |
|---|---|---|
| 做法 | 新增一个撤销 HASH 的**新提交** | 把分支/HEAD 指针**移回** HASH |
| 历史 | A, B → A, B, C（C 的文件 = A 的） | 之后的提交从分支上消失 |
| 工作区 | 随新提交更新 | 默认不动；`--hard` 连文件一起重置 |
| 已共享/已推送的历史 | **安全** | 会搞乱别人的副本；只用于未推送的工作 |
""",
  see=["git-secrets", "rebase-onto", "git-checkout"])

c("git-secrets", "Committed a secret?", "不小心提交了密码？",
  en=r"""
- Reverting is not enough once pushed: the secret stays in history. You'd need to rewrite history and **force push** — and still treat any password as **compromised**: change it at once.
""",
  zh=r"""
- 一旦推送，revert 并不够：秘密仍留在历史中。需要改写历史并**强制推送**——而且仍应把密码视为**已泄露**，立刻更换。
""",
  see=["revert-reset", "force-push"])

S("branches", "Branches", "分支")
c("branch", "Branches", "分支", exam=True,
  en=r"""
- Parallel timelines. Default branch `master` or `main` (name doesn't matter, be consistent; you can rename/configure it).
- `git branch NAME` creates; `git branch` lists (current marked `*`); `git switch NAME` moves to it (older: `git checkout NAME`).
- New commits go on the current branch; logs diverge after the branch point. Switching changes files (a README added on `docs` disappears on `main`).
- Use: try something / develop a feature without breaking working code. A well-regulated repo: every change to main arrives as a merge from a feature branch.
- Delete: `git branch -d NAME` (merged), `git branch -D NAME` (force, unmerged work lost).
""",
  zh=r"""
- 平行时间线。默认分支 `master` 或 `main`（名字无所谓，保持一致；可改名或配置）。
- `git branch 名字` 创建；`git branch` 列出（当前分支带 `*`）；`git switch 名字` 切换（旧写法：`git checkout 名字`）。
- 新提交加在当前分支上；分叉点之后各分支日志不同。切换分支会改变文件（在 `docs` 上新增的 README 回到 `main` 就不见了）。
- 用途：尝试新想法 / 开发新功能而不破坏可用代码。规范的仓库：main 上的每次变更都来自功能分支的合并。
- 删除：`git branch -d 名字`（已合并），`git branch -D 名字`（强制，未合并的工作会丢失）。
""",
  code=r"""
git branch docs
git switch docs
git add README.md && git commit -m "Add README"
git switch main
git merge docs
git branch -d docs
""",
  see=["merge", "feature-branches", "git-checkout"])

c("merge", "git merge", "git merge 合并", exam=True,
  en=r"""
- `git merge BRANCH` brings BRANCH's commits into the **current** branch.
- If the timelines don't conflict (no same lines edited differently), Git merges automatically, creating a **merge commit** with two parents (editor opens with "Merge branch 'docs'"). Both edits survive; `git log` now includes the other branch's commits.
- If one side has no new commits, Git just moves the pointer (fast-forward).
- When both changed the same lines → [[merge-conflict]].
""",
  zh=r"""
- `git merge 分支` 把该分支的提交合并进**当前**分支。
- 若两条时间线不冲突（没有对同一行做不同修改），Git 自动合并，生成一个有两个父提交的**合并提交**（编辑器预填 “Merge branch 'docs'”）。两边的修改都保留；`git log` 中出现另一分支的提交。
- 若其中一方没有新提交，Git 只需移动指针（快进 fast-forward）。
- 双方改了同一行 → [[merge-conflict]]。
""",
  see=["branch", "merge-conflict", "rebase", "pull-push"])

S("remote", "Remotes & GitHub", "远程仓库与 GitHub")
c("git-vs-github", "Git is not GitHub", "Git 不等于 GitHub", exam=True,
  en=r"""
- **Git**: open-source tool. **GitHub**: proprietary developer platform (a **forge**) that hosts remote Git repositories plus collaboration features. Others: GitLab, Bitbucket, SourceHut.
- You can host your own with little more than an SSH server (bare repos, not covered).
- Each GitHub repo has a two-part name `OWNER/REPO` (e.g. `cs-uob/software-tools`).
""",
  zh=r"""
- **Git**：开源工具。**GitHub**：私有的开发者平台（一种**代码托管平台 forge**），托管远程 Git 仓库并提供协作功能。同类：GitLab、Bitbucket、SourceHut。
- 只要一台 SSH 服务器就能自己托管（裸仓库，本课不涉及）。
- 每个 GitHub 仓库名分两部分 `所有者/仓库名`（如 `cs-uob/software-tools`）。
""",
  see=["remote", "fork-pr"])

c("https-vs-ssh", "Connecting to GitHub: HTTPS vs SSH", "连接 GitHub：HTTPS 与 SSH",
  en=r"""
- HTTPS URL: fine for cloning public repos (no auth), but you can't push that way here.
- **SSH** (recommended): upload your **public** key in GitHub Settings → SSH and GPG keys; URL `git@github.com:USER/REPO.git`. Never upload a private key (GitHub warns).
- Some networks fail ("resource temporarily unavailable") → `Hostname ssh.github.com` in `~/.ssh/config`.
""",
  zh=r"""
- HTTPS 地址：克隆公开仓库没问题（无需认证），但这种方式在本课中不能推送。
- **SSH**（推荐）：在 GitHub Settings → SSH and GPG keys 上传你的**公钥**；地址 `git@github.com:用户/仓库.git`。绝不上传私钥（GitHub 会警告）。
- 某些网络会失败（“resource temporarily unavailable”）→ 在 `~/.ssh/config` 中写 `Hostname ssh.github.com`。
""",
  see=["ssh-keys", "ssh-config", "remote"])

c("remote", "Remotes: clone & remote add", "远程：clone 与 remote add", exam=True,
  en=r"""
- Joining an existing project: `git clone URL [DIR]` → local copy with a remote named **origin** already set up.
- Sharing an existing local repo: create an empty GitHub repo (no README), then `git remote add origin URL` and `git push -u origin main` (`-u` links local main to origin/main).
- `git remote show origin`: fetch/push URLs, HEAD branch, which local branch merges with / pushes to which remote branch.
""",
  zh=r"""
- 加入已有项目：`git clone 地址 [目录]` → 得到本地副本，名为 **origin** 的远程已配置好。
- 共享已有本地仓库：在 GitHub 新建空仓库（不要勾 README），然后 `git remote add origin 地址` 和 `git push -u origin main`（`-u` 把本地 main 关联到 origin/main）。
- `git remote show origin`：查看拉取/推送地址、HEAD 分支、哪个本地分支与哪个远程分支合并/推送。
""",
  code=r"""
git clone git@github.com:USERNAME/REPONAME.git
git remote add origin git@github.com:USERNAME/REPONAME.git
git push -u origin main
git remote show origin
""",
  see=["pull-push", "https-vs-ssh", "git-vs-github"])

c("pull-push", "git pull & git push", "git pull 与 git push", exam=True,
  en=r"""
- Commits only change your **local** repository.
- `git pull` = `git fetch` (download remote changes) + `git merge` (integrate them). `git push` uploads your commits.
- Habit: **pull before push**. If the remote has commits you don't have, `push` is **rejected** → `git pull` (merge, maybe resolve conflicts) → `git push`.
- Set once: `git config --global pull.rebase false` (merge on pull) — or `true` ([[pull-rebase]]).
""",
  zh=r"""
- 提交只改变你的**本地**仓库。
- `git pull` = `git fetch`（下载远程改动）+ `git merge`（合并进来）。`git push` 上传你的提交。
- 习惯：**先 pull 再 push**。远程有你没有的提交时，`push` 会被**拒绝** → `git pull`（合并，可能要解决冲突）→ `git push`。
- 设置一次：`git config --global pull.rebase false`（pull 时合并）——或 `true`（[[pull-rebase]]）。
""",
  see=["remote", "merge", "shared-access", "merge-conflict"])

c("git-docs", "Git documentation", "Git 文档",
  en=r"""
- `apropos git`, `apropos git -a tutorial`; `man gittutorial`, `man giteveryday` (everyday commands), `man git-merge`, `man git-rebase`, `man git-blame`. Each subcommand `git X` has `man git-X`.
- Focus for week 4: core commit loop; check/undo with history; branches; backing up to a remote.
""",
  zh=r"""
- `apropos git`、`apropos git -a tutorial`；`man gittutorial`、`man giteveryday`（日常命令）、`man git-merge`、`man git-rebase`、`man git-blame`。每个子命令 `git X` 都有 `man git-X`。
- 第 4 讲重点：提交循环；用历史检查/撤销；分支；备份到远程。
""",
  see=["man", "git-init"])

for n, e, z, k in [
    ("git config --global user.name/user.email", "set identity", "设置身份", "git-config"),
    ("git init", "create repository (.git)", "创建仓库", "git-init"),
    ("git status", "what changed / what's staged", "查看状态", "git-status"),
    ("git add F / git add .", "stage changes", "暂存修改", "commit"),
    ("git commit [-m msg] [-a]", "record staged snapshot", "提交", "commit"),
    ("git log [--oneline --graph --all]", "history", "查看历史", "git-log"),
    ("git diff [HASH] [F]", "compare with commit", "比较差异", "git-diff"),
    ("git restore [-s HASH] F", "reset a file's working copy", "恢复文件", "git-restore"),
    ("git checkout HASH / main", "time travel (detached HEAD) / back", "时间旅行 / 回到最新", "git-checkout"),
    ("git revert HASH", "new commit undoing HASH", "用新提交撤销", "revert-reset"),
    ("git reset [--hard] HASH", "move branch back (rewrite)", "移回分支指针（改写）", "revert-reset"),
    ("git branch [-d|-D] NAME", "list / create / delete branch", "列出 / 创建 / 删除分支", "branch"),
    ("git switch NAME", "change branch", "切换分支", "branch"),
    ("git merge NAME", "merge NAME into current", "合并到当前分支", "merge"),
    ("git clone URL", "copy a remote repository", "克隆远程仓库", "remote"),
    ("git remote add origin URL; remote show origin", "connect / inspect remote", "关联 / 查看远程", "remote"),
    ("git pull / git push [-u origin main]", "sync with remote", "与远程同步", "pull-push"),
]:
    cmd(n, e, z, k)

# =====================================================================  W5
W(5)
S("conflicts", "Merge conflicts", "合并冲突")
c("merge-conflict", "Merge conflicts", "合并冲突", exam=True,
  en=r"""
- Happen when two branches changed the **same lines** differently. Git merges everything else and stops: "CONFLICT (content): Merge conflict in webcode.c … fix conflicts and then commit the result."
- **Read the output.** Affected files are listed in `git status`. Ignore it and your code stops working.
- Markers in the file: `<<<<<<< HEAD` (your current branch's version) / `=======` / `>>>>>>> comments` (the incoming branch's version).
- Resolve: edit to the correct final text (one side, the other, or a combination — e.g. keep `xrealloc` *and* the line break), remove the markers, `git add` each file, `git commit` explaining the resolution.
- Can be several conflict points per file and several files. Careless merging loses functionality — you must **understand both versions**.
- Same markers appear in `git pull` and `git rebase` ([[rebase]]).
""",
  zh=r"""
- 两个分支对**同一行**做了不同修改时发生。Git 合并其余部分后停下：“CONFLICT (content): Merge conflict in webcode.c … fix conflicts and then commit the result.”
- **读输出。**受影响的文件会列在 `git status` 中。置之不理，代码就跑不了。
- 文件中的标记：`<<<<<<< HEAD`（当前分支的版本）/ `=======` / `>>>>>>> comments`（被合并进来的分支的版本）。
- 解决：把内容改成正确的最终版本（取一边、另一边或组合——例如保留 `xrealloc` *并且*保留换行），删掉标记，对每个文件 `git add`，再 `git commit` 说明如何解决。
- 一个文件可能有多处冲突，也可能多个文件冲突。合并不谨慎会丢功能——必须**理解两个版本**。
- `git pull` 和 `git rebase` 中出现的是同样的标记（[[rebase]]）。
""",
  code=r"""
    mime_map_size++;
<<<<<<< HEAD
    mime_map = xrealloc(mime_map, sizeof(struct mime_mapping) * mime_map_size);
=======
    mime_map = realloc(mime_map,
        sizeof(struct mime_mapping) * mime_map_size);
>>>>>>> comments
""",
  see=["merge", "pull-push", "rebase", "git-status"])

S("shared", "Collaborating with shared access", "有共享权限的协作")
c("shared-access", "Shared-access workflow", "共享权限工作流", exam=True,
  en=r"""
- Everyone has push rights to one remote; everyone `git clone`s it, works and commits locally.
- Sync: `git pull` then `git push`. Rejected push → pull, resolve, push. Conflicts are common here.
- `pull` = `fetch` + `merge`: you can `git fetch` first, inspect, then decide (merge or rebase).
- Etiquette: never push broken code. Team order matters: whoever pushes second resolves the conflict.
""",
  zh=r"""
- 所有人对同一个远程有推送权限；每人 `git clone`，在本地工作和提交。
- 同步：先 `git pull` 再 `git push`。推送被拒 → pull、解决冲突、再 push。这种模式下冲突很常见。
- `pull` = `fetch` + `merge`：可以先 `git fetch`，看清楚，再决定合并还是 rebase。
- 礼仪：永远别推送坏代码。顺序很重要：后推送的人负责解决冲突。
""",
  see=["pull-push", "merge-conflict", "feature-branches", "pull-rebase"])

c("feature-branches", "develop & feature branches", "develop 与功能分支",
  en=r"""
- Keep `main` stable; integrate on a shared `develop` branch; each person works on their own **feature branch**.
- Publish a branch: `git push --set-upstream origin NAME` (then plain `git push`). See remote branches: `git branch -a`.
- Finish a feature: commit → `git fetch` → `git switch develop` → `git pull` if behind → `git merge NAME` → resolve → `git push`.
- If develop moved on, rebase the feature onto it first (`git rebase develop`), which then needs a force push of the feature branch ([[force-push]]).
""",
  zh=r"""
- 保持 `main` 稳定；在共享的 `develop` 分支上集成；每人在自己的**功能分支**上开发。
- 发布分支：`git push --set-upstream origin 名字`（之后直接 `git push`）。查看远程分支：`git branch -a`。
- 完成功能：提交 → `git fetch` → `git switch develop` → 落后就 `git pull` → `git merge 名字` → 解决冲突 → `git push`。
- 若 develop 已前进，先把功能分支 rebase 到它上面（`git rebase develop`），之后功能分支需要强制推送（[[force-push]]）。
""",
  see=["branch", "shared-access", "rebase"])

S("noaccess", "Collaborating without access", "无权限的协作")
c("fork-pr", "Forks & pull requests", "Fork 与 Pull Request", exam=True,
  en=r"""
- For many collaborators (most open source) you don't hand out write access.
- Contributor **forks** (public copy under their account) → clones the fork → pushes commits to the fork → opens a **pull request** asking the owner to pull them.
- Owner reviews (discussion, requested changes), then merges — or ignores/declines. Maintainers needn't watch forks until a PR arrives.
- Side benefit: if a project is abandoned or refuses something, the community can adopt a fork as canonical.
""",
  zh=r"""
- 协作者众多（大多数开源项目）时，不会给每个人写权限。
- 贡献者 **fork**（在自己账号下的公开副本）→ 克隆 fork → 把提交推到 fork → 发起 **pull request**，请所有者拉取。
- 所有者审核（讨论、要求修改）后合并——或者忽略/拒绝。维护者在收到 PR 之前无需关心各个 fork。
- 附带好处：项目被放弃或拒绝某些改动时，社区可以把某个 fork 当作正统。
""",
  see=["shared-access", "patches", "git-vs-github"])

c("patches", "Patches: format-patch, apply, am", "补丁：format-patch、apply、am",
  en=r"""
- Old-school distributed development (e.g. email, private server without PR UI).
- Contributor: `git fetch` then `git format-patch origin/main` → patch file(s) describing how your commits differ from the remote.
- Owner: `git apply PATCH` only changes the working tree (review, then commit); `git am PATCH` applies it directly **as a commit** (keeps author & message).
""",
  zh=r"""
- 传统的分布式开发方式（如通过邮件、没有 PR 界面的私有服务器）。
- 贡献者：`git fetch` 后 `git format-patch origin/main` → 生成补丁文件，描述你的提交与远程的差异。
- 所有者：`git apply 补丁` 只修改工作区（审核后再提交）；`git am 补丁` 直接**作为提交**应用（保留作者和说明）。
""",
  see=["fork-pr", "git-diff"])

S("rebase", "Rewriting history: rebase", "改写历史：rebase")
c("rebase", "git rebase", "git rebase 变基", exam=True,
  en=r"""
- "Editing the historical record" — common cause of catastrophic repo problems.
- Use: a branch split from main at B; main moved on to D. `git switch branch; git rebase main` → Git finds the branch's commits missing from main, resets to main's tip, and **replays** them on top: the branch now appears to split from D.
- Conflicts appear one commit at a time with the usual markers; fix → `git add FILES` → `git rebase --continue` (you may edit the message). **No merge commit.**
- `git rebase --abort` gives up entirely; `git rebase --skip` throws away the current commit's changes (dangerous).
- Replayed commits are **new commits with new IDs** → don't rebase history others already have.
""",
  zh=r"""
- “篡改历史记录”——仓库灾难的常见原因。
- 用途：分支在 B 处从 main 分出；main 已前进到 D。`git switch branch; git rebase main` → Git 找出分支上 main 没有的提交，先回到 main 的最新提交，再把它们逐个**重放**上去：看起来分支是从 D 分出的。
- 冲突逐个提交出现，标记相同；修好 → `git add 文件` → `git rebase --continue`（可修改说明）。**不产生合并提交。**
- `git rebase --abort` 彻底放弃；`git rebase --skip` 丢弃当前这个提交的改动（危险）。
- 重放的提交是**新提交、ID 也是新的** → 别 rebase 别人已经拿到的历史。
""",
  code=r"""
before:  A--B--C--D        main          after:  A--B--C--D            main
              \                                          \
               E--F        branch                         E'--F'     branch
""",
  see=["merge", "merge-conflict", "rebase-onto", "interactive-rebase", "rebase-vs-merge"])

c("rebase-onto", "rebase --onto", "rebase --onto",
  en=r"""
- `git rebase --onto NEWBASE OLDBASE BRANCH` transplants the commits after OLDBASE (up to BRANCH) onto NEWBASE: e.g. `git rebase --onto master branch subbranch`.
- Delete commits from history: `git rebase --onto master~5 master~3 master` turns A-B-C-D-E-F into A-D-E-F (drops B, C).
- vs `git revert`: revert keeps history and adds undo commits; `--onto` makes the commits never have existed.
""",
  zh=r"""
- `git rebase --onto 新基点 旧基点 分支` 把旧基点之后（到该分支为止）的提交移植到新基点上：如 `git rebase --onto master branch subbranch`。
- 从历史中删除提交：`git rebase --onto master~5 master~3 master` 把 A-B-C-D-E-F 变成 A-D-E-F（删掉 B、C）。
- 与 `git revert` 对比：revert 保留历史并新增撤销提交；`--onto` 让那些提交像从未存在过。
""",
  see=["rebase", "revert-reset"])

c("interactive-rebase", "Interactive rebase -i", "交互式 rebase -i", exam=True,
  en=r"""
- `git rebase -i BASE` (e.g. `HEAD~5`) opens the to-do list of commits in your editor; change the word in front of each:
| Command | Effect |
|---|---|
| `pick` | use the commit as is |
| `reword` | use it, edit the message |
| `edit` | stop here for more changes (e.g. split a commit) |
| `squash` | meld into the previous commit |
| `drop` | remove the commit |
- Use: tidy a messy history ("My laptop was running low on battery", debugging back-and-forth) before proposing changes.
""",
  zh=r"""
- `git rebase -i 基点`（如 `HEAD~5`）在编辑器中打开提交待办列表；修改每行开头的命令：
| 命令 | 效果 |
|---|---|
| `pick` | 原样使用该提交 |
| `reword` | 使用，但修改说明 |
| `edit` | 停在这里做更多修改（如拆分提交） |
| `squash` | 合并进前一个提交 |
| `drop` | 删除该提交 |
- 用途：在提交改动前整理混乱的历史（“笔记本快没电了”、调试时的来回修改）。
""",
  see=["rebase", "reflog"])

c("pull-rebase", "pull.rebase", "pull.rebase 配置",
  en=r"""
- `git config --global pull.rebase true`: `git pull` = fetch + **rebase** your local commits on top of the remote's (instead of merge) → linear history. Can be set per repository.
- Manual equivalent: `git fetch; git rebase origin/main`.
- Some projects require rebased contributions for a linear timeline.
""",
  zh=r"""
- `git config --global pull.rebase true`：`git pull` = fetch + 把本地提交 **rebase** 到远程之上（而不是 merge）→ 线性历史。也可以按仓库单独设置。
- 手动等价操作：`git fetch; git rebase origin/main`。
- 有些项目要求贡献先 rebase，以保持线性时间线。
""",
  see=["pull-push", "rebase", "git-config"])

c("rebase-vs-merge", "Merge vs rebase", "merge 与 rebase 对比", exam=True,
  en=r"""
| | merge | rebase |
|---|---|---|
| History | keeps true shape; adds a merge commit | rewritten to look linear |
| Commit IDs | unchanged | replayed commits get new IDs |
| Conflicts | resolved once, in the merge commit | resolved per replayed commit |
| Safe on shared history? | yes | no (others' copies diverge; needs force push) |
| Finish after conflict | `git add` + `git commit` | `git add` + `git rebase --continue` |
""",
  zh=r"""
| | merge | rebase |
|---|---|---|
| 历史 | 保留真实形状；新增合并提交 | 改写成看起来线性 |
| 提交 ID | 不变 | 重放的提交获得新 ID |
| 冲突 | 在合并提交中一次解决 | 每个重放的提交分别解决 |
| 对共享历史安全吗 | 安全 | 不安全（别人的副本会分叉；需要强推） |
| 冲突后如何收尾 | `git add` + `git commit` | `git add` + `git rebase --continue` |
""",
  see=["merge", "rebase", "force-push"])

c("force-push", "Force push", "强制推送",
  en=r"""
- After rebasing a branch that was already pushed, the remote has commits your rewritten branch lacks → normal push rejected. `git push --force` (safer: `--force-with-lease`) overwrites the remote branch.
- Only on branches nobody else builds on (your own feature branch); never on shared main/develop.
""",
  zh=r"""
- 对已推送的分支 rebase 之后，远程有你改写后的分支所没有的提交 → 普通推送被拒绝。`git push --force`（更安全：`--force-with-lease`）覆盖远程分支。
- 只能用于没人基于它工作的分支（你自己的功能分支）；绝不用于共享的 main/develop。
""",
  see=["rebase", "feature-branches", "git-secrets"])

S("recover", "Recovering lost commits (puzzle, not examinable)", "找回丢失的提交（拓展，不考）")
c("reflog", "reflog, cherry-pick & objects", "reflog、cherry-pick 与对象库",
  en=r"""
- Git rarely truly deletes anything that was ever staged/committed. After a bad rebase:
- `git reflog` = log of where HEAD has been → find the lost commit ID (`git reflog | grep treasure`).
- Restore with `git checkout ID`, `git cherry-pick ID` (re-apply that commit on the current branch) or a diff/patch.
- Raw storage: `.git/objects/`; inspect with `git cat-file -p ID` (commit → tree → blobs).
- `git gc` garbage-collects unreachable objects (runs automatically now and then) → makes recovery impossible.
""",
  zh=r"""
- 凡是被暂存或提交过的内容，Git 很少真正删除。rebase 搞砸之后：
- `git reflog` = HEAD 去过哪里的日志 → 找到丢失的提交 ID（`git reflog | grep treasure`）。
- 恢复：`git checkout ID`、`git cherry-pick ID`（把该提交重新应用到当前分支）或用 diff/补丁。
- 底层存储：`.git/objects/`；用 `git cat-file -p ID` 查看（commit → tree → blob）。
- `git gc` 回收不可达对象（会不定期自动运行）→ 之后就找不回了。
""",
  see=["interactive-rebase", "git-log"])

for n, e, z, k in [
    ("<<<<<<< ======= >>>>>>>", "conflict markers", "冲突标记", "merge-conflict"),
    ("git fetch", "download remote changes only", "只下载远程改动", "shared-access"),
    ("git push --set-upstream origin NAME", "publish a branch", "发布分支", "feature-branches"),
    ("git branch -a", "include remote branches", "含远程分支", "feature-branches"),
    ("git format-patch origin/main", "make patch files", "生成补丁", "patches"),
    ("git apply P / git am P", "apply patch to tree / as commit", "应用补丁到工作区 / 作为提交", "patches"),
    ("git rebase main", "replay branch on main", "把分支重放到 main 上", "rebase"),
    ("git rebase --continue/--abort/--skip", "drive a rebase", "控制 rebase 过程", "rebase"),
    ("git rebase --onto NEW OLD BR", "transplant commits", "移植提交", "rebase-onto"),
    ("git rebase -i HEAD~N", "pick/reword/edit/squash/drop", "交互式整理提交", "interactive-rebase"),
    ("git config pull.rebase true", "rebase on pull", "pull 时 rebase", "pull-rebase"),
    ("git push --force-with-lease", "overwrite remote branch (careful)", "覆盖远程分支（小心）", "force-push"),
    ("git reflog; cherry-pick; cat-file -p; gc", "recover lost commits", "找回丢失提交", "reflog"),
]:
    cmd(n, e, z, k)
