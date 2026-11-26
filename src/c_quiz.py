"""Original practice questions in the style of the TB1 paper (four options).
q(week, concept_id, en, zh, options, answer_index, exp_en, exp_zh, code="")
An option is either a string (same in both languages, e.g. code) or (en, zh)."""

QUIZ = []


def q(week, cid, en, zh, options, ans, exp_en, exp_zh, code=""):
    QUIZ.append(dict(week=week, cid=cid, en=en, zh=zh, options=options, ans=ans,
                     exp_en=exp_en, exp_zh=exp_zh, code=code))


# ------------------------------------------------------------------ W1
q(1, "ssh-keys",
  "Priya can log in to `lab` with her password but key login fails. On the server, `~/.ssh` contains only `id_ed25519.pub` and `known_hosts`. What is missing?",
  "Priya 用密码能登录 `lab`，但密钥登录失败。服务器上 `~/.ssh` 里只有 `id_ed25519.pub` 和 `known_hosts`。缺了什么？",
  [("Her private key must also be copied to the server.", "还要把私钥也拷到服务器上。"),
   ("The public key must be appended to `~/.ssh/authorized_keys` on the server.", "要把公钥追加到服务器的 `~/.ssh/authorized_keys`。"),
   ("`known_hosts` on the server must contain her key.", "服务器的 `known_hosts` 必须包含她的密钥。"),
   ("The public key must be renamed to `id_rsa.pub`.", "公钥必须改名为 `id_rsa.pub`。")],
  1, "sshd only accepts keys listed in `authorized_keys`. The private key never leaves the client; `known_hosts` stores *server* keys on the client.",
  "sshd 只接受列在 `authorized_keys` 中的公钥。私钥从不离开客户端；`known_hosts` 是客户端用来存*服务器*公钥的。")
q(1, "unix-dac",
  "A file shows `-rwxr-x--- 1 root staff report.sh`. Which statement is true?",
  "某文件显示为 `-rwxr-x--- 1 root staff report.sh`。下列哪项正确？",
  [("A member of `staff` can run it but not modify it.", "`staff` 组成员能运行它但不能修改。"),
   ("Anyone can read it.", "任何人都能读它。"),
   ("Its octal mode is 755.", "它的八进制权限是 755。"),
   ("Only root can read it.", "只有 root 能读它。")],
  0, "Owner `rwx` (7), group `r-x` (5), others `---` (0): mode 750. Group members may read and execute but not write.",
  "属主 `rwx`（7），属组 `r-x`（5），其他人 `---`（0）：权限 750。组成员可读可执行，不可写。")
q(1, "unix-dac",
  "You can see the name of directory `d` with `ls`, but `cd d` says Permission denied. Which bit are you missing on `d`?",
  "你能用 `ls` 看到目录 `d` 的名字，但 `cd d` 提示 Permission denied。你在 `d` 上缺少哪个权限位？",
  ["r", "w", "x", "t"],
  2, "For a directory, `x` means you may enter it and access files inside; `r` lets you list its contents.",
  "对目录而言，`x` 表示可以进入并访问其中文件；`r` 表示可以列出内容。")
q(1, "special-bits",
  "`ls -l /usr/bin/passwd` shows `-rwsr-xr-x root root`. Why the `s`?",
  "`ls -l /usr/bin/passwd` 显示 `-rwsr-xr-x root root`。为什么有 `s`？",
  [("It is a symbolic link.", "它是符号链接。"),
   ("It runs with the owner's (root's) privileges so it can update /etc/shadow.", "它以属主（root）的权限运行，才能更新 /etc/shadow。"),
   ("Only root may delete it (sticky bit).", "只有 root 能删除它（粘滞位）。"),
   ("It is a shared library.", "它是共享库。")],
  1, "`s` in the owner's execute position is setuid: the program runs as the file's owner, not as the caller.",
  "属主执行位上的 `s` 是 setuid：程序以文件属主而不是调用者的身份运行。")
q(1, "logs",
  "You just enabled a service with systemd and want its log messages from the last 10 minutes. Which command?",
  "你刚用 systemd 启用了一个服务，想看它最近 10 分钟的日志。用哪条命令？",
  ["journalctl -u nginx --since '10min ago'", "systemctl log nginx 10", "dmesg -u nginx", "tail -n 10 /etc/nginx"],
  0, "`journalctl -u UNIT --since …` filters the systemd journal; `dmesg` is the kernel log.",
  "`journalctl -u 单元 --since …` 过滤 systemd 日志；`dmesg` 是内核日志。")

# ------------------------------------------------------------------ W2
q(2, "globbing",
  "In an empty directory you run `printf '[%s]\\n' *.txt`. What is printed (bash defaults)?",
  "在空目录中运行 `printf '[%s]\\n' *.txt`，打印什么（bash 默认设置）？",
  ["[]", "[*.txt]", ("nothing", "什么也不打印"), ("an error: no such file", "报错：文件不存在")],
  1, "A glob that matches nothing is passed to the program literally.",
  "没有匹配的通配符会原样传给程序。")
q(2, "param-expansion",
  "`f=photo.2024.jpg`. What does `echo \"${f%.*}\"` print?",
  "`f=photo.2024.jpg`。`echo \"${f%.*}\"` 打印什么？",
  ["photo", "photo.2024", "jpg", "2024.jpg"],
  1, "`%` removes the **shortest** match of `.*` from the end; `%%` would remove the longest (→ `photo`).",
  "`%` 从末尾删去 `.*` 的**最短**匹配；`%%` 删最长匹配（→ `photo`）。")
q(2, "redirection",
  "Which command puts both standard output and standard error of `make` into `build.log`?",
  "哪条命令能把 `make` 的标准输出和标准错误都写进 `build.log`？",
  ["make 2>&1 > build.log", "make > build.log 2>&1", "make 2> build.log", "make | build.log"],
  1, "Redirections are processed left to right: first stdout → file, then stderr → wherever stdout now points. The other order sends stderr to the terminal.",
  "重定向从左到右处理：先把 stdout 指向文件，再让 stderr 指向 stdout 当前所指。反过来写的话 stderr 仍去终端。")
q(2, "filters",
  "`printf 'b\\na\\nb\\nb\\na\\n' | uniq | wc -l` prints?",
  "`printf 'b\\na\\nb\\nb\\na\\n' | uniq | wc -l` 输出什么？",
  ["2", "3", "4", "5"],
  2, "`uniq` only merges adjacent duplicates: b a b(b) a → b a b a = 4 lines. Use `sort | uniq` for distinct values.",
  "`uniq` 只合并相邻的重复行：b a b(b) a → b a b a，共 4 行。要去重得先 `sort` 再 `uniq`。")
q(2, "variables",
  "A script contains `name = \"Ada\"`. What happens when it runs?",
  "脚本里写了 `name = \"Ada\"`。运行时会发生什么？",
  [("`name` is set to Ada.", "`name` 被设为 Ada。"),
   ("The shell tries to run a command called `name` with arguments `=` and `Ada`.", "shell 会尝试运行名为 `name` 的命令，参数是 `=` 和 `Ada`。"),
   ("`name` is set to an empty string.", "`name` 被设为空字符串。"),
   ("It is a comparison that returns true.", "这是一次比较，结果为真。")],
  1, "Assignments must have no spaces around `=`.",
  "赋值语句的 `=` 两边不能有空格。")
q(2, "strict-mode",
  "In a script with only `set -e`, `grep foo missing.txt | wc -l` runs. Why does the script NOT stop?",
  "脚本只设置了 `set -e`，执行 `grep foo missing.txt | wc -l`。为什么脚本没有停下？",
  [("`set -e` ignores grep.", "`set -e` 会忽略 grep。"),
   ("A pipeline's status is the last command's, and `wc` succeeded; `set -o pipefail` would fix it.", "管道的状态取最后一个命令，而 `wc` 成功了；加 `set -o pipefail` 可解决。"),
   ("Pipelines run in the background.", "管道在后台运行。"),
   ("`missing.txt` is created automatically.", "`missing.txt` 会被自动创建。")],
  1, "Without pipefail, only the final command's exit status counts.",
  "没有 pipefail 时，只看最后一个命令的退出状态。")
q(2, "path",
  "Two programs called `tool` exist: `/usr/local/bin/tool` and `/usr/bin/tool`. `PATH=/usr/bin:/usr/local/bin`. Which runs when you type `tool`?",
  "有两个叫 `tool` 的程序：`/usr/local/bin/tool` 和 `/usr/bin/tool`。`PATH=/usr/bin:/usr/local/bin`。输入 `tool` 时运行哪个？",
  ["/usr/bin/tool", "/usr/local/bin/tool", ("both, one after another", "两个依次运行"), ("neither: the name is ambiguous", "都不运行：名字有歧义")],
  0, "The shell searches PATH left to right and runs the first match.",
  "shell 按 PATH 从左到右查找，运行第一个匹配。")

# ------------------------------------------------------------------ W3
q(3, "sed",
  "What does `echo 'grey gray' | sed 's/gr[ae]y/colour/'` print?",
  "`echo 'grey gray' | sed 's/gr[ae]y/colour/'` 打印什么？",
  ["colour colour", "colour gray", "grey colour", "grey gray"],
  1, "Without the `g` flag only the first match on each line is replaced.",
  "没有 `g` 标志时，每行只替换第一个匹配。")
q(3, "regex-groups",
  "Which BRE matches lines that are a word repeated twice with a space, like `bye bye`?",
  "哪个 BRE 能匹配“同一个词重复两次、中间一个空格”的行，如 `bye bye`？",
  ["^\\(.*\\) \\1$", "^(.*) \\1$", "^.* .*$", "^\\(.*\\)\\{2\\}$"],
  0, "`\\( \\)` captures in BRE and `\\1` must repeat exactly the captured text. Option B uses ERE grouping in a BRE; option C allows any two words.",
  "BRE 中用 `\\( \\)` 捕获，`\\1` 必须重复完全相同的文本。B 在 BRE 里用了 ERE 的分组；C 允许任意两个词。")
q(3, "grep",
  "`notes.txt` has 3 lines; one of them contains `todo` twice. What do `grep -c todo notes.txt` and `grep -o todo notes.txt | wc -l` print?",
  "`notes.txt` 有 3 行，其中一行含两次 `todo`。`grep -c todo notes.txt` 和 `grep -o todo notes.txt | wc -l` 分别输出什么？",
  ["1 and 1", "1 and 2", "2 and 2", "2 and 1"],
  1, "`-c` counts matching lines; `-o` prints each match on its own line.",
  "`-c` 统计匹配的行数；`-o` 把每个匹配单独打印一行。")
q(3, "regex",
  "Which task can a regular expression NOT do?",
  "下列哪项是正则表达式做不到的？",
  [("Match lines of exactly 5 characters.", "匹配恰好 5 个字符的行。"),
   ("Match properly nested brackets of any depth.", "匹配任意深度、正确嵌套的括号。"),
   ("Match a word that appears twice in a line.", "匹配一行中出现两次的同一个词。"),
   ("Match 'colour' or 'color'.", "匹配 'colour' 或 'color'。")],
  1, "A regular language has no memory/stack, so it cannot count arbitrary nesting. (Back-references in C go beyond strictly regular languages but grep supports them.)",
  "正则语言没有记忆/栈，无法计数任意深度的嵌套。（C 用到的反向引用其实超出了严格的正则语言，但 grep 支持它。）")
q(3, "awk",
  "`scores.csv` lines look like `alice,72`. Which prints the average of the second column?",
  "`scores.csv` 每行形如 `alice,72`。哪条命令打印第二列的平均值？",
  ["awk -F, '{s+=$2} END {print s/NR}' scores.csv", "awk '{s+=$2} END {print s/NR}' scores.csv",
   "awk -F, '{print avg($2)}' scores.csv", "sed -n 's/.*,//p' scores.csv | awk '{print $1/NR}'"],
  0, "`-F,` sets the separator (without it `$2` is empty), `END` runs after all lines, `NR` = number of records read.",
  "`-F,` 设置分隔符（不设的话 `$2` 为空），`END` 在所有行之后运行，`NR` = 已读记录数。")

# ------------------------------------------------------------------ W4
q(4, "three-states",
  "You edit `a.c` (already tracked) and run `git commit -m fix` without `git add`. What happens?",
  "你修改了已跟踪的 `a.c`，没有 `git add` 就执行 `git commit -m fix`。会怎样？",
  [("The change is committed.", "修改被提交。"),
   ("Nothing is committed: the change is not staged.", "什么也没提交：修改没有暂存。"),
   ("Git deletes the change.", "Git 删除了修改。"),
   ("Git stages and commits it automatically.", "Git 自动暂存并提交。")],
  1, "Only staged changes are committed. `git commit -a` would stage changes to tracked files first.",
  "只有暂存的修改才会被提交。`git commit -a` 会先暂存已跟踪文件的修改。")
q(4, "revert-reset",
  "A bad commit was pushed to a shared `main`. The safest way to undo its effect?",
  "一个错误提交已推送到共享的 `main`。撤销其影响最安全的做法是？",
  ["git reset --hard HEAD~1 && git push --force", "git revert <hash> && git push", "git checkout <hash>", "git restore ."],
  1, "`revert` adds a new commit, so nobody's history is rewritten.",
  "`revert` 新增一个提交，不改写任何人的历史。")
q(4, "git-checkout",
  "After `git checkout 3f2a91c`, `git status` reports `HEAD detached at 3f2a91c`. What does it mean?",
  "执行 `git checkout 3f2a91c` 后，`git status` 显示 `HEAD detached at 3f2a91c`。这说明什么？",
  [("The repository is corrupt.", "仓库损坏了。"),
   ("You are viewing an old commit, not on any branch; `git checkout main` returns.", "你在查看一个旧提交、不在任何分支上；`git checkout main` 可回去。"),
   ("Commit 3f2a91c was deleted.", "提交 3f2a91c 被删除了。"),
   ("You have unstaged changes.", "你有未暂存的修改。")],
  1, "HEAD points directly at a commit instead of a branch name.",
  "HEAD 直接指向一个提交，而不是分支名。")
q(4, "gitignore",
  "Which belongs in a C project's `.gitignore`?",
  "下列哪项应写进 C 项目的 `.gitignore`？",
  ["*.c", "*.o", "Makefile", ".gitignore"],
  1, "Object files are generated by the build; sources, the Makefile and `.gitignore` itself are committed.",
  "目标文件由构建生成；源码、Makefile 和 `.gitignore` 本身都要提交。")
q(4, "pull-push",
  "`git push` is rejected because the remote contains work you don't have. What next?",
  "`git push` 被拒，因为远程有你没有的提交。下一步？",
  ["git push --force", "git pull, resolve any conflicts, then git push", "git commit --amend", "git clone again"],
  1, "Integrate the remote work first (pull = fetch + merge), then push.",
  "先把远程的工作合并进来（pull = fetch + merge），再推送。")

# ------------------------------------------------------------------ W5
q(5, "merge-conflict",
  "A file contains `<<<<<<< HEAD`, `=======`, `>>>>>>> feature`. Which part is the version from `feature`?",
  "某文件中有 `<<<<<<< HEAD`、`=======`、`>>>>>>> feature`。哪一段是来自 `feature` 的版本？",
  [("Between `<<<<<<< HEAD` and `=======`", "`<<<<<<< HEAD` 与 `=======` 之间"),
   ("Between `=======` and `>>>>>>> feature`", "`=======` 与 `>>>>>>> feature` 之间"),
   ("Everything after `>>>>>>> feature`", "`>>>>>>> feature` 之后的所有内容"),
   ("Neither: feature's version is in .git only", "都不是：feature 的版本只在 .git 里")],
  1, "The top half is your current branch (HEAD), the bottom half the branch being merged in.",
  "上半部分是当前分支（HEAD），下半部分是被合并进来的分支。")
q(5, "rebase",
  "During `git rebase main` a conflict appears. After editing the file, you should run:",
  "执行 `git rebase main` 时出现冲突。编辑好文件后应运行：",
  ["git commit -m 'merge'", "git add FILE && git rebase --continue", "git merge --continue", "git push"],
  1, "A rebase replays commits one at a time; you stage the fix and continue (or `--abort` / `--skip`).",
  "rebase 逐个重放提交；暂存修复后继续（或用 `--abort` / `--skip`）。")
q(5, "rebase-vs-merge",
  "Why should you avoid rebasing a branch your teammates have already pulled?",
  "为什么不应 rebase 队友已经拉取过的分支？",
  [("Rebase deletes the files.", "rebase 会删除文件。"),
   ("Rebase gives the replayed commits new IDs, so their copies no longer match and a force push is needed.", "rebase 给重放的提交新 ID，队友的副本对不上，还得强制推送。"),
   ("Rebase only works locally.", "rebase 只能在本地用。"),
   ("Rebase creates a merge commit.", "rebase 会产生合并提交。")],
  1, "Rewriting shared history breaks other people's repositories.",
  "改写共享的历史会搞乱别人的仓库。")
q(5, "fork-pr",
  "You want to fix a typo in a public project where you have no write access. The usual GitHub workflow?",
  "你想修正一个公开项目里的错字，但没有写权限。GitHub 上通常怎么做？",
  [("Ask for the owner's password.", "向所有者要密码。"),
   ("Fork, push the fix to your fork, open a pull request.", "fork，把修改推到自己的 fork，再发 pull request。"),
   ("`git push` to the original; GitHub will queue it.", "直接 `git push` 到原仓库，GitHub 会排队处理。"),
   ("Clone and `git rebase` onto the original.", "clone 后 `git rebase` 到原仓库上。")],
  1, "Forks + pull requests let maintainers review changes from people without write access.",
  "fork + pull request 让维护者审核无写权限者的修改。")
q(5, "interactive-rebase",
  "Your branch has 4 small 'wip' commits you want to combine into one before opening a PR. Which tool?",
  "你的分支有 4 个零碎的 'wip' 提交，想在发 PR 前合成一个。用什么？",
  ["git rebase -i with squash", "git revert", "git cherry-pick", "git reset --hard"],
  0, "Interactive rebase lets you `pick` the first and `squash` the rest.",
  "交互式 rebase 可以 `pick` 第一个，其余 `squash`。")

# ------------------------------------------------------------------ W6
q(6, "tdd",
  "In TDD, what do you do immediately after writing a new test?",
  "在 TDD 中，写完一个新测试后应该立即做什么？",
  [("Refactor the code.", "重构代码。"),
   ("Run the tests and confirm the new one fails.", "运行测试，确认新测试失败。"),
   ("Commit and push.", "提交并推送。"),
   ("Delete old tests that now look redundant.", "删除看起来多余的旧测试。")],
  1, "RED first: a test that passes before you've written the code proves nothing.",
  "先红：在写代码之前就通过的测试什么也证明不了。")
q(6, "assert",
  "A program built with `gcc -DNDEBUG` contains `assert(n > 0);` and `n` is 0. What happens at that line?",
  "用 `gcc -DNDEBUG` 编译的程序中有 `assert(n > 0);`，此时 `n` 为 0。执行到这行会怎样？",
  [("The program aborts with an assertion message.", "程序因断言失败中止并报错。"),
   ("Nothing: the assertion was compiled out.", "什么也不发生：断言已被编译掉。"),
   ("A compile error.", "编译报错。"),
   ("`n` is set to 1.", "`n` 被设为 1。")],
  1, "Defining NDEBUG removes every `assert` at compile time.",
  "定义 NDEBUG 会在编译时移除所有 `assert`。")
q(6, "git-hooks",
  "Your `.git/hooks/pre-commit` script runs the tests and exits with status 1. What happens to `git commit`?",
  "你的 `.git/hooks/pre-commit` 脚本运行测试后以状态 1 退出。`git commit` 会怎样？",
  [("It is aborted.", "被中止。"),
   ("It succeeds with a warning.", "带警告地成功。"),
   ("It is pushed to GitHub.", "被推送到 GitHub。"),
   ("The hook is deleted.", "钩子被删除。")],
  0, "A non-zero exit from pre-commit cancels the commit (`--no-verify` skips the hook).",
  "pre-commit 返回非 0 就取消提交（`--no-verify` 可跳过钩子）。")
q(6, "property-testing",
  "Which is a property test rather than an example test for a `sort` function?",
  "对 `sort` 函数而言，哪一个是属性测试而不是示例测试？",
  [("sort([3,1,2]) == [1,2,3]", "sort([3,1,2]) == [1,2,3]"),
   ("For many random lists, the output is ordered and has the same elements.", "对大量随机列表，输出有序且元素相同。"),
   ("sort([]) == []", "sort([]) == []"),
   ("The function compiles without warnings.", "函数编译时没有警告。")],
  1, "Property testing checks a rule over many generated inputs instead of specific expected outputs.",
  "属性测试在大量生成的输入上检查某条规则，而不是具体的期望输出。")

# ------------------------------------------------------------------ W7
q(7, "strace",
  "`strace ./app` ends with `openat(AT_FDCWD, \"config.ini\", O_RDONLY) = -1 ENOENT` and then `SIGSEGV`. Most likely cause?",
  "`strace ./app` 的结尾是 `openat(AT_FDCWD, \"config.ini\", O_RDONLY) = -1 ENOENT`，随后 `SIGSEGV`。最可能的原因？",
  [("config.ini is read-only.", "config.ini 是只读的。"),
   ("config.ini doesn't exist; the program used the NULL result of fopen without checking.", "config.ini 不存在；程序没检查就使用了 fopen 返回的 NULL。"),
   ("The program ran out of memory.", "程序内存不足。"),
   ("strace caused the crash.", "strace 导致了崩溃。")],
  1, "ENOENT = no such file. fopen returns NULL; using it causes the segfault.",
  "ENOENT = 文件不存在。fopen 返回 NULL；使用它导致段错误。")
q(7, "gdb-break-step",
  "Stopped in gdb on a line that calls `parse(buf)`. You want to go to the next line of the current function without entering `parse`. Command?",
  "gdb 停在调用 `parse(buf)` 的那一行。你想执行到当前函数的下一行，但不进入 `parse`。用哪个命令？",
  ["step", "next", "stepi", "finish"],
  1, "`next` steps over calls; `step` enters them; `stepi` executes one machine instruction.",
  "`next` 跳过函数调用；`step` 会进入；`stepi` 执行一条机器指令。")
q(7, "valgrind",
  "Valgrind reports 64 bytes 'definitely lost'. What does that mean?",
  "Valgrind 报告 64 字节 'definitely lost'。这是什么意思？",
  [("Memory was freed twice.", "内存被释放了两次。"),
   ("Memory was allocated and every pointer to it was lost without freeing it.", "内存分配后，所有指向它的指针都丢了，且从未释放。"),
   ("Memory is still reachable at exit.", "退出时内存仍可访问。"),
   ("The program wrote past the end of an array.", "程序越过数组末尾写入。")],
  1, "'still reachable' = pointer kept but not freed; 'invalid write' = out of bounds.",
  "'still reachable' = 指针还在但没释放；'invalid write' = 越界写。")
q(7, "makefile",
  "Given the rule `%.html: %.md` with recipe `pandoc $< -o $@`, what runs for `make notes.html`?",
  "规则 `%.html: %.md`、配方 `pandoc $< -o $@`，执行 `make notes.html` 会运行什么？",
  ["pandoc notes.html -o notes.md", "pandoc notes.md -o notes.html", "pandoc %.md -o %.html", "pandoc notes -o notes"],
  1, "`$<` is the first prerequisite (notes.md), `$@` the target (notes.html).",
  "`$<` 是第一个依赖（notes.md），`$@` 是目标（notes.html）。")
q(7, "gdb",
  "Which gcc flags make a program easiest to debug in gdb?",
  "哪组 gcc 选项让程序最便于在 gdb 中调试？",
  ["-O3", "-g -O0", "-Wall -Werror", "-DNDEBUG"],
  1, "`-g` adds debug symbols (line numbers, variable names); `-O0` stops the optimiser rearranging code.",
  "`-g` 加入调试符号（行号、变量名）；`-O0` 防止优化器重排代码。")

# ------------------------------------------------------------------ W8
q(8, "acid",
  "A bank transfer debits one account, then the server crashes before crediting the other. Which ACID property should guarantee the debit is undone?",
  "一次转账已从一个账户扣款，服务器在给另一账户入账前崩溃。哪个 ACID 性质保证扣款会被撤销？",
  ["Atomicity", "Consistency", "Isolation", "Durability"],
  0, "Atomic: the whole transaction happens or none of it does.",
  "原子性：整个事务要么全部发生，要么全都不发生。")
q(8, "normal-forms",
  "Orders(*OrderID*, *ProductID*, Quantity, ProductName). ProductName depends only on ProductID. Which normal form is violated?",
  "Orders(*OrderID*, *ProductID*, Quantity, ProductName)。ProductName 只依赖 ProductID。违反了哪个范式？",
  ["1NF", "2NF", "3NF only", ("none", "都不违反")],
  1, "A non-key attribute depending on part of a composite key is a partial dependency → not 2NF.",
  "非键属性只依赖复合键的一部分，属于部分依赖 → 不满足 2NF。")
q(8, "normal-forms",
  "Employee(*EmpID*, DeptID, DeptName): EmpID → DeptID → DeptName. Which form is violated?",
  "Employee(*EmpID*, DeptID, DeptName)：EmpID → DeptID → DeptName。违反了哪个范式？",
  ["1NF", "2NF", "3NF", "6NF only"],
  2, "DeptName depends on the key only through DeptID: a transitive dependency.",
  "DeptName 只是通过 DeptID 依赖主键：传递依赖。")
q(8, "foreign-key",
  "Each student studies one degree; a degree has many students. Where does the foreign key go?",
  "每个学生只读一个专业；一个专业有很多学生。外键放在哪里？",
  [("Degree.student → Student", "Degree.student → Student"),
   ("Student.degree → Degree", "Student.degree → Degree"),
   ("Both tables", "两张表都放"),
   ("A separate join table is required", "必须用单独的连接表")],
  1, "One-to-many: the FK goes on the 'many' side. Join tables are for many-to-many.",
  "一对多：外键放在“多”的一侧。连接表用于多对多。")
q(8, "keys",
  "In `Booking(RoomNo, Date, Guest)` a room can be booked once per date. `(RoomNo, Date)` is:",
  "在 `Booking(RoomNo, Date, Guest)` 中，一个房间每天只能被订一次。`(RoomNo, Date)` 是：",
  [("a surrogate key", "代理键"), ("a composite candidate key", "复合候选键"), ("a foreign key", "外键"), ("not a key", "不是键")],
  1, "It uniquely identifies a row and consists of two attributes.",
  "它能唯一标识一行，并由两个属性组成。")

# ------------------------------------------------------------------ W9
q(9, "having",
  "Which query lists countries with more than 5 customers?",
  "哪条查询列出客户数超过 5 的国家？",
  ["SELECT Country FROM Customer WHERE count(*) > 5 GROUP BY Country;",
   "SELECT Country, count(*) AS n FROM Customer GROUP BY Country HAVING n > 5;",
   "SELECT Country FROM Customer GROUP BY count(*) > 5;",
   "SELECT Country, count(*) FROM Customer HAVING Country > 5;"],
  1, "Conditions on aggregates go in HAVING, after GROUP BY. WHERE can't use count().",
  "对聚合结果的条件写在 GROUP BY 之后的 HAVING 中。WHERE 不能用 count()。")
q(9, "join-types",
  "You want every artist, including those with no albums (shown with NULL). `Artist a ??? Album b ON a.ArtistId = b.ArtistId`:",
  "你想列出所有艺术家，包括没有专辑的（显示为 NULL）。`Artist a ??? Album b ON a.ArtistId = b.ArtistId`：",
  ["INNER JOIN", "LEFT JOIN", "CROSS JOIN", "RIGHT JOIN"],
  1, "LEFT JOIN keeps every row of the left table and fills unmatched right columns with NULL.",
  "LEFT JOIN 保留左表所有行，右表匹配不上的列补 NULL。")
q(9, "where",
  "`SELECT title FROM Film WHERE director = 'Nolan%';` returns:",
  "`SELECT title FROM Film WHERE director = 'Nolan%';` 返回：",
  [("Films whose director's name starts with Nolan.", "导演名以 Nolan 开头的电影。"),
   ("Films whose director is literally 'Nolan%'.", "导演名恰好是 'Nolan%' 的电影。"),
   ("A syntax error.", "语法错误。"),
   ("All films.", "所有电影。")],
  1, "`=` is exact; only `LIKE` treats % as a wildcard.",
  "`=` 是精确比较；只有 `LIKE` 把 % 当通配符。")
q(9, "transactions",
  "What is a transaction?",
  "什么是事务？",
  [("Any SELECT query.", "任何 SELECT 查询。"),
   ("A group of statements that succeed together or are all rolled back.", "一组语句，要么一起成功，要么全部回滚。"),
   ("A query sent from another programming language.", "从其它编程语言发出的查询。"),
   ("A backup of the database.", "数据库备份。")],
  1, "BEGIN TRANSACTION … END/COMMIT: all-or-nothing.",
  "BEGIN TRANSACTION … END/COMMIT：全有或全无。")
q(9, "aggregate",
  "`SELECT count(Company) FROM Customer;` when 40 of 59 customers have a NULL Company returns:",
  "59 个客户中有 40 个 Company 为 NULL，`SELECT count(Company) FROM Customer;` 返回：",
  ["59", "40", "19", "NULL"],
  2, "count(column) skips NULLs; count(*) counts rows.",
  "count(列) 会跳过 NULL；count(*) 统计行数。")

# ------------------------------------------------------------------ W10
q(10, "sql-injection",
  "A login builds `SELECT * FROM users WHERE name='` + input + `'`. Which input logs in without a valid name?",
  "登录功能拼接 `SELECT * FROM users WHERE name='` + 输入 + `'`。哪个输入能在没有有效用户名的情况下登录？",
  ["admin", "' OR '1'='1", "%", "NULL"],
  1, "The quote closes the string and `OR '1'='1'` makes the condition always true. Fix: prepared statements.",
  "引号闭合了字符串，`OR '1'='1'` 让条件恒为真。修复：预编译语句。")
q(10, "horn-clauses",
  "With `ok(X) :- a(X), b(X).` and `ok(X) :- c(X).` and facts `a(p). b(q). c(r).`, what does `ok(X)` return?",
  "有规则 `ok(X) :- a(X), b(X).` 和 `ok(X) :- c(X).`，事实 `a(p). b(q). c(r).`，查询 `ok(X)` 返回什么？",
  ["p, q, r", "r", "p, r", ("nothing", "无结果")],
  1, "Comma = AND (needs the same X in a and b: none); two rules = OR → only r.",
  "逗号 = 且（同一个 X 要同时满足 a 和 b：没有）；两条规则 = 或 → 只有 r。")
q(10, "datalog-recursion",
  "Facts: `edge(a,b). edge(b,c). edge(c,d).` Rules: `path(X,Y) :- edge(X,Y).` `path(X,Z) :- edge(X,Y), path(Y,Z).` How many answers does `path(a,X)` have?",
  "事实：`edge(a,b). edge(b,c). edge(c,d).` 规则：`path(X,Y) :- edge(X,Y).` `path(X,Z) :- edge(X,Y), path(Y,Z).` 查询 `path(a,X)` 有几个答案？",
  ["1", "2", "3", "4"],
  2, "a reaches b, c and d.",
  "a 可以到达 b、c、d。")
q(10, "datalog-syntax",
  "In Datalog, which of these is a variable?",
  "在 Datalog 中，下列哪个是变量？",
  ["socrates", "'Socrates'", "Socrates", "42"],
  2, "Variables start with an upper-case letter or `_`; quoted and lower-case names are atoms.",
  "变量以大写字母或 `_` 开头；带引号和小写开头的是原子。")
q(10, "mac-models",
  "Under Bell–LaPadula, a user cleared for `secret` may:",
  "在 Bell–LaPadula 模型下，许可级别为 `secret` 的用户可以：",
  [("read topsecret files", "读 topsecret 文件"),
   ("write unclassified files", "写 unclassified 文件"),
   ("read unclassified files and write topsecret files", "读 unclassified 文件并写 topsecret 文件"),
   ("only access secret files", "只能访问 secret 文件")],
  2, "No read up, no write down: read at or below your level, write at or above it.",
  "不上读、不下写：可读等于或低于自己级别的文件，可写等于或高于自己级别的文件。")
q(10, "prepared-statements",
  "Why do prepared statements stop SQL injection?",
  "预编译语句为什么能阻止 SQL 注入？",
  [("They encrypt the query.", "它们加密了查询。"),
   ("The SQL is parsed first and user input is bound only as data, never as SQL.", "SQL 先被解析，用户输入只作为数据绑定，绝不当作 SQL。"),
   ("They remove all quotes from input.", "它们删除输入里的所有引号。"),
   ("They only allow numbers.", "它们只允许数字。")],
  1, "`?` placeholders + bind: the input can't change the query's structure.",
  "`?` 占位符 + 绑定：输入无法改变查询的结构。")
