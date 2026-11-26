from model import week

MODULES = [
    dict(id="intro", en="Orientation", zh="导论",
         d_en="What the unit is and how it is examined.", d_zh="课程定位与考核方式。"),
    dict(id="unix", en="UNIX basics", zh="UNIX 基础",
         d_en="Driving a POSIX system from the shell: admin, scripting, text processing.",
         d_zh="用 shell 驾驭 POSIX 系统：系统管理、脚本、文本处理。"),
    dict(id="git", en="Version control", zh="版本控制",
         d_en="Tracking history with Git, alone and with other people.",
         d_zh="用 Git 管理历史：单人使用与多人协作。"),
    dict(id="dev", en="Development", zh="开发实践",
         d_en="Checking that code is right (testing) and finding out why it is wrong (debugging).",
         d_zh="确认代码正确（测试），以及找出为何出错（调试）。"),
    dict(id="db", en="Databases", zh="数据库",
         d_en="Designing, querying and reasoning over stored data: SQL to Datalog.",
         d_zh="数据的设计、查询与推理：从 SQL 到 Datalog。"),
]

week(0, "intro", "Introduction", "课程导论",
     "What Software Tools is for, how labs work, and how the two open-book multiple-choice exams work.",
     "这门课学什么、实验课怎么上、两场开卷选择题考试怎么考。",
     leads=[1], folder="00-intro",
     recap_en="""
- Everything in lectures, reading and labs is examinable unless marked otherwise.
- TB1 exam = weeks 1–10, four-option multiple choice, open book.
""",
     recap_zh="""
- 讲座、指定阅读、实验内容（未特别注明的）全部可考。
- TB1 考试覆盖第 1–10 讲，四选一选择题，开卷。
""")

week(1, "unix", "System administration", "系统管理",
     "The shell and the manual, logging in remotely with SSH and keys, running a Debian VM with Vagrant, the filesystem hierarchy, packages, users/groups and permissions, services and logs.",
     "shell 与手册、用 SSH 和密钥远程登录、用 Vagrant 运行 Debian 虚拟机、文件系统层级、软件包、用户/组与权限、服务与日志。",
     builds=[0], leads=[2, 4], folder="01-sysadmin",
     recap_en="""
- Anatomy of `ls -l --human-readable ~`: prompt, command, flags (short/long), arguments.
- `man`, `man -k` / `apropos`; man sections (1 commands, 5 file formats, 8 admin).
- SSH: client `ssh` vs daemon `sshd` (TCP 22); first-connection host key → `known_hosts`; MITM.
- Keys: `ssh-keygen -t ed25519`; private key stays put (`600`), public key goes into `~/.ssh/authorized_keys`; `scp`; `~/.ssh/config`.
- Vagrant: `up / ssh / halt / destroy`; `/shared` synced folder; provisioning.
- FHS: `/bin /sbin /usr /etc /lib /home /root /tmp /var /dev /proc /sys /opt`.
- `apt update` (refresh index) vs `apt upgrade` (install newer versions); `sudo`; root = uid 0.
- DAC: owner/group/other × rwx; octal (`7=rwx 5=r-x 0=---`); directory r vs x; setuid/setgid/sticky.
- `systemctl status/start/enable --now`; `journalctl -u … --since … --boot`; `dmesg`.
""",
     recap_zh="""
- 拆解 `ls -l --human-readable ~`：提示符、命令、短/长选项、参数。
- `man`、`man -k` / `apropos`；手册分节（1 命令、5 文件格式、8 管理）。
- SSH：客户端 `ssh` 与守护进程 `sshd`（TCP 22）；首次连接主机密钥写入 `known_hosts`；中间人攻击。
- 密钥：`ssh-keygen -t ed25519`；私钥不外传（权限 `600`），公钥追加到 `~/.ssh/authorized_keys`；`scp`；`~/.ssh/config`。
- Vagrant：`up / ssh / halt / destroy`；共享目录 `/shared`；provision 预装。
- FHS 目录：`/bin /sbin /usr /etc /lib /home /root /tmp /var /dev /proc /sys /opt`。
- `apt update`（刷新索引）≠ `apt upgrade`（升级已装包）；`sudo`；root 的 uid 为 0。
- 自主访问控制：属主/属组/其他 × rwx；八进制（`7=rwx 5=r-x 0=---`）；目录的 r 与 x；setuid/setgid/sticky。
- `systemctl status/start/enable --now`；`journalctl -u … --since … --boot`；`dmesg`。
""")

week(2, "unix", "POSIX fundamentals: the shell", "POSIX 基础：Shell",
     "How the shell turns a line into arguments (splitting, globbing, quoting, variables, substitution), pipes and redirection, shell scripts and the PATH, job control, and permissions in practice.",
     "shell 如何把一行字变成参数（分词、通配、引号、变量、命令替换），管道与重定向，脚本与 PATH，作业控制，以及权限实操。",
     builds=[1], leads=[3, 6], folder="02-fundamentals",
     recap_en="""
- The shell expands **before** running: word splitting, globs, `$var`, `$( )`. Quote `"$var"`.
- Globs that match nothing stay literal; `\\*`, `'*'`, `"*"` all pass a literal `*`.
- `x=5` (no spaces); `VAR=v cmd` sets VAR only in cmd's environment; `$x` in the same line is expanded before.
- fd 0/1/2; `|` `>` `>>` `<` `2>` `2>&1` `<<<` `<<EOF`; `diff tmp <(ls -l)`.
- Filters: `cat head tail sort uniq wc tr cut`; `uniq` only removes *adjacent* duplicates → `sort | uniq`.
- Scripts: `#!/bin/sh` / `#!/usr/bin/env bash`, `chmod +x`, `$0 $1 $# $@ $?`, `test`/`[ ]`/`[[ ]]`, `&&` `||`.
- `set -e -u -o pipefail`; PATH lookup = first match wins; never put `.` on PATH.
- Jobs: `&`, Ctrl-Z, `fg`, `bg`, `jobs`, `wait`, Ctrl-C, Ctrl-D, `kill`.
- Permission rules: need x on every directory of the path; setuid (`chmod u+s`, `-rwsr-xr-x`); `visudo`.
""",
     recap_zh="""
- shell 在执行**之前**展开：分词、通配符、`$var`、`$( )`。变量要写成 `"$var"`。
- 无匹配的通配符原样保留；`\\*`、`'*'`、`"*"` 都能传入字面 `*`。
- `x=5`（等号两边无空格）；`VAR=v cmd` 只对 cmd 的环境生效；同一行里的 `$x` 已被提前展开。
- 文件描述符 0/1/2；`|` `>` `>>` `<` `2>` `2>&1` `<<<` `<<EOF`；`diff tmp <(ls -l)`。
- 过滤器：`cat head tail sort uniq wc tr cut`；`uniq` 只去掉**相邻**重复行 → 先 `sort` 再 `uniq`。
- 脚本：`#!/bin/sh` / `#!/usr/bin/env bash`，`chmod +x`，`$0 $1 $# $@ $?`，`test`/`[ ]`/`[[ ]]`，`&&` `||`。
- `set -e -u -o pipefail`；PATH 查找取第一个匹配；不要把 `.` 加进 PATH。
- 作业：`&`、Ctrl-Z、`fg`、`bg`、`jobs`、`wait`、Ctrl-C、Ctrl-D、`kill`。
- 权限：路径上每一级目录都要有 x；setuid（`chmod u+s` → `-rwsr-xr-x`）；用 `visudo` 改 sudoers。
""")

week(3, "unix", "Regular expressions", "正则表达式",
     "Regular expressions as a matching language (POSIX basic syntax), and the tools that use them: grep to search, sed to replace, awk to process fields, perl as the general-purpose option.",
     "正则表达式作为匹配语言（POSIX 基本语法），以及使用它的工具：grep 搜索、sed 替换、awk 处理字段、perl 作为通用方案。",
     builds=[2], leads=[4], folder="03-regex",
     recap_en="""
- `.` any char, `^` start, `$` end, `[abc]`, `[^abc]`, `[a-z0-9]`, `[[:alpha:]]`.
- BRE: `\\( \\)` group, `\\1` backref, `*` 0+, `\\+` 1+, `\\?` 0/1, `\\{n,m\\}`. ERE (`grep -E`, `sed -E`) drops the backslashes.
- Matching is left-to-right with backtracking and **greedy**.
- `grep -i -v -o -c -w -R -E -P`; `grep -c` counts lines, `grep -o … | wc -l` counts matches.
- `sed 's/re/rep/g'`, `&`, `\\1`, `-n` + `p`, `-i` in place, `y/abc/xyz/`.
- `awk -F, '/re/ { … } END { … }'`, `$0 $1 NF`, `$2 ~ /re/`.
""",
     recap_zh="""
- `.` 任意字符，`^` 行首，`$` 行尾，`[abc]`、`[^abc]`、`[a-z0-9]`、`[[:alpha:]]`。
- BRE：`\\( \\)` 分组，`\\1` 反向引用，`*` 0 次以上，`\\+` 1 次以上，`\\?` 0 或 1 次，`\\{n,m\\}`。ERE（`grep -E`、`sed -E`）去掉反斜杠。
- 从左到右匹配、可回溯，并且是**贪婪**的。
- `grep -i -v -o -c -w -R -E -P`；`grep -c` 数的是行，`grep -o … | wc -l` 数的是匹配次数。
- `sed 's/re/rep/g'`、`&`、`\\1`、`-n` 配合 `p`、`-i` 原地修改、`y/abc/xyz/`。
- `awk -F, '/re/ { … } END { … }'`、`$0 $1 NF`、`$2 ~ /re/`。
""")

week(4, "git", "Version control with Git", "Git 版本控制",
     "Why version control exists, the local Git loop (working tree → staging area → commits), using history to compare and undo, branching and merging, and syncing with a remote such as GitHub.",
     "为什么需要版本控制；本地 Git 循环（工作区 → 暂存区 → 提交）；利用历史比较与撤销；分支与合并；与 GitHub 等远程仓库同步。",
     builds=[1, 2], leads=[5, 6], folder="04-git",
     recap_en="""
- Core loop: `init` → edit → `add` → `commit` → `status`/`log`.
- `git diff` (working tree vs last commit), `git diff HASH`; `git restore f`, `git restore -s HASH f`.
- `checkout HASH` = detached HEAD (moves *you*); `restore` changes *files*.
- `revert` adds an inverse commit (safe when shared); `reset` moves the branch back (rewrites; `--hard` also changes files).
- `branch` / `switch` / `merge` / `branch -d`.
- `.gitignore` for build outputs; Git ≠ GitHub; `clone`, `remote add origin`, `pull` = `fetch` + `merge`, `push` rejected if remote has commits you lack.
""",
     recap_zh="""
- 核心循环：`init` → 修改 → `add` → `commit` → `status`/`log`。
- `git diff`（工作区 vs 最新提交）、`git diff HASH`；`git restore f`、`git restore -s HASH f`。
- `checkout HASH` 进入分离 HEAD（移动的是“你所在的时间点”）；`restore` 只改文件。
- `revert` 新增一个反向提交（共享后也安全）；`reset` 把分支指针移回（改写历史，`--hard` 连文件一起改）。
- `branch` / `switch` / `merge` / `branch -d`。
- 编译产物放进 `.gitignore`；Git ≠ GitHub；`clone`、`remote add origin`、`pull` = `fetch` + `merge`；远程有你没有的提交时 `push` 会被拒绝。
""")

week(5, "git", "Collaborating with Git", "Git 协作",
     "Resolving merge conflicts, collaborating with shared push access versus forks and pull requests or patches, and rewriting history with rebase.",
     "解决合并冲突；有共享推送权限的协作 vs. fork + pull request / 补丁；用 rebase 改写历史。",
     builds=[4], leads=[6], folder="05-git",
     recap_en="""
- Conflict markers `<<<<<<< HEAD` / `=======` / `>>>>>>> branch`; edit → `git add` → `git commit`.
- Shared access: `pull` before `push`; `fetch` then decide. Don't push broken code.
- No access: fork → push to fork → pull request → maintainer reviews and merges. Patches: `format-patch`, `apply`, `am`.
- `git rebase main` replays your commits on top; conflicts → `add` + `rebase --continue` / `--abort` / `--skip`.
- `rebase --onto`, `rebase -i` (pick, reword, edit, squash, drop); `pull.rebase true`.
- Rebase rewrites commit IDs: don't rebase what others already have (or you must force-push).
""",
     recap_zh="""
- 冲突标记 `<<<<<<< HEAD` / `=======` / `>>>>>>> 分支名`；手动编辑 → `git add` → `git commit`。
- 共享权限：先 `pull` 再 `push`；也可先 `fetch` 再决定。别推送坏代码。
- 无权限：fork → 推到自己的 fork → 发 pull request → 维护者审核合并。补丁：`format-patch`、`apply`、`am`。
- `git rebase main` 把你的提交“重放”到最新 main 之上；冲突时 `add` + `rebase --continue` / `--abort` / `--skip`。
- `rebase --onto`、`rebase -i`（pick、reword、edit、squash、drop）；`pull.rebase true`。
- rebase 会生成新的提交 ID：别 rebase 别人已经拿到的历史（否则只能强推）。
""")

week(6, "dev", "Testing", "测试",
     "What it means for code to be correct, assertions, unit tests with the Unity framework, test-driven development (red-green-refactor), property testing, fuzzing, formal verification, and automating tests with Git hooks and GitHub Actions.",
     "代码“正确”意味着什么；断言；用 Unity 框架写单元测试；测试驱动开发（红-绿-重构）；属性测试、模糊测试、形式化验证；用 Git 钩子和 GitHub Actions 自动运行测试。",
     builds=[2, 4], leads=[7], folder="06-testing",
     recap_en="""
- Testing asks: for all valid inputs, is the output the intended one? Most bugs = unclear spec.
- `assert()` checks internal assumptions at runtime; `-DNDEBUG` compiles them out.
- Unit test = call an interface with an input, compare with expected output. Regression = a test that used to pass now fails.
- Unity: `setUp`, `tearDown`, `TEST_ASSERT_EQUAL`, `UNITY_BEGIN` / `RUN_TEST` / `UNITY_END`; link with `-l unity`.
- TDD: RED (write failing test) → GREEN (simplest passing code) → REFACTOR (clean up, all tests pass).
- Property testing (QuickCheck), fuzzing (AFL), formal verification (Lean).
- Pre-commit hook: non-zero exit aborts the commit; `--no-verify` skips. GitHub Actions: `.github/workflows/*.yml`, `on: push`.
""",
     recap_zh="""
- 测试的问题：对所有合法输入，输出是否符合预期？多数 bug 来自规格不清。
- `assert()` 在运行时检查内部假设；`-DNDEBUG` 会把断言编译掉。
- 单元测试 = 用某输入调用接口，与期望输出比较。回归 = 以前能通过的测试现在失败。
- Unity：`setUp`、`tearDown`、`TEST_ASSERT_EQUAL`、`UNITY_BEGIN` / `RUN_TEST` / `UNITY_END`；链接 `-l unity`。
- TDD：红（先写会失败的测试）→ 绿（最简单的实现让它通过）→ 重构（整理代码，所有测试仍通过）。
- 属性测试（QuickCheck）、模糊测试（AFL）、形式化验证（Lean）。
- pre-commit 钩子：返回非零就中止提交；`--no-verify` 跳过。GitHub Actions：`.github/workflows/*.yml`，`on: push`。
""")

week(7, "dev", "Debugging", "调试",
     "Finding out why code is wrong using tools that work on the compiled binary: strace / ltrace for calls, valgrind for memory, gdb to stop, inspect and change a running program, and reverse-engineering crackmes.",
     "用作用于编译后二进制的工具找出代码为何出错：strace / ltrace 看调用，valgrind 查内存，gdb 暂停、查看并修改运行中的程序，以及逆向 crackme。",
     builds=[6, 2], leads=[8], folder="07-debugging",
     recap_en="""
- Testing says *that* something is wrong; debugging finds *why*.
- `strace cmd`, `strace -e openat cmd`, `strace -p PID`; `ltrace` for library calls.
- `valgrind --leak-check=yes ./prog`: invalid read/write, definitely / indirectly / possibly lost, still reachable.
- Compile with `-g -O0`. gdb: `run` (`r`), `break`/`b`, `step`/`s` (into calls), `next`/`n` (over calls), `stepi`/`si`, `continue`/`c`, `print`/`p`, `set var`, `info functions`, `info registers`, `disas`, `list`, `jump`.
- Crackme toolkit: `strings`, `ltrace`, `objdump -d`, gdb.
""",
     recap_zh="""
- 测试告诉你“有错”；调试找出“为什么错”。
- `strace cmd`、`strace -e openat cmd`、`strace -p PID`；`ltrace` 看库函数调用。
- `valgrind --leak-check=yes ./prog`：非法读写；definitely / indirectly / possibly lost、still reachable 的区别。
- 用 `-g -O0` 编译。gdb：`run`(`r`)、`break`/`b`、`step`/`s`（进入函数）、`next`/`n`（跳过函数）、`stepi`/`si`、`continue`/`c`、`print`/`p`、`set var`、`info functions`、`info registers`、`disas`、`list`、`jump`。
- crackme 工具箱：`strings`、`ltrace`、`objdump -d`、gdb。
""")

week(8, "db", "Relational databases: design", "关系数据库：设计",
     "Why data storage choices matter, ACID, the relational model (entities, attributes, records, relationships), keys, functional dependencies and normal forms, and creating tables in SQLite.",
     "为什么数据存储的选择很重要、ACID、关系模型（实体、属性、记录、联系）、键、函数依赖与范式，以及在 SQLite 中建表。",
     builds=[7], leads=[9], folder="08-sql",
     recap_en="""
- ACID = Atomic, Consistent, Isolated, Durable.
- Entity → table, attribute → column, record → row; relationships via foreign keys.
- Keys: candidate (minimal unique set), composite (>1 attribute), surrogate (invented ID), primary (chosen), foreign (another table's PK).
- X → Y: each X has at most one Y. Partial dependency (on part of a composite key) and transitive dependency (X→Y→Z).
- 1NF atomic values; 2NF no partial deps; 3NF no transitive deps; BCNF every determinant is a candidate key.
- `CREATE TABLE … PRIMARY KEY … FOREIGN KEY(x) REFERENCES t(y)`; `PRAGMA foreign_keys = ON;`; create referenced table first, drop in reverse order.
""",
     recap_zh="""
- ACID = 原子性、一致性、隔离性、持久性。
- 实体 → 表，属性 → 列，记录 → 行；联系通过外键表示。
- 键：候选键（最小唯一属性集）、复合键（多于一个属性）、代理键（人为编号）、主键（选定的）、外键（引用另一表的主键）。
- X → Y：每个 X 最多对应一个 Y。部分依赖（依赖复合键的一部分）与传递依赖（X→Y→Z）。
- 1NF 值原子；2NF 无部分依赖；3NF 无传递依赖；BCNF 每个决定因素都是候选键。
- `CREATE TABLE … PRIMARY KEY … FOREIGN KEY(x) REFERENCES t(y)`；`PRAGMA foreign_keys = ON;`；先建被引用表，删除时顺序相反。
""")

week(9, "db", "Relational databases: queries", "关系数据库：查询",
     "SQLite type affinity and constraints, SELECT with WHERE / ORDER BY / LIMIT, aggregates with GROUP BY and HAVING, joins, sub-queries, and updating data inside transactions.",
     "SQLite 类型亲和性与约束；SELECT 配合 WHERE / ORDER BY / LIMIT；GROUP BY 与 HAVING 聚合；连接；子查询；在事务中更新数据。",
     builds=[8], leads=[10], folder="09-sql",
     recap_en="""
- SQLite affinities: INTEGER, TEXT, BLOB, REAL, NUMERIC (+ NULL). Lengths like `VARCHAR(10)` are ignored → use `CHECK`.
- `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT …` (write order).
- `WHERE` filters rows before grouping; `HAVING` filters groups after.
- `count avg sum min max`; `LIKE '%x%'`, `IN (…)`, `IS NULL`.
- INNER (matches only), LEFT / RIGHT / FULL OUTER (keep unmatched side, fill NULL), CROSS (Cartesian product).
- Sub-query as a temporary table: `FROM (SELECT …)`.
- `UPDATE … SET … WHERE`, `ALTER TABLE`, upsert `ON CONFLICT … DO UPDATE`, `BEGIN TRANSACTION … END TRANSACTION`.
""",
     recap_zh="""
- SQLite 亲和类型：INTEGER、TEXT、BLOB、REAL、NUMERIC（以及 NULL）。`VARCHAR(10)` 这类长度会被忽略 → 用 `CHECK`。
- 书写顺序：`SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT …`。
- `WHERE` 在分组前过滤行；`HAVING` 在分组后过滤组。
- `count avg sum min max`；`LIKE '%x%'`、`IN (…)`、`IS NULL`。
- INNER（只保留匹配）、LEFT / RIGHT / FULL OUTER（保留未匹配一侧并补 NULL）、CROSS（笛卡尔积）。
- 子查询当作临时表：`FROM (SELECT …)`。
- `UPDATE … SET … WHERE`、`ALTER TABLE`、upsert `ON CONFLICT … DO UPDATE`、`BEGIN TRANSACTION … END TRANSACTION`。
""")

week(10, "db", "Databases beyond SQL: Datalog", "超越 SQL：Datalog",
     "Using SQL from a program safely (SQL injection and prepared statements), why recursive structures are awkward in SQL, and Datalog: facts, rules, queries and recursion, applied to access control.",
     "在程序中安全使用 SQL（SQL 注入与预编译语句）、为什么递归结构在 SQL 中很别扭，以及 Datalog：事实、规则、查询与递归，并用于访问控制。",
     builds=[9, 1], folder="10-datalog",
     recap_en="""
- Building SQL with `sprintf` + user input → SQL injection (`1 OR 1=1`). Fix: prepared statements (`?` + bind).
- Self-join finds one level up; an unknown depth needs recursion (`WITH RECURSIVE` in SQL, or Datalog).
- Datalog: atoms lowercase, variables Uppercase/`_`, facts `p(a).`, rules `head :- b1, b2.` (comma = AND, several rules = OR), queries `?- p(X).`
- Recursive rule: `ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).` plus a base case.
- `X != Y` to exclude self (e.g. siblings).
- Access control in Datalog: DAC, delegation, roles, MAC (Bell–LaPadula: no read up / no write down; Biba: the reverse).
""",
     recap_zh="""
- 用 `sprintf` 拼接用户输入构造 SQL → SQL 注入（`1 OR 1=1`）。修复：预编译语句（`?` 占位 + 绑定）。
- 自连接只能往上找一层；层数未知要用递归（SQL 的 `WITH RECURSIVE`，或 Datalog）。
- Datalog：原子小写，变量大写或 `_` 开头，事实 `p(a).`，规则 `head :- b1, b2.`（逗号 = 且，多条规则 = 或），查询 `?- p(X).`
- 递归规则：`ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).`，外加一条基础规则。
- 用 `X != Y` 排除自己（如兄弟姐妹）。
- 用 Datalog 做访问控制：DAC、委托、角色、MAC（Bell–LaPadula：不上读、不下写；Biba：相反）。
""")

THREADS = [
    dict(id="perm", en="Permissions & access control", zh="权限与访问控制",
         d_en="One idea, four appearances: who may read, write or execute what.",
         d_zh="同一个问题出现四次：谁能读、写、执行什么。",
         chain=["users-groups", "unix-dac", "special-bits", "ssh-key-perms", "path-permission", "setuid-demo", "sudoers", "datalog-access-control", "mac-models"]),
    dict(id="sec", en="Security mindset", zh="安全意识",
         d_en="Every week has a way things go wrong when an attacker is involved.",
         d_zh="几乎每一讲都有“遇到攻击者会怎样出错”的一面。",
         chain=["mitm", "host-key", "auth-factors", "setuid-demo", "git-secrets", "fuzzing", "crackme", "sql-injection", "prepared-statements"]),
    dict(id="text", en="Text processing pipeline", zh="文本处理流水线",
         d_en="Small tools joined by pipes, with regular expressions as the shared language.",
         d_zh="用管道串起小工具，正则表达式是它们共同的语言。",
         chain=["streams", "pipes", "filters", "regex", "grep", "sed", "awk", "unix-philosophy", "perl"]),
    dict(id="auto", en="Automation", zh="自动化",
         d_en="Stop typing the same thing: scripts, startup files, provisioning, hooks, CI, Makefiles.",
         d_zh="别重复手打：脚本、启动文件、预装配置、钩子、持续集成、Makefile。",
         chain=["shell-script", "startup-files", "vagrant", "b-script", "git-hooks", "github-actions", "makefile"]),
    dict(id="time", en="Git as time travel", zh="Git 时间旅行",
         d_en="From a linear history to parallel timelines that are merged and rewritten.",
         d_zh="从线性历史到可以合并、可以改写的平行时间线。",
         chain=["commit", "git-log", "git-restore", "git-checkout", "revert-reset", "branch", "merge", "merge-conflict", "rebase", "interactive-rebase", "reflog"]),
    dict(id="collab", en="Working with other people", zh="与他人协作",
         d_en="How work moves between people's copies of a project.",
         d_zh="工作成果如何在不同人的项目副本之间流动。",
         chain=["remote", "pull-push", "shared-access", "feature-branches", "fork-pr", "patches", "github-actions"]),
    dict(id="correct", en="Correctness ladder", zh="正确性阶梯",
         d_en="Increasing confidence that code does what it should, then tools for when it doesn't.",
         d_zh="对代码正确性的信心逐级提高；以及出错时用来定位的工具。",
         chain=["testing-question", "assert", "unit-test", "tdd", "property-testing", "fuzzing", "formal-verification", "debugging", "gdb"]),
    dict(id="data", en="From spreadsheets to deduction", zh="从电子表格到逻辑推理",
         d_en="Why we need databases, how to design them, query them, and what SQL can't express easily.",
         d_zh="为什么需要数据库、如何设计、如何查询，以及 SQL 不擅长表达什么。",
         chain=["bad-storage", "acid", "relational-model", "keys", "functional-dependency", "normal-forms", "create-table", "select", "join", "subquery", "self-join", "recursive-cte", "datalog", "datalog-recursion"]),
]
