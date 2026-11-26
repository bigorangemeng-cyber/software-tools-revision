"""Lab section: one page per week's lab. Each part may carry a solution,
which is rendered inside a collapsed <details> ("try first, then open")."""

LABS = {}
_cur = {"n": None}

# concepts whose content comes (mainly) from the labs -> get a 🧪 badge
LAB_CONCEPTS = {
    "ssh-keys", "ssh-key-perms", "scp", "ssh-config", "vagrant", "editors", "package-manager",
    "word-splitting", "globbing", "quoting", "variables", "filters", "redirection",
    "permissions-lab", "path-permission", "setuid-demo", "sudoers", "b-script", "strict-mode",
    "grep", "sed", "git-config", "gitignore", "git-restore", "git-checkout", "revert-reset",
    "branch", "merge", "https-vs-ssh", "remote", "pull-push", "merge-conflict", "shared-access",
    "feature-branches", "fork-pr", "patches", "force-push", "reflog", "pull-rebase",
    "unity", "tdd", "git-hooks", "github-actions", "crackme", "makefile", "gdb-inspect",
    "er-diagram", "create-table", "insert", "select-order", "subquery",
    "horn-clauses", "datalog-negation", "datalog-access-control", "mac-models",
}


def lab(n, en, zh, files, goal_en, goal_zh, exam_en="", exam_zh="", pit_en="", pit_zh=""):
    LABS[n] = dict(n=n, en=en, zh=zh, files=files, goal_en=goal_en, goal_zh=goal_zh,
                   exam_en=exam_en, exam_zh=exam_zh, pit_en=pit_en, pit_zh=pit_zh, parts=[])
    _cur["n"] = n


def part(pid, t_en, t_zh, en="", zh="", code="", sol_en="", sol_zh="", sol_code="", see=()):
    LABS[_cur["n"]]["parts"].append(dict(id=pid, t_en=t_en, t_zh=t_zh, en=en, zh=zh, code=code,
                                         sol_en=sol_en, sol_zh=sol_zh, sol_code=sol_code, see=list(see)))


# ======================================================================  L1
lab(1, "Welcome to the labs: SSH, Vagrant, Debian", "实验 1：SSH、Vagrant 与 Debian 管理",
    ["01-sysadmin/lab/lab.md", "01-sysadmin/lab/Vagrantfile"],
    "Log in to the lab machines with SSH keys, run your own Debian VM with Vagrant, and do basic system administration (filesystem, packages, editors).",
    "用 SSH 密钥登录实验室机器，用 Vagrant 运行自己的 Debian 虚拟机，并完成基础系统管理（文件系统、软件包、编辑器）。",
    exam_en=r"""
- Key-based login needs the public key **inside** `~/.ssh/authorized_keys` on the server; copying `id_ed25519.pub` there is not enough (official example paper Q1).
- `apt update` refreshes the package list; `apt upgrade` installs newer versions (example paper Q2).
- `scp demo.c user@host:~/code/` — local path first, `user@host:` then the remote path (example paper Q3).
- Private key `600`, public key `644`, `authorized_keys` `600`.
""",
    exam_zh=r"""
- 密钥登录要求公钥**写进**服务器的 `~/.ssh/authorized_keys`；只把 `id_ed25519.pub` 拷过去不够（官方样卷第 1 题）。
- `apt update` 刷新软件包列表；`apt upgrade` 安装新版本（样卷第 2 题）。
- `scp demo.c user@host:~/code/`——先写本地路径，再写 `user@host:` 和远程路径（样卷第 3 题）。
- 私钥 `600`，公钥 `644`，`authorized_keys` `600`。
""",
    pit_en=r"""
- Answering `y` to "Overwrite?" in `ssh-keygen` destroys a key you already use elsewhere.
- Uploading the **private** key instead of the public one.
- `authorized_keys` created with default permissions → SSH ignores it; fix with `chmod 600`.
- On lab machines VMs live in `/tmp`: anything in the VM's home directory disappears; work in `/shared`.
- Two hypervisors at once (e.g. Hyper-V and VirtualBox) → Vagrant crashes.
""",
    pit_zh=r"""
- `ssh-keygen` 问 “Overwrite?” 时回答 `y`，会毁掉你在别处正在用的密钥。
- 上传的是**私钥**而不是公钥。
- `authorized_keys` 用默认权限创建 → SSH 不认；用 `chmod 600` 修复。
- 实验室机器上虚拟机放在 `/tmp`：虚拟机家目录里的东西会丢失；文件放 `/shared`。
- 同时运行两种虚拟化软件（如 Hyper-V 和 VirtualBox）→ Vagrant 崩溃。
""")
part("l1-client", "Check your SSH client", "检查 SSH 客户端",
     en=r"""
Run `ssh localhost` and interpret the result:
| Result | Means |
|---|---|
| asks for a password | client works and an SSH server runs locally (Ctrl+C) |
| logs straight in | client + server work; no password or key already set (type `exit`) |
| `connection refused` | client works, no local server — fine, the server is the lab machine |
| `ssh: command not found` | no OpenSSH (Windows CMD) → use WSL |
""",
     zh=r"""
运行 `ssh localhost` 并判断结果：
| 结果 | 含义 |
|---|---|
| 要求输入密码 | 客户端正常，本机运行着 SSH 服务端（Ctrl+C 取消） |
| 直接登录 | 客户端和服务端都正常；没有密码或已配好密钥（输入 `exit`） |
| `connection refused` | 客户端正常，本机没有服务端——没关系，服务端是实验室机器 |
| `ssh: command not found` | 没装 OpenSSH（Windows CMD）→ 改用 WSL |
""", see=["ssh"])
part("l1-connect", "Connect to a lab machine", "连接实验室机器",
     en=r"""
- Needs eduroam or the university VPN. `ssh USERNAME@rd-mvb-linuxlab.bristol.ac.uk` (load balancer → a random `it######` machine).
- First time: answer `yes` to the host-key question. Then `whoami`, `uname -a`, `hostname`; `exit` to leave.
""",
     zh=r"""
- 需要连 eduroam 或学校 VPN。`ssh 用户名@rd-mvb-linuxlab.bristol.ac.uk`（负载均衡 → 随机分配一台 `it######` 机器）。
- 第一次连接对主机密钥问题回答 `yes`。然后试 `whoami`、`uname -a`、`hostname`；`exit` 退出。
""", see=["ssh", "host-key"])
part("l1-keys", "Set up key-based login", "配置密钥登录",
     en=r"""
Generate a key pair on **your own** machine, copy the public key to the lab, append it to `authorized_keys`, fix permissions, log in again without a password. Debug with `ssh -v`.
""",
     zh=r"""
在**自己的**机器上生成密钥对，把公钥拷到实验室机器，追加进 `authorized_keys`，修正权限，再次登录就不需要密码了。出问题用 `ssh -v` 调试。
""",
     code=r"""
ssh-keygen -t ed25519                 # Enter = default path, empty passphrase
ls -l ~/.ssh                          # -rw------- id_ed25519 / -rw-r--r-- id_ed25519.pub
ssh USER@rd-mvb-linuxlab.bristol.ac.uk 'mkdir -p ~/.ssh'
scp ~/.ssh/id_ed25519.pub USER@rd-mvb-linuxlab.bristol.ac.uk:~/.ssh/
ssh USER@rd-mvb-linuxlab.bristol.ac.uk
cd .ssh && cat id_ed25519.pub >> authorized_keys && chmod 600 authorized_keys
exit
ssh USER@rd-mvb-linuxlab.bristol.ac.uk  # no password now
""",
     sol_en="Why `>>` and not `cp`? `cp` (or `>`) would overwrite an existing `authorized_keys` and lock out keys already there; `>>` appends one line per key.",
     sol_zh="为什么用 `>>` 而不是 `cp`？`cp`（或 `>`）会覆盖已有的 `authorized_keys`，把原来的密钥都删掉；`>>` 是每个密钥追加一行。",
     see=["ssh-keys", "ssh-key-perms", "scp", "redirection"])
part("l1-config", "SSH config file", "SSH 配置文件",
     en=r"Create `~/.ssh/config` so `ssh lab` is enough. Use `IdentityFile` / `-i` for a different key per service.",
     zh=r"创建 `~/.ssh/config`，之后只需 `ssh lab`。不同服务用不同密钥时用 `IdentityFile` 或 `-i`。",
     code=r"""
Host lab
  HostName rd-mvb-linuxlab.bristol.ac.uk
  User USERNAME
""", see=["ssh-config"])
part("l1-vagrant", "Vagrant: your own Debian VM", "Vagrant：自己的 Debian 虚拟机",
     en=r"""
- Install Vagrant + VirtualBox, reboot. Empty folder + `Vagrantfile` → `vagrant up` → `vagrant ssh` (password `vagrant` if asked) → `ls /` shows `shared`.
- Leave with `exit`, stop with `vagrant halt` (always before shutting down). `vagrant destroy` + `vagrant up` rebuilds from scratch — use this to test your provision block.
- On a lab machine: `mkdir softwaretools; cd softwaretools; wget …/Vagrantfile; vagrant up`.
""",
     zh=r"""
- 安装 Vagrant + VirtualBox 并重启。新建空目录 + `Vagrantfile` → `vagrant up` → `vagrant ssh`（要密码就输 `vagrant`）→ `ls /` 能看到 `shared`。
- `exit` 退出虚拟机，`vagrant halt` 关机（关电脑前一定要做）。`vagrant destroy` + `vagrant up` 从头重建——用来测试 provision 配置。
- 在实验室机器上：`mkdir softwaretools; cd softwaretools; wget …/Vagrantfile; vagrant up`。
""", see=["vagrant"])
part("l1-admin", "Debian administration", "Debian 系统管理",
     en=r"""
- Explore the tree: `ls /bin`, `which ls`, `ls -l /bin` (first char `l` = symlink), `cat /etc/apt/sources.list`.
- Editors: `nano`, `vim` installed; `sudo apt install emacs-nox` (not `emacs`: would pull a GUI); try `mc` (mcedit), `tilde`, `micro`; `apt info PKG`; remove the ones you don't like with `sudo apt remove`.
- Keep your favourites in the Vagrantfile provision block, then `vagrant destroy` / `up` and check they are installed.
""",
     zh=r"""
- 浏览目录树：`ls /bin`、`which ls`、`ls -l /bin`（首字符 `l` = 符号链接）、`cat /etc/apt/sources.list`。
- 编辑器：已装 `nano`、`vim`；`sudo apt install emacs-nox`（别装 `emacs`，会带上整套图形界面）；可试 `mc`（mcedit）、`tilde`、`micro`；`apt info 包名`；不喜欢的用 `sudo apt remove` 删掉。
- 把常用软件写进 Vagrantfile 的 provision 块，然后 `vagrant destroy` / `up` 检查是否自动装好。
""", see=["fhs", "package-manager", "editors"])

# ======================================================================  L2
lab(2, "Shell stuff: expansion, permissions, scripts, pipes", "实验 2：Shell 展开、权限、脚本与管道",
    ["02-fundamentals/lab/lab.md"],
    "See exactly how the shell turns a line into arguments, practise users/groups/permissions/setuid/sudo, write a POSIX build script, and solve problems with pipes and redirection.",
    "亲眼看 shell 如何把一行字变成参数，练习用户/组/权限/setuid/sudo，写一个 POSIX 构建脚本，并用管道和重定向解决问题。",
    exam_en=r"""
- `head -n 6 f | uniq | wc -l`: `uniq` only removes **adjacent** duplicates (example paper Q4).
- `cmd > log.txt 2>&1` sends both streams to the file; `cmd 2>&1 > log.txt` does not (example paper Q5).
- `for file in *; do echo "${file%.*}"; done` prints names without extensions; `for $file in …` is a syntax error (example paper Q6).
- Permissions need `x` on every directory of the path; setuid shows as `s` in the owner's x position.
""",
    exam_zh=r"""
- `head -n 6 f | uniq | wc -l`：`uniq` 只去掉**相邻**的重复行（样卷第 4 题）。
- `cmd > log.txt 2>&1` 把两个流都写进文件；`cmd 2>&1 > log.txt` 不行（样卷第 5 题）。
- `for file in *; do echo "${file%.*}"; done` 打印去掉扩展名的文件名；`for $file in …` 是语法错误（样卷第 6 题）。
- 访问需要路径上每级目录的 `x`；setuid 显示为属主 x 位置上的 `s`。
""",
    pit_en=r"""
- `x = 5` (spaces) runs a command called `x`. Write `x=5`.
- Unquoted `$file` breaks on names with spaces; always `"$file"`.
- `usermod -G` without `-a` **replaces** all secondary groups.
- Editing `/etc/sudoers` directly can lock you out of sudo — always `visudo`, with a root shell open.
- After `sudo reboot` the `/shared` folder may be missing → `vagrant halt` then `vagrant up`.
""",
    pit_zh=r"""
- `x = 5`（带空格）会去执行一个叫 `x` 的命令。要写 `x=5`。
- 不加引号的 `$file` 遇到带空格的文件名就出错；一律写 `"$file"`。
- `usermod -G` 不加 `-a` 会**替换**掉全部附加组。
- 直接编辑 `/etc/sudoers` 可能让 sudo 失效——一定用 `visudo`，并保持一个 root shell 开着。
- `sudo reboot` 后 `/shared` 可能不见了 → `vagrant halt` 再 `vagrant up`。
""")
part("l2-args", "Whitespace, globs and quoting with arguments.c", "用 arguments.c 观察空白、通配与引号",
     en=r"""
Compile `gcc -Wall arguments.c -o arguments`, then compare `./arguments one       two`, `./arguments "one two"`, `./arguments "one      two"`, `./arguments *`, and `../arguments *` inside an empty folder.
- Task: three ways to make it print exactly `Argument #1: [*]`.
- Task: make it print `Argument #1: [Hello world!]`.
""",
     zh=r"""
编译 `gcc -Wall arguments.c -o arguments`，然后对比 `./arguments one       two`、`./arguments "one two"`、`./arguments "one      two"`、`./arguments *`，以及在空目录里运行 `../arguments *`。
- 任务：用三种方法让它恰好打印 `Argument #1: [*]`。
- 任务：让它打印 `Argument #1: [Hello world!]`。
""",
     sol_en=r"""
- Unquoted whitespace separates arguments and runs of spaces collapse; quotes keep spaces exactly.
- `*` expands to the file names; in an empty folder it matches nothing and is passed **literally**.
- Literal star: `./arguments '*'`, `./arguments "*"`, `./arguments \*`.
- `./arguments 'Hello world!'` (single quotes also stop bash's `!` history expansion) or `./arguments Hello\ world!`.
- File with spaces: `touch "silly named file"`; without quotes you get three files. Delete with `rm "silly named file"`, `rm silly\ named\ file` or Tab completion.
""",
     sol_zh=r"""
- 未加引号的空白分隔参数，连续空格合并；引号原样保留空格。
- `*` 展开成文件名；空目录里没有匹配，于是**原样**传入 `*`。
- 字面星号：`./arguments '*'`、`./arguments "*"`、`./arguments \*`。
- `./arguments 'Hello world!'`（单引号还能阻止 bash 对 `!` 做历史展开），或 `./arguments Hello\ world!`。
- 带空格的文件：`touch "silly named file"`；不加引号会建出三个文件。删除：`rm "silly named file"`、`rm silly\ named\ file` 或用 Tab 补全。
""", see=["shell-expansion", "word-splitting", "globbing", "quoting"])
part("l2-vars", "Shell variables", "Shell 变量",
     en=r"`p=arguments; gcc -Wall $p.c -o $p`. What goes wrong with `program=\"silly name\"` unquoted, with `program=silly name`, and with `file=arguments gcc -Wall \"$file.c\" -o \"$file\"`?",
     zh=r"`p=arguments; gcc -Wall $p.c -o $p`。不加引号使用 `program=\"silly name\"`、写成 `program=silly name`、以及 `file=arguments gcc -Wall \"$file.c\" -o \"$file\"`，分别会出什么问题？",
     sol_en=r"""
- Unquoted `$program.c` splits into `silly` and `name.c` → gcc gets three inputs. Use `"$program.c"`.
- `program=silly name` sets `program=silly` and then **runs** `name`.
- In `file=arguments gcc … "$file.c"` the shell expands `$file` (still empty) **before** the temporary assignment takes effect → `gcc -Wall .c -o`.
""",
     sol_zh=r"""
- 不加引号的 `$program.c` 被拆成 `silly` 和 `name.c` → gcc 收到三个输入。要写 `"$program.c"`。
- `program=silly name` 先设 `program=silly`，然后**运行** `name`。
- `file=arguments gcc … "$file.c"` 中，shell 在临时赋值生效**之前**就把 `$file`（此时为空）展开了 → 变成 `gcc -Wall .c -o`。
""", see=["variables"])
part("l2-perms", "Users, groups and a shared home", "用户、组与共享家目录",
     en=r"""
Create `brian` and `nigel`, add both (not `vagrant`) to group `users`. As brian: home dir readable/enterable by `users` but not writable, nothing for others; a `private` folder only for brian with `secret.txt` inside.
""",
     zh=r"""
创建 `brian` 和 `nigel`，把两人（不含 `vagrant`）加入 `users` 组。以 brian 身份：家目录 `users` 组可读可进入、不可写，其他人无权限；建一个只有 brian 能访问的 `private` 目录，里面放 `secret.txt`。
""",
     code=r"""
sudo adduser brian; sudo adduser nigel
sudo usermod -aG users brian; sudo usermod -aG users nigel
tail /etc/passwd; tail /etc/group
su brian
chgrp -R users ~        # group of home dir = users
chmod 750 ~             # rwx r-x ---
nano ~/readme.txt
mkdir ~/private && chmod 700 ~/private
nano ~/private/secret.txt
""",
     sol_en=r"""
- nigel can list brian's home and read `readme.txt` but cannot create files or edit it; vagrant gets "Permission denied" (but can `sudo` around everything).
- nigel sees the name `private` but can't `cd` into it or read `secret.txt` even knowing the full path — `x` is needed on every directory along the path.
- `readme.txt` and `secret.txt` show different groups because `chgrp -R` ran before `secret.txt` existed; new files take brian's primary group.
""",
     sol_zh=r"""
- nigel 能列出 brian 的家目录并读 `readme.txt`，但不能新建文件或修改它；vagrant 得到 “Permission denied”（但可以用 `sudo` 绕过一切）。
- nigel 能看到 `private` 这个名字，但不能 `cd` 进去，即使知道完整路径也读不了 `secret.txt`——路径上每级目录都需要 `x`。
- `readme.txt` 和 `secret.txt` 的属组不同，因为 `chgrp -R` 执行时 `secret.txt` 还不存在；新文件取 brian 的主组。
""", see=["permissions-lab", "path-permission", "unix-dac"])
part("l2-setuid", "setuid and sudo", "setuid 与 sudo",
     en=r"""
- brian compiles `message-brian.c`, `chmod u+s message-brian` → `-rwsr-xr-x`; nigel runs it → `messages.txt` written as brian.
- `sudo find / -perm /4000` → `sudo`, `su`, `mount`, `umount`, `passwd`. Why is `passwd` setuid? It must write `/etc/shadow`, owned by root.
- brian `sudo ls` → "not in the sudoers file". As root (`sudo su`), `visudo`, add `%users ALL=(ALL) /sbin/reboot` → brian can `sudo reboot`.
""",
     zh=r"""
- brian 编译 `message-brian.c`，`chmod u+s message-brian` → `-rwsr-xr-x`；nigel 运行它 → `messages.txt` 以 brian 的身份写入。
- `sudo find / -perm /4000` → `sudo`、`su`、`mount`、`umount`、`passwd`。`passwd` 为什么是 setuid？它要写 root 拥有的 `/etc/shadow`。
- brian 执行 `sudo ls` → “not in the sudoers file”。以 root（`sudo su`）运行 `visudo`，加入 `%users ALL=(ALL) /sbin/reboot` → brian 可以 `sudo reboot`。
""", see=["setuid-demo", "special-bits", "sudoers"])
part("l2-b", "The build helper ./b", "构建助手 ./b",
     en=r"Write a POSIX `sh` script `b`: `compile NAME`, `run NAME`, `build NAME`; accept `x` or `x.c`; errors → message + non-zero exit; no/unknown command → usage.",
     zh=r"写一个 POSIX `sh` 脚本 `b`：支持 `compile NAME`、`run NAME`、`build NAME`；接受 `x` 或 `x.c`；出错 → 打印信息并以非 0 退出；无命令或未知命令 → 打印用法。",
     sol_en="A reference solution is on the concept card [[b-script]]. Key ideas: `${2%.c}` strips `.c`; `[ -f \"$name.c\" ]` checks the source; `compile && run` only runs after a successful compile; errors go to stderr with `>&2`.",
     sol_zh="参考解法见知识点卡片[[b-script]]。关键点：`${2%.c}` 去掉 `.c`；`[ -f \"$name.c\" ]` 检查源文件；`compile && run` 只在编译成功后运行；错误用 `>&2` 写到 stderr。",
     see=["b-script", "param-expansion"])
part("l2-strict", "Strict mode and pipefail", "严格模式与 pipefail",
     en=r"Think of a pipeline where the last command succeeds even though an earlier one failed.",
     zh=r"想一个管道例子：前面的命令失败了，最后一个命令却成功了。",
     sol_en=r"`grep pattern missing.txt | sort` or `cat nofile | wc -l` (prints 0): `sort`/`wc` succeed, so the pipeline returns 0. With `set -o pipefail` it returns grep's/cat's failure. Counter-example from the sheet: `cat FILE | grep STRING` already fails if grep finds nothing.",
     sol_zh=r"`grep pattern missing.txt | sort` 或 `cat nofile | wc -l`（打印 0）：`sort`/`wc` 成功，于是整个管道返回 0。加 `set -o pipefail` 后返回 grep/cat 的失败。讲义里的反例：`cat FILE | grep STRING` 在 grep 没找到时本来就会失败。",
     see=["strict-mode"])
part("l2-words", "Word list exercises (pipes)", "单词表练习（管道）",
     en=r"Using `/usr/share/dict/words`: first word, last word, number of words, the 6171st word, the first five of the last 100, the last ten in reverse order.",
     zh=r"用 `/usr/share/dict/words`：第一个词、最后一个词、单词总数、第 6171 个词、最后 100 个里的前 5 个、最后 10 个倒序。",
     sol_code=r"""
head -n 1 /usr/share/dict/words
tail -n 1 /usr/share/dict/words
wc -l < /usr/share/dict/words
head -n 6171 /usr/share/dict/words | tail -n 1
tail -n 100 /usr/share/dict/words | head -n 5
tail -n 10 /usr/share/dict/words | sort -r
""", see=["filters", "pipes"])
part("l2-redir", "Redirection and diff", "重定向与 diff",
     en=r"Save `ls -l` to `tmp`; compare it with a fresh `ls -l`; save the diff to `difflog`, then run it again appending.",
     zh=r"把 `ls -l` 存进 `tmp`；与当前的 `ls -l` 比较；把 diff 结果存进 `difflog`，再运行一次并追加。",
     sol_code=r"""
ls -l > tmp
ls -l | diff tmp -        # or: diff tmp <(ls -l)
ls -l | diff tmp - > difflog
ls -l | diff tmp - >> difflog
""",
     sol_en="The difference: `tmp` itself appears in the new listing (and the total changes). After creating `difflog` the second diff also shows `difflog` as a new line.",
     sol_zh="差别在于：新列表里多了 `tmp` 本身（总计也变了）。创建 `difflog` 之后，第二次 diff 还会多出 `difflog` 这一行。",
     see=["redirection"])

# ======================================================================  L3
lab(3, "Regular expressions: grep and sed", "实验 3：正则表达式（grep 与 sed）",
    ["03-regex/lab/README.md", "03-regex/lab/solutions.org"],
    "Search the dictionary with grep, rewrite text with sed, and learn the less obvious grep options.",
    "用 grep 搜索单词表，用 sed 改写文本，并掌握 grep 不那么常用的选项。",
    exam_en=r"""
- `[ft]` means "f **or** t", not "ft" (example paper Q7).
- `colou\?r` matches colour and color; `colo[ou]r` does **not** match color (example paper Q8).
- Regular expressions cannot count/match "n a's then n b's" — no memory (example paper Q9).
- Count letters with `grep -o 'a' file | wc -l`, not `grep -c` (example paper Q10).
""",
    exam_zh=r"""
- `[ft]` 表示 “f **或** t”，不是 “ft”（样卷第 7 题）。
- `colou\?r` 匹配 colour 和 color；`colo[ou]r` **不**匹配 color（样卷第 8 题）。
- 正则无法匹配 “n 个 a 接 n 个 b”——它没有记忆（样卷第 9 题）。
- 统计字母出现次数用 `grep -o 'a' file | wc -l`，不能用 `grep -c`（样卷第 10 题）。
""",
    pit_en=r"""
- Forgetting quotes: the shell eats `$`, `*`, `\` before grep sees them.
- BRE vs ERE: `+ ? { } ( )` need backslashes in plain grep/sed, not in `-E`.
- `a*` matches zero a's too, so "at least four a's" needs `a.*a.*a.*a` or `\(.*a\)\{4,\}`.
""",
    pit_zh=r"""
- 忘了加引号：`$`、`*`、`\` 在 grep 看到之前就被 shell 处理掉了。
- BRE 与 ERE：普通 grep/sed 里 `+ ? { } ( )` 要加反斜杠，`-E` 里不用。
- `a*` 也匹配 0 个 a，所以“至少 4 个 a”要写 `a.*a.*a.*a` 或 `\(.*a\)\{4,\}`。
""")
part("l3-grep", "Grepping the dictionary", "在单词表中 grep",
     en=r"Q (capitalised); start with r/R; end in j; count of q any case; first five with 'cl'; 'kp' but not 'ckp'; last 15 two-letter words; three-letter words with no vowels; 7 letters, 3rd 'e', ending 'ded'; start with p/P with ≥4 a's.",
     zh=r"含大写 Q；以 r/R 开头；以 j 结尾；忽略大小写含 q 的个数；含 'cl' 的前 5 个；含 'kp' 但不含 'ckp'；最后 15 个两字母词；不含元音的三字母词；7 个字母、第 3 个是 e、以 ded 结尾；以 p/P 开头且至少 4 个 a。",
     sol_code=r"""
grep 'Q' words
grep '^[rR]' words                # or: grep -i '^r'
grep 'j$' words
grep -ci 'q' words
grep 'cl' words | head -n 5
grep '[^c]kp' words
grep '^..$' words | tail -n 15
grep '^[^aeiou]\{3\}$' words      # course key also excludes y: [^aoeuiy]
grep '^..e.ded$' words
grep -i '^p\(.*a\)\{4,\}' words   # or: grep -i '^p.*a.*a.*a.*a'
""", see=["grep", "bracket-expr", "regex-quantifiers", "regex-groups"])
part("l3-sed", "Sed exercises", "sed 练习",
     en=r"day→week on words ending 'ay'; words starting with s → 'sway'; duplicate 'day' after a space; 'Xday' → 'Xday or Xweek'; flip 'someday' → 'day (some)'; what does `g` do?",
     zh=r"对以 ay 结尾的词把 day 改成 week；以 s 开头的词改成 'sway'；在含 day 的行后面再重复一个 day；'Xday' → 'Xday or Xweek'；把 'someday' 翻成 'day (some)'；`g` 的作用是什么？",
     sol_code=r"""
grep 'ay$' words | sed 's/day/week/'
grep 'ay$' words | sed 's/^s.*/sway/'
sed 's/.*day.*/& day/' words
sed 's/^\(.*\)day$/\1day or \1week/' words
sed 's/^\(.*\)\([dw]ay\)$/\2 (\1)/' words
echo banana | sed 's/a/e/'    # benana   (first match only)
echo banana | sed 's/a/e/g'   # benene   (every match on the line)
""", see=["sed", "regex-groups"])
part("l3-more", "More grep: -w, -o vs -c, spellings, postcodes", "更多 grep：-w、-o 与 -c、拼写、邮编",
     en=r"""
1. A file where `grep PATTERN` returns two lines but `grep -w PATTERN` one.
2. When do `grep -o P f | wc -l` and `grep -c P f` differ?
3. Match encyclopaedia/encyclopedia (and nothing else); color/colour.
4. UK postcode schema: two letters, one digit, optional space, digit, two letters.
5. Find a postcode the long official regex accepts but the simple schema rejects.
""",
     zh=r"""
1. 构造一个文件，使 `grep PATTERN` 返回两行而 `grep -w PATTERN` 只返回一行。
2. `grep -o P f | wc -l` 和 `grep -c P f` 什么时候结果不同？
3. 只匹配 encyclopaedia/encyclopedia；color/colour。
4. 英国邮编简化规则：两个字母、一个数字、可选空格、一个数字、两个字母。
5. 找一个长版官方正则接受、但简化规则不接受的邮编。
""",
     sol_code=r"""
printf 'cat\ncatalogue\n' > f.txt
grep cat f.txt        # cat, catalogue
grep -w cat f.txt     # cat   (-w = whole word)

echo banana | grep -c a          # 1  (counts LINES)
echo banana | grep -o a | wc -l  # 3  (counts MATCHES)

grep -x 'encyclopa\?edia' words  # -x = whole line must match
grep -x 'colou\?r' words

grep '^[A-Z]\{2\}[0-9] \?[0-9][A-Z]\{2\}$' postcodes.txt   # e.g. BS8 1UB
""",
     sol_en="5: e.g. `M1 1AE` (one letter), `SW1A 1AA` (letter after the digit), `GIR 0AA`, `BFPO 123` — all valid in the full regex, rejected by the two-letters-one-digit schema.",
     sol_zh="第 5 题：如 `M1 1AE`（只有一个字母）、`SW1A 1AA`（数字后还有字母）、`GIR 0AA`、`BFPO 123`——完整正则都接受，简化规则都拒绝。",
     see=["grep", "regex-quantifiers"])

# ======================================================================  L4
lab(4, "Git on your own, then with GitHub", "实验 4：单机 Git 与 GitHub",
    ["04-git/lab/standalone.md", "04-git/lab/github.md"],
    "Practise the commit loop, ignoring files, comparing and undoing with history, branching and merging, then connect a repository to GitHub over SSH.",
    "练习提交循环、忽略文件、用历史比较与撤销、分支与合并，然后通过 SSH 把仓库连到 GitHub。",
    exam_en=r"""
- `git add` = **stage** (example paper Q11). A branch = a reference to a sequence of commits (Q12). Git was written by Linus Torvalds (Q13).
- `git pull` = `git fetch` then `git merge` (Q14).
- "Your branch and 'origin/main' have diverged, 7 and 42 commits": you made 7 local commits, the remote got 42 you don't have (Q15).
""",
    exam_zh=r"""
- `git add` = **暂存**（样卷第 11 题）。分支 = 指向一串提交的引用（第 12 题）。Git 由 Linus Torvalds 编写（第 13 题）。
- `git pull` = `git fetch` 再 `git merge`（第 14 题）。
- “Your branch and 'origin/main' have diverged, 7 and 42 commits”：你本地有 7 个提交，远程有 42 个你没有的提交（第 15 题）。
""",
    pit_en=r"""
- Committing build outputs (`program`, `*.o`) — add them to `.gitignore`.
- Forgetting that `git commit -a` does not add **new** files.
- `git checkout HASH` leaves you in detached HEAD; commits made there are easy to lose. Go back with `git checkout main`.
- `git reset` on commits you've already pushed breaks everyone else.
- HTTPS clone → can't push here; use the SSH URL.
""",
    pit_zh=r"""
- 把编译产物（`program`、`*.o`）提交了——应写进 `.gitignore`。
- 忘了 `git commit -a` 不会加入**新**文件。
- `git checkout HASH` 进入分离 HEAD，在那里做的提交容易丢。用 `git checkout main` 回去。
- 对已经推送的提交用 `git reset` 会搞乱所有人。
- 用 HTTPS 克隆 → 本课程中不能推送；要用 SSH 地址。
""")
part("l4-setup", "Identity and a first repository", "身份与第一个仓库",
     code=r"""
git config --global user.name "YOURNAME"
git config --global user.email "YOUREMAIL"
mkdir project1 && cd project1 && git init
# write main.c
git status          # main.c untracked (red)
git add main.c      # staged (green)
git commit -m "first file"
git log
""",
     en=r"On a lab-machine VM, put the two `git config` lines in a Vagrantfile provision block with `privileged: false`. Change the editor with `export EDITOR=nano` (in `~/.profile`).",
     zh=r"在实验室机器的虚拟机上，把两行 `git config` 放进 Vagrantfile 的 provision 块并加 `privileged: false`。用 `export EDITOR=nano`（写在 `~/.profile`）更换编辑器。",
     see=["git-config", "git-init", "commit", "three-states"])
part("l4-ignore", "Ignoring the compiled program", "忽略编译出的程序",
     code=r"""
gcc main.c -o program && ./program
echo program > .gitignore
git add .gitignore && git commit -m "ignore program"
""",
     en=r"The binary disappears from `git status`; `.gitignore` itself **is** committed.",
     zh=r"二进制文件从 `git status` 中消失；`.gitignore` 本身**要**提交。",
     see=["gitignore"])
part("l4-undo", "Diff, restore, checkout, revert, reset", "diff、restore、checkout、revert、reset",
     code=r"""
git diff HASH                 # now vs that commit
git restore -s HASH main.c    # working copy -> old version (shows as modified)
git restore main.c            # back to latest
git checkout HASH             # detached HEAD, status says clean
git checkout main             # back
git revert HASH               # new commit undoing HASH (safe when shared)
git reset HASH                # move branch back; --hard also resets files
""", see=["git-diff", "git-restore", "git-checkout", "revert-reset"])
part("l4-branch", "Branch and merge", "分支与合并",
     code=r"""
git branch docs && git switch docs
# add README.md, commit twice; add a comment to main.c, commit
git switch main               # README disappears here
# change the output string, commit
git merge docs                # editor opens: "Merge branch 'docs'"
git branch -d docs
""",
     en=r"Logs differ on the two branches until the merge; after it, main has both the README and both edits to `main.c`.",
     zh=r"合并前两个分支的日志不同；合并后 main 同时拥有 README 和对 `main.c` 的两处修改。",
     see=["branch", "merge"])
part("l4-github", "GitHub over SSH", "通过 SSH 使用 GitHub",
     code=r"""
# GitHub: Settings → SSH and GPG keys → New SSH key → paste id_ed25519.pub
git clone git@github.com:USERNAME/REPONAME.git
git remote show origin
git config --global pull.rebase false
# edit + commit locally, edit a different line on the web, then:
git push            # rejected: remote has work you don't have
git pull            # merge commit
git push
""", see=["https-vs-ssh", "remote", "pull-push"])

# ======================================================================  L5
lab(5, "Collaborating with Git", "实验 5：Git 协作",
    ["05-git/lab/pushpull.md", "05-git/lab/pullrequest.md", "05-git/lab/puzzle.md"],
    "In a team: share one repository, create and resolve conflicts (merge and rebase), organise work with develop and feature branches, and contribute without access via forks, pull requests and patches.",
    "以小组形式：共享一个仓库，制造并解决冲突（merge 与 rebase），用 develop 和功能分支组织工作，并通过 fork、PR 和补丁在无权限时贡献代码。",
    exam_en=r"""
- Conflict markers: `<<<<<<< HEAD` (yours) / `=======` / `>>>>>>> 51224257` (the incoming commit) (example paper Q16).
- Merge conflict: edit → `git add` → `git commit`. Rebase conflict: edit → `git add` → `git rebase --continue`.
- Rebase and force-push only on **private** branches.
""",
    exam_zh=r"""
- 冲突标记：`<<<<<<< HEAD`（你的）/ `=======` / `>>>>>>> 51224257`（合并进来的提交）（样卷第 16 题）。
- merge 冲突：编辑 → `git add` → `git commit`。rebase 冲突：编辑 → `git add` → `git rebase --continue`。
- 只在**私有**分支上 rebase 和强推。
""",
    pit_en=r"""
- Pushing without pulling → rejected. Pull first.
- Leaving conflict markers in the file and committing.
- `git push --force` on develop/main overwrites teammates' work.
""",
    pit_zh=r"""
- 不先 pull 就 push → 被拒。先 pull。
- 把冲突标记留在文件里就提交了。
- 在 develop/main 上 `git push --force` 会覆盖队友的工作。
""")
part("l5-shared", "Shared repository: avoiding and resolving conflicts", "共享仓库：避免与解决冲突",
     en=r"""
- One member creates the repo and adds the others as collaborators; everyone clones it.
- Take turns: `git pull` → edit → commit → `git pull` → `git push`.
- Then everybody edits the **same line**: the second person to push is rejected, `git pull` reports a conflict, they edit the file, `git add`, `git commit`, `git pull` again in case, `git push`.
""",
     zh=r"""
- 一人建仓库并把其他人加为协作者；每人 clone。
- 轮流：`git pull` → 修改 → 提交 → `git pull` → `git push`。
- 然后大家改**同一行**：第二个推送的人被拒，`git pull` 报冲突，编辑文件，`git add`，`git commit`，以防万一再 `git pull`，然后 `git push`。
""", see=["shared-access", "merge-conflict"])
part("l5-rebase", "Resolving with fetch + rebase", "用 fetch + rebase 解决",
     code=r"""
git fetch
git rebase origin/main
# fix conflicts
git add FILE
git rebase --continue
git push
git config --global pull.rebase true   # make pull do fetch+rebase
""", see=["rebase", "pull-rebase"])
part("l5-develop", "develop and feature branches", "develop 与功能分支",
     code=r"""
git switch -c develop && git push --set-upstream origin develop   # one person
git branch -a                       # see remote branches
git switch -c feature-x && git push --set-upstream origin feature-x
# ... commits, git push ...
git fetch && git switch develop && git pull
git merge feature-x && git push
# if develop moved on while you worked:
git switch feature-x && git rebase develop
git push --force origin feature-x   # private branch only
""", see=["feature-branches", "force-push"])
part("l5-pr", "Forks, pull requests and patches", "Fork、Pull Request 与补丁",
     code=r"""
# fork on GitHub, clone YOUR fork, commit, push, then "New pull request"
git fetch
git format-patch origin/main        # contributor: creates 0001-*.patch
git apply 0001-*.patch              # owner: changes files only, then commit
git am 0001-*.patch                 # owner: applies as a commit
""", see=["fork-pr", "patches"])
part("l5-puzzle", "Puzzle: recover a deleted commit (not examinable)", "谜题：找回删除的提交（不考）",
     code=r"""
git reflog | grep -i treasure
git cherry-pick HASH                 # or: git checkout HASH
git cat-file -p HASH                 # inspect objects in .git/objects
""",
     en=r"`git gc` removes unreachable objects, so recovery is only possible until it runs.",
     zh=r"`git gc` 会清除不可达对象，所以只有在它运行之前才能找回。",
     see=["reflog"])

# ======================================================================  L6
lab(6, "Testing: Unity, TDD and automation", "实验 6：Unity、TDD 与自动化测试",
    ["06-testing/lab/tdd.md", "06-testing/lab/automation.md"],
    "Install the Unity C test framework, build a calculator test-first, then run tests automatically with a Git pre-commit hook and GitHub Actions.",
    "安装 C 测试框架 Unity，用测试先行的方式构建计算器，再用 Git pre-commit 钩子和 GitHub Actions 自动运行测试。",
    exam_en=r"""
- RED → GREEN → REFACTOR, keeping every test.
- A hook/CI fails when the test program exits non-zero.
- Hooks are local; CI runs on the shared repository for everybody.
""",
    exam_zh=r"""
- 红 → 绿 → 重构，保留每一个测试。
- 测试程序以非 0 退出时，钩子 / CI 就判定失败。
- 钩子只在本地；CI 在共享仓库上为所有人运行。
""",
    pit_en=r"""
- Missing `-I /usr/local/include/unity/` → "unity.h not found"; missing `-l unity` → undefined references.
- Forgetting `chmod +x .git/hooks/pre-commit` → hook never runs.
- Workflow triggered on `main` while your branch is `master` (or vice versa).
""",
    pit_zh=r"""
- 没加 `-I /usr/local/include/unity/` → 找不到 unity.h；没加 `-l unity` → 未定义引用。
- 忘了 `chmod +x .git/hooks/pre-commit` → 钩子从不运行。
- 工作流在 `main` 上触发，而你的分支叫 `master`（或反过来）。
""")
part("l6-unity", "Install Unity and run a first test", "安装 Unity 并运行第一个测试",
     code=r"""
git clone https://github.com/ThrowTheSwitch/Unity.git
cd Unity && cmake . && sudo make install
cd ~/calculator     # contains calc.c and test.c
gcc -I /usr/local/include/unity/ -o tests test.c -l unity
./tests             # test.c:13:test_add:PASS ... OK
export CPATH=/usr/local/include/unity/
gcc -o tests test.c -l unity; ./tests
""", see=["unity"])
part("l6-tdd", "Build the calculator test-first", "测试先行地构建计算器",
     en=r"""
- `test_sub`: copy `add` as `sub` → "Expected 0 Was 2" (RED) → fix to subtract (GREEN).
- Edge case: decide what `add(INT_MAX, 1)` should do, write the assert, then implement.
- Spec: add, subtract, multiply, divide, exponentiate for ints and floats; `calculate("2 * 2")` returns the result as a string. Extend coverage: big/small numbers, division by zero, odd characters.
""",
     zh=r"""
- `test_sub`：先把 `add` 复制成 `sub` → “Expected 0 Was 2”（红）→ 改成减法（绿）。
- 边界情况：先决定 `add(INT_MAX, 1)` 应该怎样，写断言，再实现。
- 规格：整数和浮点数的加、减、乘、除、乘方；`calculate("2 * 2")` 以字符串返回结果。扩大覆盖：大数、小数、除以零、奇怪字符。
""", see=["tdd", "testing-question"])
part("l6-hook", "Pre-commit hook", "pre-commit 钩子",
     code=r"""
cat > .git/hooks/pre-commit <<'EOF'
#!/bin/sh
gcc -I /usr/local/include/unity -o tests test.c -l unity
./tests
EOF
chmod +x .git/hooks/pre-commit
git commit -a              # with a broken calc.c: shows FAIL, commit aborted
git commit -a --no-verify  # skip the hook (deliberately)
""", see=["git-hooks"])
part("l6-actions", "GitHub Actions", "GitHub Actions",
     code=r"""
git remote add origin git@github.com:USERNAME/REPONAME.git
git push -u origin master
mkdir -p .github/workflows    # add tests.yml (see concept 6.6.2)
git add .github && git commit -m "CI" && git push
""",
     en=r"Watch the run under the **Actions** tab. Push a failing test (with `--no-verify`) and then a syntax error: both turn red, but at different steps (run tests vs compile).",
     zh=r"在 **Actions** 标签页查看运行。用 `--no-verify` 推一个会失败的测试，再推一个语法错误：两次都会变红，但失败在不同步骤（运行测试 vs 编译）。",
     see=["github-actions"])

# ======================================================================  L7
lab(7, "Debugging: crackmes", "实验 7：调试（crackme）",
    ["07-debugging/lab/README.md", "07-debugging/lab/GNUmakefile"],
    "Find the password of seven small programs without reading their source, using strings, ltrace, strace, objdump and gdb.",
    "不看源码，用 strings、ltrace、strace、objdump 和 gdb 找出七个小程序的密码。",
    exam_en=r"""
- `-g` adds debugging symbols (example paper Q20). gdb = the GNU Debugger (Q22).
- Reading `strace`: a failed `openat(...) = -1 ENOENT` followed by `SIGSEGV` → the program used a NULL `FILE*` it never checked (example paper Q21).
- `make` converts files according to rules; pattern rule `%.a: %.b` with `$<` (source) and `$@` (target) (Q17, Q19).
""",
    exam_zh=r"""
- `-g` 加入调试符号（样卷第 20 题）。gdb = GNU 调试器（第 22 题）。
- 读 `strace`：`openat(...) = -1 ENOENT` 失败之后出现 `SIGSEGV` → 程序用了没检查过的 NULL `FILE*`（样卷第 21 题）。
- `make` 根据规则转换文件；模式规则 `%.a: %.b` 中 `$<` 是源文件、`$@` 是目标（第 17、19 题）。
""",
    pit_en=r"""
- Reading the source (or `cheater.sh`) defeats the purpose.
- `step` vs `next`: `step` dives into `strcmp`/`malloc`; use `next` to stay in `main`.
- macOS uses `lldb`/`dtrace`; only the tools taught are examined.
""",
    pit_zh=r"""
- 直接看源码（或 `cheater.sh`）就失去了练习意义。
- `step` 与 `next`：`step` 会钻进 `strcmp`/`malloc`；想留在 `main` 里用 `next`。
- macOS 用 `lldb`/`dtrace`；考试只考讲过的工具。
""")
part("l7-walk", "Walkthrough: crackme-1", "示例：crackme-1",
     code=r"""
make                                  # cc -g -O0 crackme-1.c -o crackme-1 ...
./crackme-1                           # What is the password?  -> Nope
strings -d ./crackme-1                # candidate strings: Beetlejuice, ;*3$ ...
ltrace ./crackme-1 <<< ';*3$'         # strcmp(";*3$", "Beetlejuice") = -7
gdb ./crackme-1
(gdb) b main
(gdb) run <<< 'guess'
(gdb) disas                           # => marks the current instruction
(gdb) si / i r / p $rdi               # step, registers, print
""",
     en=r"`ltrace` reveals the comparison directly: the password is the second argument of `strcmp`.",
     zh=r"`ltrace` 直接暴露了比较过程：密码就是 `strcmp` 的第二个参数。",
     see=["crackme", "ltrace", "gdb-inspect", "here-doc"])
part("l7-hints", "Strategy for the others", "其余几题的思路",
     en=r"""
| Crackme | Approach |
|---|---|
| 1A | `strings` isn't enough → `ltrace` |
| 1B | the comparison isn't a plain `strcmp` → follow it in gdb (`b`, `n`, `p`) |
| 2 | no shortcut with strings/ltrace → gdb, watch what is compared |
| 3 | ltrace shows a comparison with something that isn't your input → what was done to it first? |
| 4 | "random" password → is the random generator seeded properly? (and why is OpenBSD special?) |
| 5 | infinitely many answers; try a `.` in your input |
""",
     zh=r"""
| crackme | 思路 |
|---|---|
| 1A | 光靠 `strings` 不够 → 用 `ltrace` |
| 1B | 比较的不是普通 `strcmp` → 在 gdb 里跟踪（`b`、`n`、`p`） |
| 2 | strings/ltrace 走不了捷径 → 用 gdb 看比较了什么 |
| 3 | ltrace 里比较的不是你的输入 → 输入先被怎么处理了？ |
| 4 | “随机”密码 → 随机数生成器的种子设对了吗？（OpenBSD 为什么特殊？） |
| 5 | 有无穷多个解；在输入里试试 `.` |
""", see=["crackme", "strace", "gdb-break-step"])

# ======================================================================  L8
lab(8, "Entity relationships and schema design", "实验 8：实体联系与模式设计",
    ["08-sql/lab/README.md", "08-sql/lab/uni-diagram.png"],
    "Read an ER diagram, draw one for a society database, and implement it as a CREATE/DROP script in SQLite.",
    "读懂一张 ER 图，为社团数据库画一张 ER 图，并用 SQLite 写成建表/删表脚本。",
    exam_en=r"""
- Foreign key goes on the **many** side of a one-to-many; many-to-many needs a join table.
- Create referenced tables first, drop in reverse order; `PRAGMA foreign_keys = ON;`.
- Spreadsheets are fine for small jobs like bookkeeping, not for large or nationally important data (example paper Q23).
""",
    exam_zh=r"""
- 一对多时外键放在**多**的一侧；多对多需要连接表。
- 先建被引用的表，删表顺序相反；`PRAGMA foreign_keys = ON;`。
- 电子表格适合记账这类小任务，不适合大量或国家级重要数据（样卷第 23 题）。
""",
    pit_en=r"""
- Storing a list (attendees) in one column → not 1NF.
- Storing the same fact twice (unit name in Enrolment) → contradictions after updates.
- Forgetting `NOT NULL` for mandatory relationships.
""",
    pit_zh=r"""
- 在一列里存列表（参加者）→ 不满足 1NF。
- 同一事实存两遍（在 Enrolment 里再存课程名）→ 更新后产生矛盾。
- 必选联系忘了加 `NOT NULL`。
""")
part("l8-read", "Reading the university ER diagram", "读懂大学 ER 图",
     en=r"""
Tables Unit(id, title, code, level, cp), Student(id, name, username, cohort, grade), Lecturer(id, name, username, office), RGroup(id, name); relationships *enrols* (with attribute grade), *directs*, *belongs to*.
""",
     zh=r"""
表：Unit(id, title, code, level, cp)、Student(id, name, username, cohort, grade)、Lecturer(id, name, username, office)、RGroup(id, name)；联系：*enrols*（带属性 grade）、*directs*、*belongs to*。
""",
     sol_en=r"""
| Relationship | Cardinality (crow's feet) | Implementation |
|---|---|---|
| Student enrols in Unit | many-to-many, optional both ways (a unit may have no students yet) | join table Enrol(student FK, unit FK, grade) |
| Lecturer directs Unit | each unit has exactly **one** director (mandatory); a lecturer directs zero or more | `Unit.director` FK, NOT NULL |
| Lecturer belongs to RGroup | a lecturer is in at most one group (optional); a group has one or more lecturers | `Lecturer.rgroup` FK, nullable |
""",
     sol_zh=r"""
| 联系 | 基数（鸦爪符号） | 实现 |
|---|---|---|
| 学生选修课程 | 多对多，两边都可选（课程可以暂时没有学生） | 连接表 Enrol(student 外键, unit 外键, grade) |
| 讲师主管课程 | 每门课恰好**一个**主管（必选）；讲师可主管 0 门或多门 | `Unit.director` 外键，NOT NULL |
| 讲师属于研究组 | 讲师至多属于一个组（可选）；每组至少一名讲师 | `Lecturer.rgroup` 外键，可为空 |
""", see=["er-diagram", "foreign-key"])
part("l8-hovsoc", "HovSoc: design and CREATE/DROP script", "HovSoc：设计与建表脚本",
     en=r"""
Members (name, optional student number, unique e-mail, skill level ≥ 0); a committee of members with unique roles that must all be filled; events (date, name, location, optional description, organiser = a member); attendance (many members per event). Never two events at the same location on the same date; names are not unique.
""",
     zh=r"""
成员（姓名、可选学号、唯一邮箱、技能等级 ≥ 0）；委员会由成员组成，职位唯一且每个职位必须有人；活动（日期、名称、地点、可选描述、组织者 = 某成员）；参加（每个活动多名成员）。同一地点同一天不会有两个活动；活动名不唯一。
""",
     sol_code=r"""
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS Attends;
DROP TABLE IF EXISTS Event;
DROP TABLE IF EXISTS Committee;
DROP TABLE IF EXISTS Member;

CREATE TABLE Member (
  id INTEGER PRIMARY KEY,                      -- surrogate key
  name TEXT NOT NULL,
  studentNo TEXT UNIQUE,                       -- optional
  email TEXT NOT NULL UNIQUE,
  skill INTEGER NOT NULL CHECK (skill >= 0));
CREATE TABLE Committee (
  role TEXT PRIMARY KEY,                       -- one row per role, all filled
  member INTEGER NOT NULL UNIQUE REFERENCES Member(id));
CREATE TABLE Event (
  id INTEGER PRIMARY KEY,
  date TEXT NOT NULL,
  location TEXT NOT NULL,
  name TEXT NOT NULL,
  description TEXT,                            -- optional
  organiser INTEGER NOT NULL REFERENCES Member(id),
  UNIQUE (location, date));                    -- candidate key
CREATE TABLE Attends (
  member INTEGER REFERENCES Member(id),
  event INTEGER REFERENCES Event(id),
  PRIMARY KEY (member, event));                -- many-to-many
""",
     sol_en="Run with `sqlite3 hovsoc.db < hovsoc.sql`. `(location, date)` is a candidate key; the surrogate `id` keeps foreign keys short. `member ... UNIQUE` in Committee assumes one role per person — drop it if a member may hold two roles.",
     sol_zh="用 `sqlite3 hovsoc.db < hovsoc.sql` 运行。`(location, date)` 是候选键；代理键 `id` 让外键更简短。Committee 中 `member ... UNIQUE` 假设一人只担任一个职位——若允许兼任就去掉它。",
     see=["create-table", "keys", "constraints", "normal-forms"])
part("l8-marks", "Modelling marks and exam boards", "建模：成绩与考试委员会",
     en=r"Students have an **actual mark** (input to the exam board) and an **agreed mark** (on the transcript). Store the agreed mark; the actual mark can be recomputed from component marks rather than stored twice.",
     zh=r"学生有**原始分**（交给考试委员会的）和**确认分**（写进成绩单的）。存储确认分；原始分可以从各组成部分的分数重新算出，而不是存两份。",
     see=["normal-forms", "relational-model"])

# ======================================================================  L9
lab(9, "SQL queries: elections and census", "实验 9：SQL 查询（选举与人口普查）",
    ["09-sql/lab/README.md", "09-sql/lab/Elections.db", "09-sql/lab/Census.db"],
    "Answer each question with a single query over the 2014 Bristol elections and the 2011 census data, joining by names instead of hard-coding ids. All answers below were run against the real databases.",
    "用单条查询回答 2014 年布里斯托选举和 2011 年人口普查数据的问题，按名称连接而不是硬编码 id。下面所有答案都在真实数据库上运行验证过。",
    exam_en=r"""
- `WHERE name = 'Keanu %'` is an exact comparison — `%` is only a wildcard with `LIKE` (example paper Q27).
- `ORDER BY revenue DESC LIMIT 3` = top three (Q28).
- INNER JOIN keeps only rows that match on both sides (Q26).
""",
    exam_zh=r"""
- `WHERE name = 'Keanu %'` 是精确比较——`%` 只有配合 `LIKE` 才是通配符（样卷第 27 题）。
- `ORDER BY revenue DESC LIMIT 3` = 前三名（第 28 题）。
- 内连接只保留两边都能匹配的行（第 26 题）。
""",
    pit_en=r"""
- Percentages with integers: `100 * a / b` truncates → write `100.0 * a / b`.
- Grouping by name when names repeat (ward names are not unique) → group by the code/id.
- `WHERE` on an aggregate → use `HAVING`.
""",
    pit_zh=r"""
- 用整数算百分比：`100 * a / b` 会截断 → 写成 `100.0 * a / b`。
- 名字有重复时按名字分组（选区名不唯一）→ 按编码/id 分组。
- 对聚合结果用 `WHERE` → 应该用 `HAVING`。
""")
part("l9-schema", "The two schemas", "两个数据库的结构",
     code=r"""
Elections:  Ward(id, name, electorate)  Party(id, name)
            Candidate(id, name, party -> Party, ward -> Ward, votes)
Census:     Country(code, name)  Region(code, parent -> Country, name)
            County(code, name, parent -> Region, country)        -- "CLU"
            Ward(code, name, parent -> County)  Occupation(id, name)  -- 9 classes
            Statistic(wardId -> Ward, occId -> Occupation, gender 1=F 0=M, data)
""", see=["join", "foreign-key"])
part("l9-easy-e", "Easier: elections", "基础题：选举",
     sol_code=r"""
-- 1 parties, alphabetical
SELECT DISTINCT Party.name FROM Candidate JOIN Party ON Candidate.party = Party.id
ORDER BY Party.name;
-- 2 parties in Bedminster
SELECT DISTINCT Party.name FROM Candidate
JOIN Party ON Candidate.party = Party.id JOIN Ward ON Candidate.ward = Ward.id
WHERE Ward.name = 'Bedminster' ORDER BY Party.name;
-- 3 Labour votes in Stockwood                                        -> 855
SELECT Candidate.votes FROM Candidate
JOIN Party ON Candidate.party = Party.id JOIN Ward ON Candidate.ward = Ward.id
WHERE Ward.name = 'Stockwood' AND Party.name = 'Labour';
-- 4 Southville candidates, winner first    -> Charlie Bolton, Green, 1700 ...
SELECT Candidate.name, Party.name, Candidate.votes FROM Candidate
JOIN Party ON Candidate.party = Party.id JOIN Ward ON Candidate.ward = Ward.id
WHERE Ward.name = 'Southville' ORDER BY Candidate.votes DESC;
-- 5 Knowle winner only                -> Gary Hopkins, Liberal Democrat, 1659
...same as 4 with 'Knowle' ... ORDER BY Candidate.votes DESC LIMIT 1;
""", see=["select", "join"])
part("l9-easy-c", "Easier: census", "基础题：人口普查",
     sol_code=r"""
-- 1 CLU, region, country of Cabot
--   -> Bristol, City of (E06000023) / South West (E12000009) / England (E92000001)
SELECT Ward.name, County.name, County.code, Region.name, Region.code, Country.name, Country.code
FROM Ward JOIN County ON Ward.parent = County.code
JOIN Region ON County.parent = Region.code JOIN Country ON Region.parent = Country.code
WHERE Ward.name = 'Cabot';
-- 2 women managers in Cabot (occupation 1)                          -> 229
SELECT data FROM Statistic JOIN Ward ON Statistic.wardId = Ward.code
WHERE Ward.name = 'Cabot' AND occId = 1 AND gender = 1;
-- 3 Stoke Bishop: men per occupation, columns name, number
SELECT Occupation.name AS name, Statistic.data AS number
FROM Statistic JOIN Ward ON Statistic.wardId = Ward.code
JOIN Occupation ON Statistic.occId = Occupation.id
WHERE Ward.name = 'Stoke Bishop' AND gender = 0 ORDER BY Occupation.id;
""", see=["select", "join"])
part("l9-hard-e", "Harder: elections", "进阶题：选举",
     sol_code=r"""
-- 1 total votes in Bristol                                          -> 78807
SELECT sum(votes) FROM Candidate;
-- 2 Windmill Hill: votes and % of electorate                   -> 3818 | 40.4
SELECT sum(c.votes) AS votes, round(100.0 * sum(c.votes) / w.electorate, 1) AS percent
FROM Candidate c JOIN Ward w ON c.ward = w.id WHERE w.name = 'Windmill Hill';
-- 3 Southville: % of the ward's votes          -> Bolton 42.5, Phipps 33.1 ...
SELECT c.name, p.name,
       round(100.0 * c.votes / (SELECT sum(votes) FROM Candidate WHERE ward = c.ward), 1) AS percent
FROM Candidate c JOIN Party p ON c.party = p.id JOIN Ward w ON c.ward = w.id
WHERE w.name = 'Southville' ORDER BY percent DESC;
-- 4 Conservative % in each ward (sub-query as a table)        -> 24 rows
SELECT w.name, round(100.0 * c.votes / t.total, 1) AS percent
FROM Candidate c JOIN Party p ON c.party = p.id JOIN Ward w ON c.ward = w.id
JOIN (SELECT ward, sum(votes) AS total FROM Candidate GROUP BY ward) t ON t.ward = c.ward
WHERE p.name = 'Conservative' ORDER BY w.name;
-- 5 Labour's rank in Whitchurch Park = 1 + candidates with more votes  -> 3
SELECT 1 + count(*) FROM Candidate c JOIN Ward w ON c.ward = w.id
WHERE w.name = 'Whitchurch Park'
  AND c.votes > (SELECT c2.votes FROM Candidate c2 JOIN Party p ON c2.party = p.id
                 WHERE c2.ward = c.ward AND p.name = 'Labour');
-- 6 total votes per party                -> Labour 22785, Conservative 18367 ...
SELECT p.name AS party, sum(c.votes) AS votes
FROM Candidate c JOIN Party p ON c.party = p.id GROUP BY p.id ORDER BY votes DESC;
-- 7 wards where Green beat Labour (self-join on Candidate)
--   -> Bishopston 1078, Redland 776, Southville 378, Stoke Bishop 45
SELECT w.name AS ward, g.votes - l.votes AS difference
FROM Ward w
JOIN Candidate g ON g.ward = w.id JOIN Party pg ON g.party = pg.id AND pg.name = 'Green'
JOIN Candidate l ON l.ward = w.id JOIN Party pl ON l.party = pl.id AND pl.name = 'Labour'
WHERE g.votes > l.votes ORDER BY difference DESC;
""",
     sol_en="Patterns to recognise: totals → `sum`; percentage → `100.0 *` and a per-ward total (correlated sub-query or a grouped sub-query joined as a table); rank → count who beat you; compare two rows of the same table → join it twice under different aliases.",
     sol_zh="要认出的套路：总数 → `sum`；百分比 → `100.0 *` 加每个选区的总数（相关子查询，或把分组子查询当表连接）；排名 → 数有几个人比你多；同一张表里两行比较 → 用不同别名连接两次。",
     see=["aggregate", "subquery", "join", "self-join"])
part("l9-hard-c", "Harder: census", "进阶题：人口普查",
     sol_code=r"""
-- 1 women in sales & customer service, Cabot                        -> 362
SELECT data FROM Statistic s JOIN Ward w ON s.wardId = w.code
JOIN Occupation o ON s.occId = o.id
WHERE w.name = 'Cabot' AND o.name LIKE 'Sales%' AND gender = 1;
-- 2 everyone in that class in Cabot (sum over genders)              -> 663
-- 3 caring, leisure & other service in City of Bristol CLU        -> 17934
SELECT sum(data) FROM Statistic s JOIN Ward w ON s.wardId = w.code
JOIN County c ON w.parent = c.code JOIN Occupation o ON s.occId = o.id
WHERE c.name = 'Bristol, City of' AND o.name LIKE 'Caring%';
-- 4 Cabot: people per occupation class          (GROUP BY o.id, 9 rows)
-- 5 smallest ward by working population  -> 81, St. Martin's, Isles of Scilly
SELECT sum(data) AS pop, w.name, c.name FROM Statistic s
JOIN Ward w ON s.wardId = w.code JOIN County c ON w.parent = c.code
GROUP BY w.code ORDER BY pop ASC LIMIT 1;
-- 6 smallest and largest in one table  (UNION; largest = City and Hunslet, Leeds, 16717)
SELECT * FROM (... ORDER BY pop ASC  LIMIT 1)
UNION
SELECT * FROM (... ORDER BY pop DESC LIMIT 1);
-- 7 average ward working population in London                   -> 6327.4
SELECT avg(pop) FROM (SELECT sum(data) AS pop FROM Statistic s
  JOIN Ward w ON s.wardId = w.code JOIN County c ON w.parent = c.code
  JOIN Region r ON c.parent = r.code WHERE r.name = 'London' GROUP BY w.code);
-- 8 same for every region: GROUP BY region in the outer query (9 rows)
-- 9 % of managers who are women, per region       (CASE inside sum)
SELECT r.name, round(100.0 * sum(CASE WHEN gender = 1 THEN data ELSE 0 END) / sum(data), 2)
FROM Statistic s JOIN Ward w ON s.wardId = w.code JOIN County c ON w.parent = c.code
JOIN Region r ON c.parent = r.code WHERE s.occId = 1 GROUP BY r.code;
-- 10 London CLUs x occupation with count >= 10000, ascending
SELECT c.name AS CLU, o.name AS occupation, sum(data) AS count
FROM Statistic s JOIN Ward w ON s.wardId = w.code JOIN County c ON w.parent = c.code
JOIN Region r ON c.parent = r.code JOIN Occupation o ON s.occId = o.id
WHERE r.name = 'London' GROUP BY c.code, o.id HAVING count >= 10000 ORDER BY count;
-- 11 occupation | women | men   (two CASE sums, GROUP BY occupation)
-- 12 query 9 UNION ALL one extra row 'England' computed over all regions
""",
     sol_en="New tools here: `CASE WHEN … THEN … ELSE … END` inside `sum` to split by gender; `UNION` to stack two one-row results; `HAVING` on the aggregate alias.",
     sol_zh="这里用到的新工具：在 `sum` 里用 `CASE WHEN … THEN … ELSE … END` 按性别拆分；用 `UNION` 把两个单行结果叠起来；对聚合别名用 `HAVING`。",
     see=["aggregate", "having", "subquery", "select-order"])

# ======================================================================  L10
lab(10, "Datalog: family tree and access control", "实验 10：Datalog（家族树与访问控制）",
    ["10-datalog/lab/README.org", "10-datalog/lab/addams.dot"],
    "Encode the Addams family in AbcDatalog and derive relatives with rules, then build an access-control system: DAC, delegation, roles and mandatory access control. Rules below were checked with a small evaluator.",
    "在 AbcDatalog 中录入亚当斯家族，用规则推导亲属关系，然后构建访问控制系统：DAC、委托、角色和强制访问控制。下面的规则都用一个小型求值器验证过。",
    exam_en=r"""
- With `sibling(A,B) :- parent(A,C), parent(B,C).` a person is also their own sibling, and siblings are found through **any** shared parent (example paper Q31).
- Recursion is what SQL struggles with (example paper Q30).
""",
    exam_zh=r"""
- 对 `sibling(A,B) :- parent(A,C), parent(B,C).`，一个人也是自己的兄弟姐妹，并且通过**任一**共同父母都能找到兄弟姐妹（样卷第 31 题）。
- 递归正是 SQL 不擅长的（样卷第 30 题）。
""",
    pit_en=r"""
- Mixing up argument order: the lab uses `parent(Child, Parent)`.
- Variables must start with an upper-case letter; `sharron` is a constant, `Sharron` a variable.
- Every variable in the head must appear in the body.
""",
    pit_zh=r"""
- 参数顺序搞反：实验约定 `parent(孩子, 父母)`。
- 变量必须大写开头；`sharron` 是常量，`Sharron` 是变量。
- 头部出现的每个变量都必须出现在规则体里。
""")
part("l10-addams", "The Addams family", "亚当斯家族",
     code=r"""
java -jar AbcDatalog-0.7.0.jar &      # GUI; over SSH use ssh -X
parent(pugsley, gomez).  parent(pugsley, morticia).
parent(wednesday, gomez). parent(wednesday, morticia).
parent(pubert, gomez).   parent(pubert, morticia).
parent(debbie, sharron). parent(debbie, dave).
parent(gomez, father).   parent(gomez, eudora).
parent(fester, father).  parent(fester, eudora).
parent(morticia, fatherFrump). parent(morticia, hester).
parent(ophella, fatherFrump).  parent(ophella, hester).
parent(eudora, mooma).  parent(eudora, slurp).
parent(fatherFrump, mooma). parent(fatherFrump, slurp).
parent(jester, mooma).  parent(jester, slurp).
parent(sloom, mooma).   parent(sloom, slurp).
""",
     en=r"Tasks: check `parent(X, sharron)`; define sibling (and fix `sibling(wednesday, wednesday)`); cousin; aunt/uncle; whose uncle is Fester; Pugsley's and Debbie's aunts and uncles.",
     zh=r"任务：检查 `parent(X, sharron)`；定义兄弟姐妹（并修正 `sibling(wednesday, wednesday)`）；堂表亲；叔舅姑姨；Fester 是谁的叔叔；Pugsley 和 Debbie 的叔舅姑姨。",
     sol_code=r"""
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
sibling(X, Y)     :- parent(X, P), parent(Y, P), X != Y.
cousin(X, Y)      :- parent(X, P), parent(Y, Q), sibling(P, Q).
auntOrUncle(X, A) :- parent(X, P), sibling(P, A).

parent(X, sharron)?          -> debbie
sibling(gomez, X)?           -> fester
cousin(gomez, morticia)?     -> true  (Eudora and Father Frump are siblings)
auntOrUncle(X, fester)?      -> pugsley, wednesday, pubert
auntOrUncle(pugsley, A)?     -> fester, ophella
auntOrUncle(debbie, A)?      -> none
""",
     sol_en="Defining cousin as \"children of siblings\" avoids needing negation (\"shares a grandparent but is not a sibling\" would need `not`). The `?`-at-the-end query form is how AbcDatalog's GUI is used in the lab; the lecture writes queries as `?- p(X).`",
     sol_zh="把堂表亲定义为“兄弟姐妹的孩子”就不需要否定（“有共同祖父母但不是兄弟姐妹”需要 `not`）。实验里 AbcDatalog 图形界面的查询写法是末尾加 `?`；讲座写成 `?- p(X).`。",
     see=["horn-clauses", "datalog-negation", "datalog-recursion"])
part("l10-dac", "Access control: DAC, delegation, roles", "访问控制：DAC、委托、角色",
     sol_code=r"""
% discretionary
canRead(P, F) :- owner(F, P).
canRead(P, F) :- principal(P), othersCanRead(F).
% delegation: A speaks for C if A delegates (possibly via others) to C
speaksFor(A, A) :- principal(A).
speaksFor(A, C) :- delegatesTo(A, B), speaksFor(B, C).
canRead(P, F) :- owner(F, O), speaksFor(O, D), saysCanRead(D, P, F), principal(P).
% roles: a grant may name a role instead of a principal
canRead(P, F) :- owner(F, O), speaksFor(O, D), saysCanRead(D, R, F), holds(P, R).
""",
     sol_en="Tested cases: a non-owner's `saysCanRead` has no effect; bob → carol → dave delegation lets dave grant bob's file; a grant to role `auditor` reaches whoever `holds` it. Without `principal(P)` in the third rule, the role name itself would appear as a reader.",
     sol_zh="测试过的情况：非属主的 `saysCanRead` 无效；bob → carol → dave 的委托链让 dave 能授权读 bob 的文件；授权给角色 `auditor` 会传到持有该角色的人。第三条规则若不加 `principal(P)`，角色名本身也会被当成读者。",
     see=["datalog-access-control", "datalog-recursion"])
part("l10-mac", "Mandatory access control", "强制访问控制",
     sol_code=r"""
level(unclassified). level(secret). level(topsecret).
below(unclassified, secret). below(secret, topsecret). below(unclassified, topsecret).
atMost(X, X) :- level(X).
atMost(X, Y) :- below(X, Y).
fileLevel(F, unclassified) :- unclassified(F).
fileLevel(F, secret)       :- secret(F).
fileLevel(F, topsecret)    :- topsecret(F).
% Bell-LaPadula (confidentiality): read down, write up
blpRead(P, F)   :- clearance(P, C), fileLevel(F, L), atMost(L, C).
blpWrite(P, F)  :- clearance(P, C), fileLevel(F, L), atMost(C, L).
% Biba as stated in the lab (integrity): write strictly down, read strictly up
bibaWrite(P, F) :- clearance(P, C), fileLevel(F, L), below(L, C).
bibaRead(P, F)  :- clearance(P, C), fileLevel(F, L), below(C, L).
""",
     sol_en="Datalog has no arithmetic comparison here, so the ordering is written as facts. For a `secret` principal: BLP read = unclassified + secret, write = secret + topsecret; Biba (lab wording) read = topsecret, write = unclassified.",
     sol_zh="这里的 Datalog 没有算术比较，所以等级顺序用事实写出来。对 `secret` 级主体：BLP 可读 unclassified + secret，可写 secret + topsecret；Biba（按实验说法）可读 topsecret，可写 unclassified。",
     see=["mac-models"])
