from model import W, S, c, cmd

# =====================================================================  W0
W(0)
S("unit", "The unit", "课程定位")
c("unit-aim", "Unit aim", "课程目标", exam=True,
  en=r"""
- Learn to use a computer "as a grown-up, not as a user": the shell and standard tools rather than GUIs.
- Taught to (almost) all incoming students: undergraduates and conversion MSc together.
- Format: one shared lecture + a two-hour lab each week. Labs build the **muscle memory** for UNIX; no attendance requirement.
- Ask the lecturers and TAs (rather than a chatbot); read the manual ([[man]]).
- Lab machines are the examinable reference system ([[posix]]).
""",
  zh=r"""
- 学会“像专业人士而不是普通用户那样”使用电脑：用 shell 和标准工具，而不是图形界面。
- 几乎所有新生都要修：本科生与转专业硕士一起上。
- 形式：每周一次大课 + 两小时实验。实验是为了练出 UNIX 的**肌肉记忆**；不考勤。
- 有问题问老师和助教（而不是聊天机器人）；学会读手册（[[man]]）。
- 实验室机器是考试所依据的参考系统（[[posix]]）。
""",
  see=["tb1-exam", "shell"])

S("exam", "Assessment", "考核")
c("tb1-exam", "Exams (TB1 structure)", "考试结构（TB1）", exam=True,
  en=r"""
- Two exams: weeks 1–10 (TB1) and weeks 11–20. Both **four-option multiple choice**, **open book**. Pass mark 40% (UG) / 50% (PG).
- Everything is examinable: lecture content, assigned reading, lab materials (unless marked non-examinable).
- TB1: 3 questions per week × 10 weeks + 1 extra question from each lecturer = 32 questions.
| Week | Topic | Module | Qs |
|---|---|---|---|
| 1 | System administration | UNIX basics | 3 |
| 2 | POSIX fundamentals | UNIX basics | 3 |
| 3 | Regular expressions | UNIX basics | 3 |
| 4 | Git basics | Version control | 3 |
| 5 | Git (collaborative) | Version control | 3 |
| 6 | Testing | Development | 3 |
| 7 | Debugging | Development | 3 |
| 8 | SQL | Databases | 3 |
| 9 | More SQL | Databases | 3 |
| 10 | Datalog | Databases | 3 |
! Open book: how you take notes is up to you. This site's Open-book print pack is designed to be printed.
""",
  zh=r"""
- 两场考试：第 1–10 讲（TB1）和第 11–20 讲。都是**四选一选择题**、**开卷**。及格线 40%（本科）/ 50%（研究生）。
- 全部可考：讲座内容、指定阅读、实验材料（除非标注不考）。
- TB1：每讲 3 题 × 10 讲 + 两位老师各 1 道附加题 = 32 题。
| 讲 | 主题 | 模块 | 题数 |
|---|---|---|---|
| 1 | 系统管理 | UNIX 基础 | 3 |
| 2 | POSIX 基础 | UNIX 基础 | 3 |
| 3 | 正则表达式 | UNIX 基础 | 3 |
| 4 | Git 基础 | 版本控制 | 3 |
| 5 | Git 协作 | 版本控制 | 3 |
| 6 | 测试 | 开发实践 | 3 |
| 7 | 调试 | 开发实践 | 3 |
| 8 | SQL 设计 | 数据库 | 3 |
| 9 | SQL 查询 | 数据库 | 3 |
| 10 | Datalog | 数据库 | 3 |
! 开卷考试：笔记形式不限。本站的“开卷打印包”就是为打印准备的。
""",
  see=["unit-aim"])

# =====================================================================  W1
W(1)
S("shell", "The shell & the manual", "Shell 与手册")
c("shell", "Shell & terminal", "Shell 与终端", exam=True,
  en=r"""
- **Terminal**: the window/device that shows text and takes keystrokes. **Shell**: the program in it that reads your command line and runs programs (bash on most Linux, zsh on macOS).
- **Prompt**: the shell is waiting for input. bash shows `$`, zsh `%`, root `#`. Prompts can be customised to show user, host, directory.
- One of the oldest interfaces; awkward at first, very powerful once learnt. The trick: use it every day.
- Output is text; most terminals can't show pictures (some can: kitty graphics protocol, sixels).
""",
  zh=r"""
- **终端（terminal）**：显示文字、接收按键的窗口/设备。**Shell**：运行在终端里、读取命令行并启动程序的程序（多数 Linux 是 bash，macOS 是 zsh）。
- **提示符（prompt）**：表示 shell 正在等待输入。bash 用 `$`，zsh 用 `%`，root 常用 `#`。提示符可自定义显示用户、主机、目录。
- 最古老的交互方式之一；一开始别扭，熟练后非常强大。诀窍：每天用。
- 输出是文本；大多数终端不能显示图片（少数可以：kitty 图形协议、sixel）。
""",
  see=["command-anatomy", "man", "shell-expansion"])

c("command-anatomy", "Anatomy of a command", "命令的结构", exam=True,
  en=r"""
| Part | In `ls -l --human-readable ~` | Notes |
|---|---|---|
| prompt | `$` | printed by the shell |
| command | `ls` | first word: program (or builtin) to run |
| flags / options | `-l`, `--human-readable` | short: one dash + letter; long: two dashes + word |
| argument | `~` | `~` = your home directory (expanded by the shell) |
- Press Return to run. Conventions vary: Java uses one dash for long options, Windows uses `/`.
- Short flags can usually be combined: `ls -la` = `ls -l -a`.
- Names are historical, not intuitive (`ls`, not `dir`) — learn them, they are examinable.
""",
  zh=r"""
| 部分 | 在 `ls -l --human-readable ~` 中 | 说明 |
|---|---|---|
| 提示符 | `$` | 由 shell 打印 |
| 命令 | `ls` | 第一个词：要运行的程序（或内建命令） |
| 选项/标志 | `-l`、`--human-readable` | 短选项：一个减号 + 字母；长选项：两个减号 + 单词 |
| 参数 | `~` | `~` = 你的家目录（由 shell 展开） |
- 按回车执行。约定并不统一：Java 长选项也用一个减号，Windows 用 `/`。
- 短选项通常可合并：`ls -la` = `ls -l -a`。
- 命令名是历史遗留，不直观（是 `ls` 不是 `dir`）——必须记，考试会考。
""",
  code=r"""
$ ls -l --human-readable ~
-rwx------ 1 gretch bristol 4.6K Jun 24 14:54 nigel.jpg
# permissions  links owner group size date      name
""",
  see=["shell", "unix-dac", "word-splitting"])

c("man", "The manual: man & apropos", "手册：man 与 apropos", exam=True,
  en=r"""
- `man CMD` shows the manual page **for your system** (unlike generic web answers).
- Inside man (a pager, `less`): `q` quit, `/word` search, `n` next hit, `j`/`k` scroll.
- `man man` explains man itself; `man intro` is a beginner introduction.
- Search the manual: `man -k keyword` = `apropos keyword` (e.g. `apropos git -a tutorial`).
- Sections: 1 user commands, 2 system calls, 3 library functions, 5 file formats (e.g. `man 5 passwd`), 7 overviews, 8 admin commands. `man 5 passwd` ≠ `man passwd`.
- Other built-in docs: `info` (e.g. `info gdb`), `CMD --help`.
""",
  zh=r"""
- `man 命令` 显示**你这台系统上**的手册页（不同于网上的通用答案）。
- 手册里（分页器 `less`）：`q` 退出，`/词` 搜索，`n` 下一个，`j`/`k` 上下滚动。
- `man man` 讲解 man 自身；`man intro` 是入门介绍。
- 搜索手册：`man -k 关键词` = `apropos 关键词`（如 `apropos git -a tutorial`）。
- 分节：1 用户命令，2 系统调用，3 库函数，5 文件格式（如 `man 5 passwd`），7 概述，8 管理命令。`man 5 passwd` ≠ `man passwd`。
- 其它文档：`info`（如 `info gdb`）、`命令 --help`。
""",
  see=["git-docs", "users-groups", "gdb"])

c("posix", "POSIX & portability", "POSIX 与可移植性",
  en=r"""
- **POSIX**: the standard describing how a UNIX-like system (shell, utilities, C API) should behave. Few systems follow it precisely; most vary a little, some a lot.
- The unit sticks to POSIX on the **lab machines** as the examinable standard.
- Linux: fine. macOS: mostly fine (zsh, BSD tools) but virtualisation (VirtualBox/Vagrant) won't work and the debugging lab differs. Windows: use WSL (sometimes breaks); PowerShell/CMD will not work.
- TAs are told not to help with non-lab setups → when in doubt, use a lab machine (via [[ssh]]).
""",
  zh=r"""
- **POSIX**：规定类 UNIX 系统（shell、工具、C 接口）应如何工作的标准。很少有系统完全遵守；多数略有差异，有的差很多。
- 本课程以**实验室机器**上的 POSIX 行为为考试标准。
- Linux：没问题。macOS：大体可以（zsh、BSD 版工具），但不能用 VirtualBox/Vagrant，调试实验也不同。Windows：用 WSL（偶尔出怪问题）；PowerShell/CMD 不行。
- 助教不负责非实验室环境 → 有疑问就用实验室机器（通过 [[ssh]] 登录）。
""",
  see=["shell", "vagrant"])

S("remote", "Remote access with SSH", "SSH 远程登录")
c("ssh", "SSH: client & daemon", "SSH：客户端与守护进程", exam=True,
  en=r"""
- **SSH (Secure Shell)**: protocol for an encrypted shell on another machine. Standard implementation: OpenSSH.
- `ssh` = **client** (on your machine). `sshd` = **server/daemon** (background service on the remote machine), TCP **port 22** by default.
- `ssh USER@HOST` logs in; `exit` returns. `ssh -X USER@HOST firefox` forwards X11 graphics.
- `ssh localhost` test: password prompt = client + server OK; "connection refused" = client OK, no local server; "not found" = no OpenSSH.
- Lab load balancer: `rd-mvb-linuxlab.bristol.ac.uk` (needs eduroam or VPN). Check where you are: `whoami`, `uname -a`, `hostname`.
- Debug a failing connection with `ssh -v` (`-vv`, `-vvv`).
""",
  zh=r"""
- **SSH（安全外壳）**：在另一台机器上获得加密 shell 的协议。标准实现：OpenSSH。
- `ssh` = **客户端**（在你的机器上）。`sshd` = **服务端/守护进程**（远程机器上的后台服务），默认 TCP **22 端口**。
- `ssh 用户@主机` 登录；`exit` 退出。`ssh -X 用户@主机 firefox` 转发 X11 图形界面。
- 测试 `ssh localhost`：要密码 = 客户端和服务端都正常；“connection refused” = 客户端正常但本机没开服务；“not found” = 没装 OpenSSH。
- 实验室负载均衡地址：`rd-mvb-linuxlab.bristol.ac.uk`（需 eduroam 或 VPN）。确认身份与位置：`whoami`、`uname -a`、`hostname`。
- 连接失败时用 `ssh -v`（`-vv`、`-vvv`）看调试信息。
""",
  code=r"""
$ ssh aa20123@rd-mvb-linuxlab.bristol.ac.uk
$ ssh -X evelyn@imac firefox      # run a GUI program remotely
""",
  see=["host-key", "ssh-keys", "ssh-config", "systemd"])

c("host-key", "Host key verification", "主机密钥校验", exam=True,
  en=r"""
- First connection to a new host: "authenticity of host can't be established… fingerprint SHA256:… Are you sure?" Answer `yes` → host's public key stored in `~/.ssh/known_hosts`.
- Later connections compare against `known_hosts`; a changed key triggers a warning (possible attack).
- To verify properly, have someone with **physical access** run `ssh-keyscan -q -t ed25519 localhost` on the server and compare fingerprints.
- Purpose: defeat [[mitm]] attacks.
""",
  zh=r"""
- 首次连接新主机会问：“无法确认主机真实性……指纹 SHA256:…… 是否继续？”回答 `yes` → 主机公钥写入 `~/.ssh/known_hosts`。
- 以后每次连接都与 `known_hosts` 比较；密钥变化会报警（可能遭到攻击）。
- 严格校验：让能**物理接触**服务器的人在服务器上运行 `ssh-keyscan -q -t ed25519 localhost`，对比指纹。
- 目的：防御[[mitm]]。
""",
  see=["ssh", "mitm"])

c("mitm", "Man-in-the-middle attack", "中间人攻击",
  en=r"""
- Attacker (Smith) tricks the client (Evelyn) into connecting to them instead of the real server (iMac).
- Smith relays everything both ways, so it looks normal — but can **record** and **modify** traffic.
- Defence in SSH: check the server's host key fingerprint ([[host-key]]); key-based auth never sends a reusable secret ([[ssh-keys]]).
""",
  zh=r"""
- 攻击者（Smith）诱使客户端（Evelyn）连到自己，而不是真正的服务器（iMac）。
- Smith 双向转发所有内容，看起来一切正常——但可以**记录**甚至**篡改**通信。
- SSH 中的防御：核对服务器主机密钥指纹（[[host-key]]）；密钥认证不会发送可重复使用的秘密（[[ssh-keys]]）。
""",
  see=["host-key"])

c("auth-factors", "Authentication factors", "认证因素",
  en=r"""
| Factor | Example | In SSH |
|---|---|---|
| something you know | password, PIN | password login (default, least secure) |
| something you have | key file, card, phone | key pair login |
| something you are | biometrics | — |
- Two factors together = 2FA: e.g. a key file protected by a passphrase.
- Never reuse your university password anywhere else.
""",
  zh=r"""
| 因素 | 例子 | 在 SSH 中 |
|---|---|---|
| 你知道的 | 密码、PIN | 密码登录（默认，最不安全） |
| 你拥有的 | 密钥文件、卡、手机 | 密钥对登录 |
| 你本身的 | 生物特征 | — |
- 两种因素组合 = 双因素认证：例如带口令保护的密钥文件。
- 学校密码绝不在别处重复使用。
""",
  see=["ssh-keys"])

c("ssh-keys", "SSH key pairs", "SSH 密钥对", exam=True,
  en=r"""
- Generate: `ssh-keygen -t ed25519` (modern, secure algorithm). Default location `~/.ssh/`. Empty passphrase = convenient; passphrase = 2FA.
- **Private key** `id_ed25519`: never leaves your machine. **Public key** `id_ed25519.pub`: give to every server/service (lab, GitHub).
- How login works: server sends a random **challenge**; client **signs** it with the private key; server checks the signature with the stored public key. The key itself is never sent → a breached service can't impersonate you elsewhere.
- Install on a server: append the public key to `~/.ssh/authorized_keys` (one key per line) and `chmod 600` it.
- Reusing one public key everywhere is safe security-wise but lets services link your identities (privacy). Use `-i FILE` or `IdentityFile` for different keys.
- If you overwrite an existing key you break whatever used it → answer `n` to "Overwrite?".
""",
  zh=r"""
- 生成：`ssh-keygen -t ed25519`（现代、安全的算法）。默认存放在 `~/.ssh/`。不设口令 = 方便；设口令 = 双因素。
- **私钥** `id_ed25519`：永不离开你的机器。**公钥** `id_ed25519.pub`：交给每台服务器/服务（实验室、GitHub）。
- 登录原理：服务器发送随机**挑战值**；客户端用私钥对其**签名**；服务器用存储的公钥验证签名。密钥本身从不发送 → 某个服务被攻破也无法拿你的身份登录别处。
- 部署到服务器：把公钥追加到 `~/.ssh/authorized_keys`（每行一个），再 `chmod 600`。
- 各处共用一个公钥在安全上没问题，但服务之间可据此关联你的身份（隐私问题）。不同用途可用 `-i 文件` 或 `IdentityFile` 指定不同密钥。
- 覆盖已有密钥会让依赖它的服务失效 → 遇到 “Overwrite?” 回答 `n`。
""",
  code=r"""
ssh-keygen -t ed25519
scp ~/.ssh/id_ed25519.pub USER@rd-mvb-linuxlab.bristol.ac.uk:~/.ssh/
# then, logged in on the lab machine:
cd ~/.ssh
cat id_ed25519.pub >> authorized_keys   # >> appends, > would overwrite
chmod 600 authorized_keys
""",
  see=["ssh-key-perms", "scp", "auth-factors", "https-vs-ssh", "redirection"])

c("ssh-key-perms", "Key file permissions", "密钥文件权限",
  en=r"""
| File | Mode | Meaning |
|---|---|---|
| `id_ed25519` | `-rw-------` (600) | only owner reads/writes the private key |
| `id_ed25519.pub` | `-rw-r--r--` (644) | anyone may read a public key |
| `authorized_keys` | `-rw-------` (600) | SSH **refuses** it if others can write |
| `~/.ssh/config` | not writable by others | otherwise SSH ignores it |
- SSH deliberately rejects keys/configs with loose permissions — a practical use of [[unix-dac]].
""",
  zh=r"""
| 文件 | 权限 | 含义 |
|---|---|---|
| `id_ed25519` | `-rw-------`（600） | 只有属主能读写私钥 |
| `id_ed25519.pub` | `-rw-r--r--`（644） | 公钥谁都可以读 |
| `authorized_keys` | `-rw-------`（600） | 若他人可写，SSH 会**拒绝**使用 |
| `~/.ssh/config` | 他人不可写 | 否则 SSH 不认 |
- SSH 故意拒绝权限过松的密钥/配置——这是[[unix-dac]]的实际应用。
""",
  see=["ssh-keys", "unix-dac"])

c("scp", "scp & sftp: copying over SSH", "scp 与 sftp：经 SSH 复制",
  en=r"""
- `scp SOURCE DEST` works like `cp`, but either side may be remote: `[USER@]HOST:PATH`. A colon means "on another machine".
- `sftp` gives an interactive file-transfer session. Both run over SSH, so keys/config apply.
""",
  zh=r"""
- `scp 源 目标` 用法同 `cp`，但任一侧可以是远程：`[用户@]主机:路径`。有冒号就表示“在另一台机器上”。
- `sftp` 提供交互式文件传输。两者都走 SSH，所以密钥和配置同样生效。
""",
  code=r"""
scp notes.txt lab:~/backup/       # local -> remote (using the 'lab' alias)
scp lab:~/result.csv .            # remote -> current directory
""",
  see=["ssh-config", "ssh"])

c("ssh-config", "~/.ssh/config", "SSH 配置文件",
  en=r"""
- Global config `/etc/ssh/ssh_config` (`/etc` = system-wide settings); per-user `~/.ssh/config`. See `man ssh_config`.
- A `Host` block defines an alias with its settings; then `ssh lab` is enough.
""",
  zh=r"""
- 全局配置 `/etc/ssh/ssh_config`（`/etc` 放系统级配置）；用户配置 `~/.ssh/config`。参见 `man ssh_config`。
- 一个 `Host` 块定义一个别名及其设置；之后只需 `ssh lab`。
""",
  code=r"""
Host lab
  HostName rd-mvb-linuxlab.bristol.ac.uk
  User aa20123

Host github.com
  User git
  IdentityFile ~/.ssh/github_key
  # if 'resource temporarily unavailable':
  # Hostname ssh.github.com
  # Port 22
""",
  see=["ssh", "https-vs-ssh"])

S("vm", "Virtual machines with Vagrant", "用 Vagrant 管理虚拟机")
c("vagrant", "Vagrant & the Vagrantfile", "Vagrant 与 Vagrantfile", exam=True,
  en=r"""
- **Vagrant** manages VMs from a config file, the `Vagrantfile` (Ruby syntax); it downloads **boxes** (disk images) and runs them with a **provider** such as VirtualBox.
- `config.vm.box = "generic/debian12"` picks the image; `synced_folder ".", "/shared"` shares the Vagrantfile's folder with the guest at `/shared`.
- `config.vm.provision "shell", inline: <<-SHELL … SHELL` runs commands (as root) when the box is first created — a [[here-doc]]. `privileged: false` runs them as user `vagrant`.
- Commands: `vagrant up` (create/start), `vagrant ssh` (log in; guest port 22 → host 2222), `vagrant halt` (shut down cleanly), `vagrant destroy` (delete VM).
- Lab machines store VMs in local `/tmp` → lost on reboot / another machine. So: keep work in `/shared`, put installs (editor, git config) in the provision block.
- Errors: "no provider" → install VirtualBox + reboot; hypervisor errors → can't run two hypervisors at once.
""",
  zh=r"""
- **Vagrant** 根据配置文件 `Vagrantfile`（Ruby 语法）管理虚拟机；它下载 **box**（磁盘镜像），交给 VirtualBox 等 **provider** 运行。
- `config.vm.box = "generic/debian12"` 选择镜像；`synced_folder ".", "/shared"` 把 Vagrantfile 所在目录共享到虚拟机的 `/shared`。
- `config.vm.provision "shell", inline: <<-SHELL … SHELL` 在首次创建时以 root 执行命令——这是一个[[here-doc]]。加 `privileged: false` 则以 `vagrant` 用户执行。
- 命令：`vagrant up`（创建/启动），`vagrant ssh`（登录；虚拟机 22 端口映射到主机 2222），`vagrant halt`（正常关机），`vagrant destroy`（删除虚拟机）。
- 实验室机器把虚拟机放在本地 `/tmp` → 重启或换机器就没了。所以：文件放 `/shared`，要装的软件（编辑器、git 配置）写进 provision。
- 报错：“no provider” → 装 VirtualBox 并重启；hypervisor 报错 → 不能同时运行两种虚拟化程序。
""",
  code=r"""
Vagrant.configure("2") do |config|
  config.vm.box = "generic/debian12"
  config.vm.synced_folder ".", "/shared"
  config.vm.provision "shell", inline: <<-SHELL
    apt-get install -y emacs-nox
  SHELL
  config.vm.provision :shell, privileged: false, inline: <<-SHELL
    git config --global user.name "YOURNAME"
  SHELL
end
""",
  see=["package-manager", "git-config", "fhs"])

S("fs", "The filesystem hierarchy", "文件系统层级")
c("fhs", "Filesystem Hierarchy Standard", "文件系统层级标准 FHS", exam=True,
  en=r"""
- One tree rooted at `/`; other filesystems are **mounted** into it (`mount` lists them).
| Dir | Holds |
|---|---|
| `/bin`, `/usr/bin` | programs (on Debian `/bin` → `usr/bin` symlink) |
| `/sbin` | system/admin programs (`fdisk`, `mkfs…`) |
| `/usr/local/bin` | software installed by the local admin |
| `/etc` | system-wide configuration (`/etc/ssh`, `/etc/passwd`) |
| `/lib` | shared libraries `.so` (Windows: `.dll`), e.g. `libc.so.6` |
| `/home/USER` | users' home dirs; root's is `/root` |
| `/tmp` | temporary files, may be RAM, not kept across reboot |
| `/var` | varying data: logs, caches, spool |
| `/dev`, `/proc`, `/sys` | virtual filesystems: devices, processes, kernel |
| `/opt` | manually installed bundles |
| `/srv`, `/run`, `/boot`, `/media` | served files, runtime state, bootloader, removable media |
- `/usr` is a historical accident (separate disks); today it is mostly read-only programs and data.
- `which ls` → where a program lives. `ls -l` colours: green executable, blue directory/link; first char `l` = symlink, `d` = directory.
- Conventions differ on macOS, BSD and WSL — know the rough layout.
""",
  zh=r"""
- 整个系统是一棵以 `/` 为根的树；其它文件系统**挂载**到树上（`mount` 可列出）。
| 目录 | 存放 |
|---|---|
| `/bin`、`/usr/bin` | 程序（Debian 上 `/bin` 是指向 `usr/bin` 的符号链接） |
| `/sbin` | 系统/管理程序（`fdisk`、`mkfs…`） |
| `/usr/local/bin` | 本地管理员自行安装的软件 |
| `/etc` | 系统级配置（`/etc/ssh`、`/etc/passwd`） |
| `/lib` | 共享库 `.so`（Windows 叫 `.dll`），如 `libc.so.6` |
| `/home/用户` | 用户家目录；root 的是 `/root` |
| `/tmp` | 临时文件，可能在内存中，重启不保留 |
| `/var` | 变化的数据：日志、缓存、队列 |
| `/dev`、`/proc`、`/sys` | 虚拟文件系统：设备、进程、内核 |
| `/opt` | 手动安装的软件包 |
| `/srv`、`/run`、`/boot`、`/media` | 对外提供的文件、运行时状态、引导、可移动介质 |
- `/usr` 是历史遗留（当年分在不同磁盘）；如今主要存放只读的程序与数据。
- `which ls` → 程序在哪。`ls -l` 颜色：绿色可执行，蓝色目录/链接；首字符 `l` 表示符号链接，`d` 表示目录。
- macOS、BSD、WSL 布局各不相同——掌握大致约定即可。
""",
  code=r"""
$ tree -L 1 /
$ which ls          # /usr/bin/ls
$ ls -l /bin        # lrwxrwxrwx ... /bin -> usr/bin
""",
  see=["everything-file", "path", "logs"])

c("everything-file", "Everything is a file", "一切皆文件",
  en=r"""
- UNIX design principle: almost every interaction with the OS looks like reading/writing a file: devices in `/dev`, processes in `/proc`, kernel state in `/sys`.
- Hence access control is traditionally done with **file permissions** ([[unix-dac]]). Exceptions exist (directories behave specially, daemons, some kernel structures).
""",
  zh=r"""
- UNIX 设计原则：与操作系统的几乎所有交互都表现为读写文件：设备在 `/dev`，进程在 `/proc`，内核状态在 `/sys`。
- 因此访问控制传统上通过**文件权限**实现（[[unix-dac]]）。也有例外（目录的语义特殊、守护进程、某些内核结构）。
""",
  see=["fhs", "unix-dac", "streams"])

S("pkg", "Software & privileges", "软件安装与特权")
c("package-manager", "Package managers & apt", "包管理器与 apt", exam=True,
  en=r"""
- Ways to install software: compile (`./configure; make; make install`), download prebuilt (put it in `/opt` if you must), or let the OS **package manager** do it.
- **Repository** = collection of packages; **package** = software + metadata + **dependencies**. Package manager downloads, installs dependencies, updates.
- Debian: `apt` (repos listed in `/etc/apt/sources.list`). RPM distros: `dnf`. macOS: `brew` (not from Apple, recommended).
| Command | Does |
|---|---|
| `apt search 'common lisp'` | search package index |
| `apt info PKG` | details |
| `sudo apt install PKG` | install + dependencies |
| `sudo apt remove PKG` | uninstall |
| `sudo apt update` | fetch the new package **list** |
| `sudo apt upgrade` | upgrade installed packages to latest in the list |
- Installing needs root: without sudo you get "Could not open lock file … Permission denied … are you root?".
- Pick variants carefully: `emacs-nox` = console-only, avoids pulling in a whole GUI.
""",
  zh=r"""
- 安装软件的方式：源码编译（`./configure; make; make install`）、下载预编译版（非要这样就放 `/opt`），或交给系统的**包管理器**。
- **软件源（repository）** = 软件包集合；**软件包** = 软件 + 元数据 + **依赖**。包管理器负责下载、装依赖、更新。
- Debian：`apt`（源列在 `/etc/apt/sources.list`）。RPM 系发行版：`dnf`。macOS：`brew`（非苹果官方，推荐）。
| 命令 | 作用 |
|---|---|
| `apt search 'common lisp'` | 搜索包索引 |
| `apt info 包名` | 查看详情 |
| `sudo apt install 包名` | 安装（含依赖） |
| `sudo apt remove 包名` | 卸载 |
| `sudo apt update` | 拉取新的软件包**列表** |
| `sudo apt upgrade` | 把已装的包升级到列表里的最新版 |
- 安装需要 root：不加 sudo 会报 “Could not open lock file … Permission denied … are you root?”。
- 注意选对版本：`emacs-nox` 是纯终端版，避免装上整套图形界面。
""",
  code=r"""
$ apt install sbcl            # fails: permission denied
$ sudo !!                     # !! = the whole previous command
sudo apt install sbcl
""",
  see=["sudo-root", "vagrant", "makefile"])

c("sudo-root", "root & sudo", "root 与 sudo", exam=True,
  en=r"""
- **root** (uid 0, "Charlie Root") is all-powerful. Normal users control only what they need.
- Changes that affect other users (installing/removing software, services, config in `/etc`) require root.
- `sudo CMD` = run one command as root (temporarily). Alternatives: `doas`, `pkexec`, `su -c`. `sudo su` opens a root shell.
- Why not always be root? You'll forget, break things and swear a lot. Least privilege.
- Who may use sudo is configured in `/etc/sudoers` ([[sudoers]]). Lab machines: no sudo; your VM: yes.
- Permissions don't protect against anyone who can become root.
- `!!` = previous command (`sudo !!`).
""",
  zh=r"""
- **root**（uid 0，绰号 “Charlie Root”）拥有一切权限。普通用户只能控制自己需要的东西。
- 会影响其他用户的操作（装卸软件、服务、`/etc` 中的配置）需要 root。
- `sudo 命令` = 临时以 root 身份执行一条命令。替代品：`doas`、`pkexec`、`su -c`。`sudo su` 打开 root shell。
- 为什么不一直当 root？你会忘记自己是 root，然后搞坏东西。最小权限原则。
- 谁能用 sudo 由 `/etc/sudoers` 配置（[[sudoers]]）。实验室机器上不能 sudo；自己的虚拟机可以。
- 权限挡不住任何能变成 root 的人。
- `!!` = 上一条命令（`sudo !!`）。
""",
  see=["users-groups", "special-bits", "sudoers"])

c("editors", "Console text editors", "终端文本编辑器",
  en=r"""
| Editor | Notes | Quit |
|---|---|---|
| `nano` | simple, everywhere | Ctrl-X |
| `vim` / `vi` | modal (1991 / 1976), powerful editing grammar, Git's default editor | Esc then `:q` / `ZZ` |
| `emacs` (`emacs-nox`) | Lisp-based, not installed by default | Ctrl-X Ctrl-C |
| `mcedit`, `micro`, `tilde` | friendlier alternatives | Alt-0 (mcedit) |
- Investing in vim/emacs early pays off. Set your editor: `export EDITOR=nano` (in `~/.profile` to keep it).
""",
  zh=r"""
| 编辑器 | 说明 | 退出 |
|---|---|---|
| `nano` | 简单，到处都有 | Ctrl-X |
| `vim` / `vi` | 模态编辑器（1991 / 1976），编辑语法强大，Git 默认编辑器 | Esc 后 `:q` / `ZZ` |
| `emacs`（`emacs-nox`） | 基于 Lisp，默认未安装 | Ctrl-X Ctrl-C |
| `mcedit`、`micro`、`tilde` | 更友好的替代品 | Alt-0（mcedit） |
- 早点学 vim/emacs 很值。设置默认编辑器：`export EDITOR=nano`（写进 `~/.profile` 才能保留）。
""",
  see=["git-config", "startup-files"])

S("dac", "Users, groups & permissions", "用户、组与权限")
c("users-groups", "Users & groups", "用户与组", exam=True,
  en=r"""
- Every user has a **uid** and belongs to at least one **group** (gid). Every file is owned by exactly one user and one group.
- `id` shows yours, e.g. `uid=1000(goblin) gid=1000(goblin) groups=1000(goblin),0(wheel)`.
| File | Contents |
|---|---|
| `/etc/passwd` | `name:x:uid:gid:full name,,,:home:shell` (world-readable) |
| `/etc/group` | `group:x:gid:member1,member2` |
| `/etc/shadow` | password hashes (root only) |
- Field formats: `man 5 passwd` (section 5 = file formats).
- Create/manage: `adduser`, `usermod -aG GROUP USER`, `su USER` (switch user) → see [[permissions-lab]].
""",
  zh=r"""
- 每个用户有 **uid**，且至少属于一个**组**（gid）。每个文件恰好属于一个用户和一个组。
- `id` 显示自己的身份，如 `uid=1000(goblin) gid=1000(goblin) groups=1000(goblin),0(wheel)`。
| 文件 | 内容 |
|---|---|
| `/etc/passwd` | `用户名:x:uid:gid:全名,,,:家目录:登录shell`（所有人可读） |
| `/etc/group` | `组名:x:gid:成员1,成员2` |
| `/etc/shadow` | 密码哈希（仅 root 可读） |
- 字段格式：`man 5 passwd`（第 5 节 = 文件格式）。
- 创建/管理：`adduser`、`usermod -aG 组 用户`、`su 用户`（切换用户）→ 见[[permissions-lab]]。
""",
  code=r"""
$ grep goblin /etc/passwd
goblin:*:1000:1000:Gretchen Hallett,,,:/home/goblin:/usr/local/bin/bash
$ grep wheel /etc/group
wheel:*:0:root,goblin
""",
  see=["unix-dac", "man", "sudo-root"])

c("unix-dac", "UNIX DAC: rwx permissions", "UNIX 自主访问控制：rwx 权限", exam=True,
  en=r"""
- **DAC** (discretionary access control): the owner decides. Permission to **r**ead, **w**rite, e**x**ecute is set separately for **user** (owner), **group**, **other**.
- `ls -l` mode string: type + 3 triplets. `-rwxr-x--- root wheel script.sh`: owner rwx, group r-x, others nothing → a wheel member can read and run but not write.
- Octal: r=4, w=2, x=1. `rwx`=7, `r-x`=5, `rw-`=6, `r--`=4, `---`=0. So `750` = `rwxr-x---`, `600` = `rw-------`, `644` = `rw-r--r--`.
- `chmod` changes mode (`chmod 600 f`, `chmod u+x f`, `chmod go-rwx d`); `chown` changes owner (and group: `chown user:group f`); `chgrp` changes group.
- **Directories**: `r` = list contents; `x` = enter (`cd`) / access files inside; `w` = create/delete entries.
- Access needs permission along the **whole path** ([[path-permission]]).
""",
  zh=r"""
- **DAC**（自主访问控制）：由属主决定。**读 r**、**写 w**、**执行 x** 分别对**属主（user）**、**属组（group）**、**其他人（other）**设置。
- `ls -l` 的权限串：类型 + 三组三位。`-rwxr-x--- root wheel script.sh`：属主 rwx，属组 r-x，其他人无 → wheel 组成员可读可执行、不可写。
- 八进制：r=4，w=2，x=1。`rwx`=7，`r-x`=5，`rw-`=6，`r--`=4，`---`=0。故 `750` = `rwxr-x---`，`600` = `rw-------`，`644` = `rw-r--r--`。
- `chmod` 改权限（`chmod 600 f`、`chmod u+x f`、`chmod go-rwx d`）；`chown` 改属主（也可改组：`chown 用户:组 f`）；`chgrp` 改属组。
- **目录**：`r` = 列出内容；`x` = 进入（`cd`）/访问其中文件；`w` = 创建/删除条目。
- 访问需要**整条路径**上的权限（[[path-permission]]）。
""",
  code=r"""
-rwxr-x---  root wheel my-cool-script.sh
 |\_/\_/\_/
 | |  |  └─ other: ---  (0)
 | |  └──── group: r-x  (5)
 | └─────── user : rwx  (7)    → mode 750
 └───────── type : - file, d dir, l symlink
""",
  see=["special-bits", "ssh-key-perms", "everything-file", "datalog-access-control"])

c("special-bits", "setuid, setgid & sticky bits", "setuid、setgid 与粘滞位", exam=True,
  en=r"""
| Bit | On | Effect | Shows as |
|---|---|---|---|
| setuid | executable | runs as the file's **owner**, not the caller (how `sudo`, `passwd`, `su`, `mount` work) | `-rwsr-xr-x` |
| setgid | directory | new files get the **directory's group**, not the creator's | `drwxrwsr-x` |
| sticky | directory | only root or the file/dir owner may delete (unlink) files — e.g. `/tmp` | `drwxrwxrwt` |
- Octal prefix: setuid 4, setgid 2, sticky 1 (`chmod 4755 prog`).
- Find setuid programs: `sudo find / -perm /4000`.
- Writing your own setuid program is dangerous: a bug can hand over your account ([[setuid-demo]]).
""",
  zh=r"""
| 位 | 作用对象 | 效果 | 显示 |
|---|---|---|---|
| setuid | 可执行文件 | 以文件**属主**身份运行，而非调用者（`sudo`、`passwd`、`su`、`mount` 靠它工作） | `-rwsr-xr-x` |
| setgid | 目录 | 新建文件归**目录所属组**，而非创建者的组 | `drwxrwsr-x` |
| sticky（粘滞位） | 目录 | 只有 root 或文件/目录属主能删除其中文件——如 `/tmp` | `drwxrwxrwt` |
- 八进制前缀：setuid 4，setgid 2，sticky 1（`chmod 4755 prog`）。
- 查找 setuid 程序：`sudo find / -perm /4000`。
- 自己写 setuid 程序很危险：一个 bug 就可能把你的账号交给别人（[[setuid-demo]]）。
""",
  see=["unix-dac", "sudo-root", "setuid-demo"])

S("services", "Services & logs", "服务与日志")
c("systemd", "systemd & systemctl", "systemd 与 systemctl", exam=True,
  en=r"""
- Servers (web, IRC, git, media, Minecraft…) are easier and safer when **managed by the OS** as services/daemons.
- Linux has several service managers; the usual one is **systemd** (PID 1, `/sbin/init`). Polarising: replaced shell-script init, breaks some UNIX traditions, manages ever more ("units").
| Command | Does |
|---|---|
| `systemctl status` | overview of the system / of one unit |
| `systemctl start sshd` | start now |
| `systemctl enable sshd` | start at boot |
| `systemctl enable --now sshd` | both |
| `systemctl stop / restart` | stop / restart |
- Unit files (e.g. `/etc/systemd/system/sshd.service`): `[Unit]` (Description, After=), `[Service]` (ExecStart=, ExecReload=, Restart=on-failure, Type=), `[Install]` (WantedBy=multi-user.target).
""",
  zh=r"""
- 服务器程序（网页、IRC、git、媒体、Minecraft……）交给**操作系统管理**为服务/守护进程，更方便也更安全。
- Linux 有多种服务管理器；最常见的是 **systemd**（PID 1，`/sbin/init`）。争议很大：取代了 shell 脚本式的 init，打破部分 UNIX 传统，管的东西越来越多（“unit”）。
| 命令 | 作用 |
|---|---|
| `systemctl status` | 系统 / 某个 unit 的概况 |
| `systemctl start sshd` | 立即启动 |
| `systemctl enable sshd` | 开机自启 |
| `systemctl enable --now sshd` | 两者都做 |
| `systemctl stop / restart` | 停止 / 重启 |
- unit 文件（如 `/etc/systemd/system/sshd.service`）：`[Unit]`（Description、After=）、`[Service]`（ExecStart=、ExecReload=、Restart=on-failure、Type=）、`[Install]`（WantedBy=multi-user.target）。
""",
  code=r"""
[Unit]
Description=OpenBSD Secure Shell server
After=network.target
[Service]
ExecStartPre=/usr/sbin/sshd -t
ExecStart=/usr/sbin/sshd -D $SSHD_OPTS
Restart=on-failure
[Install]
WantedBy=multi-user.target
""",
  see=["logs", "ssh"])

c("logs", "Logs: journalctl & dmesg", "日志：journalctl 与 dmesg", exam=True,
  en=r"""
- `journalctl -n 3` last 3 system log entries; `-u sshd` one unit; `--since '10min ago'`; `--boot` since boot.
- `systemctl status sshd` also shows the latest log lines for that unit.
- Traditional text logs live in `/var/log/` (`grep -R sshd /var/log/`).
- `sudo dmesg -H` = the **kernel's** log (hardware, drivers, boot) — when you're still stuck.
""",
  zh=r"""
- `journalctl -n 3` 最近 3 条系统日志；`-u sshd` 只看某个 unit；`--since '10min ago'`；`--boot` 本次开机以来。
- `systemctl status sshd` 也会显示该 unit 最近几行日志。
- 传统文本日志在 `/var/log/`（`grep -R sshd /var/log/`）。
- `sudo dmesg -H` = **内核**日志（硬件、驱动、启动）——实在没头绪时看。
""",
  see=["systemd", "fhs"])

for n, e, z, k in [
    ("ls -l -a -h", "long listing, include hidden, human sizes", "详细列表、含隐藏文件、易读大小", "command-anatomy"),
    ("man / man -k / apropos", "read / search the manual", "阅读 / 搜索手册", "man"),
    ("whoami, hostname, uname -a, id", "who/where am I", "我是谁、在哪台机器", "users-groups"),
    ("ssh USER@HOST", "remote login (TCP 22)", "远程登录（TCP 22）", "ssh"),
    ("ssh -X", "forward X11 GUI", "转发图形界面", "ssh"),
    ("ssh -v", "verbose debug output", "调试输出", "ssh"),
    ("ssh-keygen -t ed25519", "create a key pair", "生成密钥对", "ssh-keys"),
    ("ssh-keyscan -t ed25519 HOST", "print a host's public key", "打印主机公钥", "host-key"),
    ("scp SRC HOST:PATH", "copy over SSH", "经 SSH 复制文件", "scp"),
    ("vagrant up / ssh / halt / destroy", "start / log in / stop / delete VM", "启动 / 登录 / 关机 / 删除虚拟机", "vagrant"),
    ("tree -L 1 /", "show directory tree", "显示目录树", "fhs"),
    ("which CMD", "where is a program", "程序位置", "fhs"),
    ("mount", "list mounted filesystems", "列出已挂载文件系统", "fhs"),
    ("apt search/info/install/remove", "find & manage packages", "查找与管理软件包", "package-manager"),
    ("apt update / apt upgrade", "refresh list / upgrade installed", "刷新列表 / 升级已装", "package-manager"),
    ("sudo CMD, sudo !!", "run as root; repeat last cmd as root", "以 root 执行；以 root 重复上一条", "sudo-root"),
    ("chmod MODE F", "change permissions (600, u+x, go-w)", "修改权限", "unix-dac"),
    ("chown USER[:GROUP] F, chgrp", "change owner / group", "修改属主 / 属组", "unix-dac"),
    ("systemctl status/start/enable --now", "manage services", "管理服务", "systemd"),
    ("journalctl -n -u --since --boot", "read system logs", "查看系统日志", "logs"),
    ("dmesg -H", "kernel log", "内核日志", "logs"),
]:
    cmd(n, e, z, k)

# =====================================================================  W2
W(2)
S("think", "Thinking in commands", "命令思维")
c("cmd-groups", "Three kinds of command", "命令的三类",
  en=r"""
- Commands that **get information** (`ls`, `find`, `ps`, `cat`), commands that **filter information** (`grep`, `sort`, `head`, `cut`), commands that **do stuff** (`rm`, `mv`, `sed -i`). Some do all three.
- Shell work = chain getters → filters → doers with [[pipes]], loops and [[command-substitution]].
- Example task from the lecture: find all markdown files, find which mention "Joseph", replace with "Gretchen" — built up step by step (see [[find-xargs]]).
- Learning the shell takes practice: switch to it entirely for a month.
""",
  zh=r"""
- **获取信息**的命令（`ls`、`find`、`ps`、`cat`），**过滤信息**的命令（`grep`、`sort`、`head`、`cut`），**执行操作**的命令（`rm`、`mv`、`sed -i`）。有的三者兼备。
- shell 工作 = 用[[pipes]]、循环和[[command-substitution]]把 获取 → 过滤 → 执行 串起来。
- 讲座例子：找出所有 markdown 文件，找出提到 “Joseph” 的，替换成 “Gretchen”——一步步搭建（见[[find-xargs]]）。
- 学 shell 需要练：坚持全用 shell 一个月。
""",
  see=["pipes", "filters", "unix-philosophy"])

S("expansion", "How the shell reads a line", "Shell 如何解析一行命令")
c("shell-expansion", "Shell expansion order", "Shell 展开顺序", exam=True,
  en=r"""
- The shell, not the program, rewrites your line **before** running it. Roughly: `~` and variables `$x` → command substitution `$( )` → **word splitting** on whitespace → **glob** (pathname) expansion → quote removal → run with argv.
- The program only sees the final list of arguments (`argv[0]` = program name).
- Lab tool `arguments.c` prints each argument in brackets — the best way to see what the shell did.
""",
  zh=r"""
- 改写命令行的是 shell，不是程序，并且发生在**执行之前**。大致顺序：`~` 与变量 `$x` → 命令替换 `$( )` → 按空白**分词** → **通配符**（路径名）展开 → 去掉引号 → 以 argv 形式运行。
- 程序只看到最终的参数列表（`argv[0]` = 程序名）。
- 实验工具 `arguments.c` 用方括号打印每个参数——最直观地看出 shell 做了什么。
""",
  code=r"""
#include <stdio.h>
int main(int argc, char** argv) {
  for (int i = 0; i < argc; i++)
    printf("Argument #%i: [%s]\n", i, argv[i]);
  return 0;
}
/* gcc -Wall arguments.c -o arguments */
""",
  see=["word-splitting", "globbing", "quoting", "variables", "command-substitution"])

c("word-splitting", "Whitespace & word splitting", "空白与分词", exam=True,
  en=r"""
- Unquoted whitespace separates arguments; runs of spaces count as one separator: `./arguments one     two` → 2 args.
- Quotes keep spaces inside one argument: `./arguments "one     two"` → 1 arg, spaces preserved.
- `IFS` controls the separator characters for splitting (e.g. in `for` loops over `$(…)`).
""",
  zh=r"""
- 未加引号的空白分隔参数；连续多个空格算一个分隔：`./arguments one     two` → 2 个参数。
- 引号让空格留在同一个参数里：`./arguments "one     two"` → 1 个参数，空格保留。
- `IFS` 决定分词用哪些分隔字符（如对 `$(…)` 结果做 `for` 循环时）。
""",
  code=r"""
$ ./arguments one     two
Argument #0: [./arguments]
Argument #1: [one]
Argument #2: [two]
$ ./arguments "one     two"
Argument #1: [one     two]
""",
  see=["quoting", "shell-expansion"])

c("globbing", "Globbing (pattern matching)", "通配符（路径名展开）", exam=True,
  en=r"""
| Pattern | Matches filenames |
|---|---|
| `*` | any string (not leading `.`) |
| `?` | any one character |
| `[abc]`, `[a-z]` | one character from the set |
| `**` | recursive in bash with `globstar` / in zsh |
- Expanded by the shell into matching file names, sorted. `./arguments *` lists the files in the directory.
- **No match → the pattern is passed literally** (in an empty dir, `../arguments *` prints `[*]`).
- Ways to pass a literal `*`: `\*`, `'*'`, `"*"` (or run it where nothing matches).
- Globs are not regexes: `*` here ≠ regex `*` ([[regex-quantifiers]]).
""",
  zh=r"""
| 模式 | 匹配的文件名 |
|---|---|
| `*` | 任意字符串（不含开头的 `.`） |
| `?` | 任意一个字符 |
| `[abc]`、`[a-z]` | 集合中的一个字符 |
| `**` | bash 开启 `globstar` 或 zsh 中可递归匹配 |
- 由 shell 展开为匹配到的文件名（排序后）。`./arguments *` 会列出目录中的文件。
- **无匹配时模式原样传入**（空目录里 `../arguments *` 打印 `[*]`）。
- 传入字面 `*` 的方法：`\*`、`'*'`、`"*"`（或在没有可匹配文件的地方运行）。
- 通配符不是正则：这里的 `*` ≠ 正则的 `*`（[[regex-quantifiers]]）。
""",
  see=["quoting", "find-xargs", "regex-quantifiers"])

c("quoting", "Quoting & escaping", "引号与转义", exam=True,
  en=r"""
| Form | Effect |
|---|---|
| `'…'` single quotes | everything literal: no `$`, no globs, no splitting |
| `"…"` double quotes | no splitting/globs, but `$var` and `$( )` still expand |
| `\x` backslash | escape one character (`\*`, `\ `, `\$`) |
- Files with spaces: `touch "silly named file"`; without quotes you create 3 files. `rm "silly named file"`, `rm silly\ named\ file`, or use Tab completion (inserts the escapes).
- Regexes passed to grep/sed are usually single-quoted so the shell leaves `$`, `*`, `\` alone ([[grep]]).
""",
  zh=r"""
| 形式 | 效果 |
|---|---|
| `'…'` 单引号 | 全部按字面：不展开 `$`、不通配、不分词 |
| `"…"` 双引号 | 不分词、不通配，但 `$var` 和 `$( )` 仍会展开 |
| `\x` 反斜杠 | 转义一个字符（`\*`、`\ `、`\$`） |
- 带空格的文件名：`touch "silly named file"`；不加引号会建出 3 个文件。删除：`rm "silly named file"`、`rm silly\ named\ file`，或用 Tab 补全（自动加转义）。
- 传给 grep/sed 的正则通常用单引号括起来，让 shell 不碰 `$`、`*`、`\`（[[grep]]）。
""",
  see=["word-splitting", "variables", "globbing"])

c("variables", "Shell variables", "Shell 变量", exam=True,
  en=r"""
- Set: `x=5` (**no spaces** around `=`; value is the string "5"). Get: `$x` or `${x}` (braces needed inside words: `${a}b` vs `$ab`).
- **Always double-quote** expansions: `gcc -Wall "$p.c" -o "$p"` works even if `p="silly name"`.
- `program=silly name` = set program=silly **then run** `name`. Quote values with spaces.
- `VAR=value cmd` sets VAR only in cmd's environment — but `file=x gcc "$file.c"` fails: `$file` was expanded before the assignment took effect.
- Unset variables expand to empty string (dangerous: `rm -rf "$FOLDER/"`) → `set -u` ([[strict-mode]]) or `${x:?x is not defined}`.
- `export VAR` makes it an **environment variable** inherited by child processes; `env` lists them (`PATH`, `HOME`, `EDITOR`…).
""",
  zh=r"""
- 赋值：`x=5`（`=` 两边**不能有空格**；值是字符串 "5"）。取值：`$x` 或 `${x}`（在单词中间需要花括号：`${a}b` 与 `$ab` 不同）。
- **始终加双引号**：`gcc -Wall "$p.c" -o "$p"` 即使 `p="silly name"` 也正确。
- `program=silly name` = 先设 program=silly，**再执行** `name`。含空格的值要加引号。
- `VAR=值 命令` 只在该命令的环境中设置 VAR——但 `file=x gcc "$file.c"` 不行：`$file` 在赋值生效前就已被展开。
- 未设置的变量展开为空字符串（危险：`rm -rf "$FOLDER/"`）→ 用 `set -u`（[[strict-mode]]）或 `${x:?x is not defined}`。
- `export VAR` 使其成为**环境变量**，被子进程继承；`env` 列出全部（`PATH`、`HOME`、`EDITOR`……）。
""",
  code=r"""
p=arguments
gcc -Wall "$p.c" -o "$p"
files="$(ls *.md)"
echo "${x:?x is not defined}"
""",
  see=["quoting", "path", "strict-mode", "command-substitution"])

c("command-substitution", "Command substitution $( )", "命令替换 $( )", exam=True,
  en=r"""
- `$(cmd)` runs cmd and **splices** its standard output into the command line (old form: backticks `` `cmd` ``).
- Unquoted, the result is word-split (one argument per word/line); quoted `"$(cmd)"` keeps it as one argument.
- Typical: `for f in $(find . -name \*.md); do …; done`, `n=$(wc -l < file)`.
""",
  zh=r"""
- `$(命令)` 运行命令，并把其标准输出**拼接**进命令行（旧写法：反引号 `` `命令` ``）。
- 不加引号时结果会被分词（每个词/行一个参数）；加引号 `"$(命令)"` 则作为一个参数。
- 常见用法：`for f in $(find . -name \*.md); do …; done`、`n=$(wc -l < file)`。
""",
  see=["control-flow", "find-xargs", "pipes"])

S("pipes", "Streams, pipes & redirection", "流、管道与重定向")
c("streams", "Standard streams", "标准流", exam=True,
  en=r"""
| fd | Name | Default |
|---|---|---|
| 0 | stdin | keyboard |
| 1 | stdout | terminal |
| 2 | stderr | terminal (errors, warnings) |
- Programs read stdin and write stdout, so they can be connected. Errors go to stderr so they don't pollute a pipe.
- Ctrl-D at the start of a line = end of input (EOF).
""",
  zh=r"""
| 文件描述符 | 名称 | 默认 |
|---|---|---|
| 0 | stdin 标准输入 | 键盘 |
| 1 | stdout 标准输出 | 终端 |
| 2 | stderr 标准错误 | 终端（错误、警告） |
- 程序读 stdin、写 stdout，因此可以互相连接。错误写到 stderr，不会混进管道数据。
- 行首按 Ctrl-D = 输入结束（EOF）。
""",
  see=["pipes", "redirection", "everything-file"])

c("pipes", "Pipes |", "管道 |", exam=True,
  en=r"""
- `a | b` connects a's **stdout** to b's **stdin**; both run at the same time. The basis of composing small tools ([[unix-philosophy]]).
- Exit status of a pipeline = that of the **last** command (unless `set -o pipefail`).
- Only stdout goes through the pipe; send stderr too with `a 2>&1 | b`.
""",
  zh=r"""
- `a | b` 把 a 的 **stdout** 接到 b 的 **stdin**；两者同时运行。这是组合小工具的基础（[[unix-philosophy]]）。
- 管道的退出状态 = **最后一个**命令的退出状态（除非 `set -o pipefail`）。
- 只有 stdout 进管道；要连 stderr 一起：`a 2>&1 | b`。
""",
  code=r"""
ls ./** | tr '\t' '\n' | grep '.md' | wc -l
""",
  see=["streams", "filters", "strict-mode", "redirection"])

c("redirection", "Redirection", "重定向", exam=True,
  en=r"""
| Syntax | Meaning |
|---|---|
| `cmd > f` | stdout to file f (truncate/overwrite) |
| `cmd >> f` | append stdout to f |
| `cmd < f` | stdin from f |
| `cmd 2> f` | stderr to f |
| `cmd > f 2>&1` | stdout and stderr to f (order matters) |
| `1>&2 echo msg` / `echo msg >&2` | write to stderr |
| `cmd <<< "text"` | here-string: text as stdin |
| `cmd << EOF … EOF` | [[here-doc]]: following lines as stdin |
| `cmd <(other)` | process substitution: other's output as a file name |
| `-` as a file name | many tools: read stdin |
- Lab: `ls -l > tmp`, then compare with the live listing: `ls -l | diff tmp -` or `diff tmp <(ls -l)`; log with `> difflog`, then `>> difflog`.
""",
  zh=r"""
| 语法 | 含义 |
|---|---|
| `cmd > f` | stdout 写入文件 f（清空/覆盖） |
| `cmd >> f` | stdout 追加到 f |
| `cmd < f` | stdin 来自 f |
| `cmd 2> f` | stderr 写入 f |
| `cmd > f 2>&1` | stdout 和 stderr 都写入 f（顺序有关系） |
| `1>&2 echo msg` / `echo msg >&2` | 写到 stderr |
| `cmd <<< "文本"` | here-string：文本作为 stdin |
| `cmd << EOF … EOF` | [[here-doc]]：后续几行作为 stdin |
| `cmd <(other)` | 进程替换：把 other 的输出当作一个文件名 |
| 文件名写 `-` | 很多工具表示读 stdin |
- 实验：`ls -l > tmp`，再与当前列表比较：`ls -l | diff tmp -` 或 `diff tmp <(ls -l)`；记录用 `> difflog`，再次用 `>> difflog` 追加。
""",
  see=["streams", "pipes", "here-doc", "ssh-keys"])

c("here-doc", "Here documents & here-strings", "Here 文档与 here-string",
  en=r"""
- **Here document** `<<WORD … WORD`: multi-line literal text fed as stdin, ending at a line containing only WORD (arbitrary keyword, often `EOF`). `<<-` allows indented terminator. Same idea appears in Ruby (Vagrantfile `<<-SHELL`).
- **Here-string** `<<< "text"`: one string as stdin. Used in the crackme lab: `./crackme-1 <<< 'guess'`.
""",
  zh=r"""
- **Here 文档** `<<WORD … WORD`：把多行字面文本作为 stdin，直到某行只有 WORD 为止（关键字任意，常用 `EOF`）。`<<-` 允许结束符缩进。Ruby 里也有同样写法（Vagrantfile 的 `<<-SHELL`）。
- **Here-string** `<<< "文本"`：把一个字符串作为 stdin。crackme 实验里用：`./crackme-1 <<< '猜测'`。
""",
  code=r"""
cat <<EOF > hello.txt
line one
line two
EOF
wc -l <<< "$matches"
""",
  see=["vagrant", "crackme", "redirection"])

c("filters", "Filter commands", "过滤类命令", exam=True,
  en=r"""
| Command | Does |
|---|---|
| `cat [F…]` | concatenate files to stdout (no args: copy stdin) |
| `head -n N` | first N lines (default 10); `-n -2` = all but last 2 |
| `tail -n N` | last N lines; `-n +N` = from line N on |
| `sort` (`-r`, `-n`, `-u`) | sort lines (reads everything first) |
| `uniq` (`-c`) | drop **adjacent** duplicate lines → usually `sort \| uniq` |
| `wc -l` (`-w`, `-c`) | count lines (words, bytes) |
| `tr 'a-z' 'A-Z'`, `tr '\t' '\n'` | translate characters |
| `cut -d: -f1` | pick fields / characters |
| `tee F` | copy stdin to F *and* stdout |
| `column -ts,` | align into a table |
- All also accept file names: `head Readme.txt` = `cat Readme.txt | head`.
- Word list exercises (`/usr/share/dict/words`): first word `head -n 1`, last `tail -n 1`, count `wc -l`, 6171st `head -n 6171 | tail -n 1`, first 5 of last 100 `tail -n 100 | head -n 5`, last 10 reversed `tail -n 10 | sort -r`.
""",
  zh=r"""
| 命令 | 作用 |
|---|---|
| `cat [文件…]` | 把文件内容连接输出（无参数则复制 stdin） |
| `head -n N` | 前 N 行（默认 10）；`-n -2` = 除最后 2 行外全部 |
| `tail -n N` | 后 N 行；`-n +N` = 从第 N 行开始 |
| `sort`（`-r`、`-n`、`-u`） | 排序（先读完全部输入） |
| `uniq`（`-c`） | 去掉**相邻**重复行 → 通常先 `sort` 再 `uniq` |
| `wc -l`（`-w`、`-c`） | 统计行数（词数、字节数） |
| `tr 'a-z' 'A-Z'`、`tr '\t' '\n'` | 字符转换 |
| `cut -d: -f1` | 取字段 / 字符 |
| `tee F` | stdin 同时写到 F *和* stdout |
| `column -ts,` | 对齐成表格 |
- 都可直接接文件名：`head Readme.txt` = `cat Readme.txt | head`。
- 单词表练习（`/usr/share/dict/words`）：第一个词 `head -n 1`，最后一个 `tail -n 1`，总数 `wc -l`，第 6171 个 `head -n 6171 | tail -n 1`，最后 100 个里的前 5 个 `tail -n 100 | head -n 5`，最后 10 个倒序 `tail -n 10 | sort -r`。
""",
  see=["pipes", "grep", "awk"])

c("find-xargs", "find, -exec & xargs", "find、-exec 与 xargs",
  en=r"""
- `find DIR -name '*.md'` lists matching files recursively (quote/escape the glob so the shell doesn't expand it first).
- `-exec CMD {} \;` runs CMD once per file; `-exec CMD {} \+` runs it once with many files.
- `xargs` turns stdin lines into arguments: `find . -name '*.md' | xargs grep -l Joseph`.
- Lecture progression: `for f in $(find …); do grep -iH joseph "$f"; done` → `sed -i` on the matches → one-liner `find . -name \*.md -exec sed -i 's/Joseph/Gretchen/g' {} \+` → wrap in a [[shell-functions|function]].
""",
  zh=r"""
- `find 目录 -name '*.md'` 递归列出匹配文件（通配符要加引号/转义，免得 shell 先展开）。
- `-exec 命令 {} \;` 每个文件执行一次；`-exec 命令 {} \+` 把多个文件一次性传给命令。
- `xargs` 把 stdin 的各行变成参数：`find . -name '*.md' | xargs grep -l Joseph`。
- 讲座推进：`for f in $(find …); do grep -iH joseph "$f"; done` → 对匹配文件 `sed -i` → 一行 `find . -name \*.md -exec sed -i 's/Joseph/Gretchen/g' {} \+` → 包装成[[shell-functions|函数]]。
""",
  code=r"""
for f in $(find . -name \*.md); do
  grep -iH joseph "${f}"
done
find . -name \*.md -exec sed -ie 's/Joseph/Gretchen/g' {} \+
""",
  see=["sed", "command-substitution", "control-flow"])

S("scripts", "Shell scripting", "Shell 脚本")
c("control-flow", "Loops, tests & exit status", "循环、条件与退出状态", exam=True,
  en=r"""
- Loops and ifs are **shell builtins** with funky syntax: `for v in 1 2 3; do …; done`, `for v in $(seq 1 3)`, `while …; do …; done`, `case "$1" in a) …;; *) …;; esac`.
- Every command returns an **exit status**: 0 = success, non-zero = failure. `$?` holds the last one.
- `if` runs a command and branches on its status: `if test "$x" -gt 3; then …; fi`. `[ … ]` is the same as `test`; `[[ … ]]` is a bash builtin with nicer rules.
- Tests: `-gt -lt -eq -ne` numbers; `=` `!=` strings; `-z` empty string; `-f` file exists; `-d` directory; `!` not.
- `a && b` run b only if a succeeded; `a || b` run b only if a failed (`cmd || echo "This has all gone wrong!"`).
""",
  zh=r"""
- 循环和条件是语法古怪的 **shell 内建命令**：`for v in 1 2 3; do …; done`、`for v in $(seq 1 3)`、`while …; do …; done`、`case "$1" in a) …;; *) …;; esac`。
- 每个命令都返回**退出状态**：0 = 成功，非 0 = 失败。`$?` 保存上一个命令的状态。
- `if` 执行一个命令并根据其状态分支：`if test "$x" -gt 3; then …; fi`。`[ … ]` 等同 `test`；`[[ … ]]` 是 bash 内建，规则更友好。
- 判断：数字 `-gt -lt -eq -ne`；字符串 `=` `!=`；`-z` 空串；`-f` 文件存在；`-d` 是目录；`!` 取反。
- `a && b` a 成功才执行 b；`a || b` a 失败才执行 b（`cmd || echo "This has all gone wrong!"`）。
""",
  code=r"""
x=5
if [ "${x}" -gt 3 ]; then echo 'x > 3'; fi
[[ "${x}" -gt 3 ]] && echo still true
for var in $(seq 1 3); do echo "$var"; done
""",
  see=["shell-script", "strict-mode", "git-hooks", "b-script"])

c("shell-functions", "Shell functions", "Shell 函数",
  en=r"""
- Define: `name() { commands; }`; call like a command; arguments arrive as `$1 $2 … $@`.
- Can override commands: `cp() { /bin/cp -a "$@"; }` (call the real one by full path).
- Defined functions vanish with the shell → put them in a [[startup-files|startup file]].
""",
  zh=r"""
- 定义：`name() { commands; }`；像命令一样调用；参数为 `$1 $2 … $@`。
- 可以覆盖已有命令：`cp() { /bin/cp -a "$@"; }`（用完整路径调用真正的 cp）。
- 函数随 shell 退出而消失 → 写进[[startup-files|启动文件]]。
""",
  code=r"""
transition() {
  find . -name \*.md -exec sed -ie 's/Joseph/Gretchen/g' {} \+;
}
""",
  see=["startup-files", "find-xargs"])

c("startup-files", "Startup files: .profile, .bashrc", "启动文件：.profile、.bashrc",
  en=r"""
- The shell reads startup files every time it starts: `~/.profile` (POSIX login shells), `~/.bash_profile` / `~/.bashrc` (bash), `~/.zshrc` (zsh), `~/.kshrc` (ksh, OpenBSD).
- Put lasting functions, aliases and `export`s there (e.g. `export EDITOR=nano`, `export PATH="$PATH:$HOME/.local/bin"`).
- Reload without restarting: `source ~/.profile` (or `. ~/.profile`).
""",
  zh=r"""
- shell 每次启动都会读启动文件：`~/.profile`（POSIX 登录 shell）、`~/.bash_profile` / `~/.bashrc`（bash）、`~/.zshrc`（zsh）、`~/.kshrc`（ksh，OpenBSD）。
- 需要长期保留的函数、别名、`export` 写在这里（如 `export EDITOR=nano`、`export PATH="$PATH:$HOME/.local/bin"`）。
- 不重启而重新加载：`source ~/.profile`（或 `. ~/.profile`）。
""",
  see=["path", "shell-functions", "editors"])

c("shell-script", "Shell scripts & the shebang", "Shell 脚本与 shebang", exam=True,
  en=r"""
- Executing a file: compiled **ELF** binaries go to the dynamic linker (`ld-linux.so`) to load libraries; a text file starting with `#!` (**shebang**) is run by the interpreter named on that line.
- `#!/bin/sh` portable POSIX shell; `#!/usr/bin/env bash` / `#!/usr/bin/env python3` finds the interpreter via PATH (portable across systems).
- Make it executable: `chmod +x myscript`; run `./myscript` or install on [[path]].
- Inside: `$0` script name, `$1 … $9` positional args, `$#` count, `$@` all args, `$?` last status, `exit N` set status.
- Error messages go to stderr: `1>&2 echo "[WARNING]"`.
""",
  zh=r"""
- 执行一个文件时：编译出的 **ELF** 二进制交给动态链接器（`ld-linux.so`）加载库；以 `#!`（**shebang**）开头的文本文件则交给该行指定的解释器运行。
- `#!/bin/sh` 可移植的 POSIX shell；`#!/usr/bin/env bash` / `#!/usr/bin/env python3` 通过 PATH 找解释器（跨系统可移植）。
- 赋予执行权限：`chmod +x myscript`；用 `./myscript` 运行，或装到[[path]]上。
- 脚本内：`$0` 脚本名，`$1 … $9` 位置参数，`$#` 参数个数，`$@` 全部参数，`$?` 上一个状态，`exit N` 设置退出状态。
- 错误信息写到 stderr：`1>&2 echo "[WARNING]"`。
""",
  code=r"""
#!/usr/bin/env bash
echo "The program's name is ${0} and the arguments passed are ${@}!"
if [[ ! -z "${masochist}" ]]; then
  1>&2 echo "[WARNING]: Advanced!"
fi
""",
  see=["path", "unix-dac", "strict-mode", "b-script", "git-hooks"])

c("path", "PATH", "PATH 环境变量", exam=True,
  en=r"""
- `$PATH` = colon-separated list of directories searched for commands. **First match wins.**
- Add your own: `export PATH="$PATH:$HOME/.local/bin"` in `~/.profile`, copy scripts there.
- Don't add `.` or prepend your folder before system ones: someone can plant a fake `ls` (trolling / vulnerabilities). To change a system program, override in `~/.profile` instead.
- `which CMD` shows which one wins.
""",
  zh=r"""
- `$PATH` = 用冒号分隔的目录列表，shell 在其中查找命令。**取第一个匹配。**
- 加入自己的目录：在 `~/.profile` 中 `export PATH="$PATH:$HOME/.local/bin"`，把脚本放进去。
- 别把 `.` 加进 PATH，也别把自己的目录放在系统目录前面：别人可能放一个假的 `ls`（恶作剧/漏洞）。想改系统程序的行为，在 `~/.profile` 里覆盖即可。
- `which 命令` 显示最终用的是哪个。
""",
  see=["startup-files", "fhs", "variables"])

c("strict-mode", "Strict mode: set -euo pipefail", "严格模式：set -euo pipefail", exam=True,
  en=r"""
| Option | Effect |
|---|---|
| `set -e` | exit the script on the first failing command |
| `set -u` | using an undefined variable is an error (protects `rm -rf "$FOLDER/"`) |
| `set -o pipefail` | a pipeline fails if **any** command in it fails, not just the last |
- Like `-Werror` for C. Allow an expected failure explicitly: `cmd || true`, or handle it: `cmd || echo "gone wrong"`.
- pipefail example: `false | sort` returns 0 without it (sort succeeded); `grep x missing.txt | wc -l` prints 0 and "succeeds".
""",
  zh=r"""
| 选项 | 效果 |
|---|---|
| `set -e` | 任何命令失败就退出脚本 |
| `set -u` | 使用未定义变量即报错（防止 `rm -rf "$FOLDER/"` 酿成大祸） |
| `set -o pipefail` | 管道中**任一**命令失败则整个管道失败，而不只看最后一个 |
- 相当于 C 的 `-Werror`。允许的失败要显式写：`cmd || true`，或处理：`cmd || echo "gone wrong"`。
- pipefail 例子：没有它时 `false | sort` 返回 0（sort 成功了）；`grep x missing.txt | wc -l` 打印 0 并“成功”。
""",
  see=["control-flow", "pipes", "variables"])

c("b-script", "Lab: the build helper ./b", "实验：构建助手 ./b",
  en=r"""
- Spec: POSIX sh script `b`, executable. `./b compile NAME` → `gcc -Wall -std=c11 -g NAME.c -o NAME`; accepts `hello` or `hello.c`; missing source → error message + non-zero exit, don't call gcc.
- `./b run NAME` runs `./NAME` (error if missing); `./b build NAME` compiles, and runs only if compile succeeded; no/unknown command → usage text.
- Practises: positional args, `case`, string trimming `${1%.c}`, tests `-f`, `&&`, exit codes. Real projects use [[makefile|make]] for this.
""",
  zh=r"""
- 要求：POSIX sh 脚本 `b`，可执行。`./b compile NAME` → `gcc -Wall -std=c11 -g NAME.c -o NAME`；接受 `hello` 或 `hello.c`；源文件不存在 → 输出错误并以非 0 退出，不调用 gcc。
- `./b run NAME` 运行 `./NAME`（不存在则报错）；`./b build NAME` 先编译，成功才运行；无命令/未知命令 → 打印用法。
- 练习点：位置参数、`case`、字符串截取 `${1%.c}`、`-f` 测试、`&&`、退出码。真实项目用[[makefile|make]]完成这类工作。
""",
  code=r"""
#!/bin/sh
usage() { echo "usage: $0 compile|run|build NAME" >&2; exit 1; }
[ $# -eq 2 ] || usage
name="${2%.c}"
compile() { [ -f "$name.c" ] || { echo "no $name.c" >&2; exit 2; }
            gcc -Wall -std=c11 -g "$name.c" -o "$name"; }
run()     { [ -x "$name" ] || { echo "no ./$name" >&2; exit 3; }; "./$name"; }
case "$1" in
  compile) compile ;;
  run)     run ;;
  build)   compile && run ;;
  *)       usage ;;
esac
""",
  see=["shell-script", "control-flow", "makefile"])

S("jobs", "Job control", "作业控制")
c("job-control", "Background jobs & signals", "后台作业与信号", exam=True,
  en=r"""
| Key / command | Effect |
|---|---|
| `cmd &` | run in the background |
| Ctrl-Z | suspend (stop) the foreground job, back to the shell |
| `fg` / `bg` | resume in foreground / background |
| `jobs` | list jobs; `wait` waits for all background jobs |
| Ctrl-C | interrupt (kill) the foreground command (SIGINT) |
| Ctrl-D | end of input (EOF) — not a signal |
| `kill PID` / `kill %1` | send a signal (default TERM); `kill -9` = KILL |
| Ctrl-T | status of the running program (few systems support it) |
- `ps` / `ps aux` lists processes and their PIDs. If something has really hung: Ctrl-Z, then `kill`.
""",
  zh=r"""
| 按键 / 命令 | 作用 |
|---|---|
| `cmd &` | 在后台运行 |
| Ctrl-Z | 挂起（暂停）前台作业，回到 shell |
| `fg` / `bg` | 在前台 / 后台继续 |
| `jobs` | 列出作业；`wait` 等待全部后台作业结束 |
| Ctrl-C | 中断（结束）前台命令（SIGINT） |
| Ctrl-D | 输入结束（EOF）——不是信号 |
| `kill PID` / `kill %1` | 发送信号（默认 TERM）；`kill -9` = KILL |
| Ctrl-T | 显示正在运行程序的状态（少数系统支持） |
- `ps` / `ps aux` 列出进程及 PID。程序真卡死时：Ctrl-Z，再 `kill`。
""",
  see=["strace", "streams"])

S("permlab", "Permissions in practice (lab)", "权限实操（实验）")
c("permissions-lab", "Users, groups & a shared home (lab)", "用户、组与共享家目录（实验）",
  en=r"""
- `sudo adduser brian`, `sudo adduser nigel`; `sudo usermod -aG users brian` (add to group, `-a` = append!). Check with `tail /etc/passwd`, `tail /etc/group`.
- `su brian` switches user (prompt changes); `exit` returns.
- Goal: brian rwx; group `users` may list and enter but not create; others nothing → `chgrp -R users ~brian`, `chmod 750 ~brian`.
- Results: nigel can view brian's dir and readme but not edit/create; vagrant can't enter at all ("Permission denied") — but vagrant can `sudo` around everything.
- A `private` dir with `700`: nigel sees the folder name but can't `cd` or list it, and can't read `private/secret.txt` even knowing the name.
- Why files differ in group: new files take the creator's primary group (unless the dir has setgid).
""",
  zh=r"""
- `sudo adduser brian`、`sudo adduser nigel`；`sudo usermod -aG users brian`（加入组，`-a` = 追加，别漏！）。用 `tail /etc/passwd`、`tail /etc/group` 检查。
- `su brian` 切换用户（提示符会变）；`exit` 返回。
- 目标：brian 拥有 rwx；`users` 组可列出、可进入但不能新建；其他人无权限 → `chgrp -R users ~brian`、`chmod 750 ~brian`。
- 结果：nigel 能看 brian 的目录和 readme，但不能改/建；vagrant 根本进不去（“Permission denied”）——但 vagrant 能用 `sudo` 绕过一切。
- 权限 `700` 的 `private` 目录：nigel 能看到目录名，但不能 `cd`、不能列出，即使知道文件名也读不了 `private/secret.txt`。
- 为什么两个文件的属组不同：新文件取创建者的主组（除非目录设置了 setgid）。
""",
  see=["users-groups", "unix-dac", "path-permission"])

c("path-permission", "Permission along the whole path", "整条路径的权限",
  en=r"""
- To access `/home/brian/private/secret.txt` you need `x` on **every** directory: `/`, `/home`, `/home/brian`, `/home/brian/private` — and then `r` on the file.
- So a world-readable file inside a `700` directory is still private.
! On lab machines your home dir is readable by other students by default — keep private work in a folder only you can access.
""",
  zh=r"""
- 要访问 `/home/brian/private/secret.txt`，需要**每一级**目录都有 `x`：`/`、`/home`、`/home/brian`、`/home/brian/private`——然后文件本身要有 `r`。
- 因此位于 `700` 目录中的“所有人可读”文件，实际仍是私有的。
! 实验室机器上家目录默认其他同学可读——私人作业放在只有你能访问的目录里。
""",
  see=["unix-dac", "permissions-lab"])

c("setuid-demo", "setuid in practice (message-brian)", "setuid 实操（message-brian）",
  en=r"""
- brian compiles `message-brian.c` (appends argv[1] to `/home/brian/messages.txt`), then `chmod u+s message-brian` → `-rwsr-xr-x`.
- nigel runs `./message-brian "Hi from Nigel!"` → file created/appended as **brian**, although nigel can't write in brian's home himself.
- Shows: setuid lets others do *one specific task* as you. Danger: a bug in such a program = account takeover.
- Audit: `sudo find / -perm /4000` → `sudo`, `su`, `mount`, `umount`, `passwd` (needs to write `/etc/shadow`, owned by root).
""",
  zh=r"""
- brian 编译 `message-brian.c`（把 argv[1] 追加到 `/home/brian/messages.txt`），再 `chmod u+s message-brian` → `-rwsr-xr-x`。
- nigel 运行 `./message-brian "Hi from Nigel!"` → 文件以 **brian** 的身份被创建/追加，尽管 nigel 自己无权在 brian 家目录写文件。
- 说明：setuid 让别人以你的身份完成*某个特定任务*。风险：程序里一个 bug = 账号被接管。
- 审计：`sudo find / -perm /4000` → `sudo`、`su`、`mount`、`umount`、`passwd`（需要写属于 root 的 `/etc/shadow`）。
""",
  see=["special-bits", "users-groups"])

c("sudoers", "sudoers & visudo", "sudoers 与 visudo",
  en=r"""
- Without permission: "brian is not in the sudoers file. This incident will be reported."
- `/etc/sudoers` (+ files in `/etc/sudoers.d`, via `#includedir` — not a comment!). Lines: `root ALL=(ALL) ALL`, `%sudo ALL=(ALL) ALL` (group sudo, with password), `%wheel ALL=(ALL) NOPASSWD: ALL`.
- Grant one command: `%users ALL=(ALL) /sbin/reboot` → brian can `sudo reboot`.
! Always edit with `visudo` (checks syntax). A syntax error in sudoers breaks sudo; keep a root shell (`sudo su`) open while editing.
""",
  zh=r"""
- 没有权限时：“brian is not in the sudoers file. This incident will be reported.”
- `/etc/sudoers`（以及通过 `#includedir` 引入的 `/etc/sudoers.d` 中的文件——这一行不是注释！）。常见行：`root ALL=(ALL) ALL`、`%sudo ALL=(ALL) ALL`（sudo 组，需要密码）、`%wheel ALL=(ALL) NOPASSWD: ALL`。
- 只授权一条命令：`%users ALL=(ALL) /sbin/reboot` → brian 可以 `sudo reboot`。
! 一定用 `visudo` 编辑（会检查语法）。sudoers 语法错误会让 sudo 失效；编辑时保持一个 root shell（`sudo su`）开着。
""",
  see=["sudo-root", "users-groups"])

for n, e, z, k in [
    ("touch F", "create empty file / update time", "创建空文件 / 更新时间", "quoting"),
    ("rm, mkdir, cd, mv, cp, ln -s", "basic file operations", "基本文件操作", "cmd-groups"),
    ("x=5; echo \"$x\"; ${x:?msg}", "set / use / require a variable", "设置 / 使用 / 强制要求变量", "variables"),
    ("export VAR; env", "environment variables", "环境变量", "variables"),
    ("$(cmd)  `cmd`", "command substitution", "命令替换", "command-substitution"),
    ("a | b", "pipe stdout to stdin", "管道", "pipes"),
    ("> >> < 2> 2>&1", "redirect streams", "重定向", "redirection"),
    ("<<< 'str'  <<EOF", "here-string / here-document", "here-string / here 文档", "here-doc"),
    ("diff A B; diff A <(cmd)", "compare files / with output", "比较文件 / 与命令输出比较", "redirection"),
    ("cat head tail sort uniq wc tr cut tee column", "text filters", "文本过滤器", "filters"),
    ("find . -name '*.md' -exec CMD {} \\+", "find files and act on them", "查找文件并处理", "find-xargs"),
    ("xargs CMD", "stdin lines → arguments", "stdin 行 → 参数", "find-xargs"),
    ("for / if / case / while", "control flow builtins", "流程控制内建命令", "control-flow"),
    ("test, [ ], [[ ]], $?", "conditions and exit status", "条件判断与退出状态", "control-flow"),
    ("&&  ||", "run if previous succeeded / failed", "前一条成功 / 失败时执行", "control-flow"),
    ("name() { …; }", "define a function", "定义函数", "shell-functions"),
    ("source ~/.profile", "re-read a startup file", "重新读取启动文件", "startup-files"),
    ("#!/usr/bin/env bash; chmod +x", "make a script runnable", "让脚本可执行", "shell-script"),
    ("set -e -u -o pipefail", "strict mode", "严格模式", "strict-mode"),
    ("& Ctrl-Z fg bg jobs wait kill ps", "job control", "作业控制", "job-control"),
    ("adduser, usermod -aG, su, chgrp -R", "manage users and groups", "管理用户和组", "permissions-lab"),
    ("chmod u+s; find / -perm /4000", "set / find setuid", "设置 / 查找 setuid", "setuid-demo"),
    ("visudo", "safely edit /etc/sudoers", "安全编辑 sudoers", "sudoers"),
    ("awk basename bc comm crontab dd df du ed env install less ln patch screen/tmux sendmail strings stty tar trap wall yes", "POSIX tool zoo (all examinable: read the man pages)", "POSIX 工具大全（都可能考：去读手册）", "cmd-groups"),
]:
    cmd(n, e, z, k)

# =====================================================================  W3
W(3)
S("theory", "What regular expressions are", "正则表达式是什么")
c("regex", "Regular expressions", "正则表达式", exam=True,
  en=r"""
- A language for **matching text**, based on a **finite state machine**. Also called re / regex / regexp.
- Described by Stephen Cole Kleene in the 1950s; built into UNIX tools before standards existed.
- A **regular language**: bounded complexity, no arbitrary recursion/nesting (can't match balanced brackets).
- Finicky and brittle, "write-only code" (you will forget how it works) — but solves ~99% of practical text problems. Example of excess: the "almost works" email-address regex.
""",
  zh=r"""
- 一种**匹配文本**的语言，基于**有限状态机**。也写作 re / regex / regexp。
- 由 Stephen Cole Kleene 于 1950 年代提出；在标准出现前就已内置于 UNIX 工具。
- 属于**正则语言**：复杂度有上限，不能任意递归/嵌套（无法匹配成对括号）。
- 挑剔、脆弱，“只写代码”（写完你自己也会忘）——但能解决约 99% 的实际文本问题。反面教材：那个“几乎能用”的邮箱正则。
""",
  see=["regex-flavours", "regex-matching", "globbing", "grep"])

c("regex-flavours", "Flavours: BRE, ERE, PCRE", "流派：BRE、ERE、PCRE", exam=True,
  en=r"""
| Flavour | Used by | Group / repeat syntax |
|---|---|---|
| POSIX **Basic** (BRE) | `grep`, `sed` (default) — **the unit's standard** | `\( \)`, `\{n,m\}`, `\+`, `\?` (backslash = special) |
| POSIX **Extended** (ERE) | `grep -E`, `sed -E`, `awk` | `( )`, `{n,m}`, `+`, `?`, alternation `a\|b` |
| **Perl / PCRE** | `perl`, `grep -P`, most languages | ERE + `\d \w \s`, lazy `*?`, lookarounds… |
- In ERE/PCRE you escape to get the *literal* character (`\(`); in BRE you escape to get the *special* meaning.
- Alternation ("or"): ERE `day|way`; GNU BRE writes it with a backslash before the bar.
""",
  zh=r"""
| 流派 | 使用者 | 分组 / 重复语法 |
|---|---|---|
| POSIX **基本**（BRE） | `grep`、`sed`（默认）——**本课程标准** | `\( \)`、`\{n,m\}`、`\+`、`\?`（加反斜杠才是特殊含义） |
| POSIX **扩展**（ERE） | `grep -E`、`sed -E`、`awk` | `( )`、`{n,m}`、`+`、`?`、“或” `a\|b` |
| **Perl / PCRE** | `perl`、`grep -P`、大多数编程语言 | ERE + `\d \w \s`、非贪婪 `*?`、环视…… |
- ERE/PCRE 中转义得到*字面*字符（`\(`）；BRE 中转义得到*特殊*含义。
- “或”运算：ERE 写 `day|way`；GNU BRE 要在竖线前加反斜杠。
""",
  see=["regex", "regex-groups", "regex-quantifiers", "perl"])

c("regex-matching", "How a regex is matched", "正则如何匹配",
  en=r"""
- Start at the left, one item at a time: if it matches, continue; otherwise **backtrack** and retry (possibly from the next character).
- Most regexes are **greedy**: quantifiers match as much as possible (`a.*b` on `axbxb` matches the whole string).
- A regex with no anchors matches if it occurs **anywhere** in the line (substring).
""",
  zh=r"""
- 从左边开始逐项匹配：匹配就继续；否则**回溯**重试（可能从下一个字符开始）。
- 大多数正则是**贪婪**的：量词尽可能多地匹配（`a.*b` 在 `axbxb` 上匹配整个字符串）。
- 没有锚点的正则只要在行中**任意位置**出现就算匹配（子串）。
""",
  see=["regex-quantifiers", "regex-basics"])

S("syntax", "Syntax (POSIX basic)", "语法（POSIX 基本）")
c("regex-basics", "Characters, . ^ $", "字符、. ^ $", exam=True,
  en=r"""
| Item | Matches |
|---|---|
| `abc` | literal "abc" anywhere in the line |
| `.` | any single character |
| `^` | start of line |
| `$` | end of line (single-quote it in the shell) |
| `brian.` | "brian" followed by any one character |
| `^..$` | lines of exactly two characters |
| `\.` | a literal dot |
""",
  zh=r"""
| 写法 | 匹配 |
|---|---|
| `abc` | 行中任意位置的字面 “abc” |
| `.` | 任意单个字符 |
| `^` | 行首 |
| `$` | 行尾（在 shell 中要用单引号括起来） |
| `brian.` | “brian” 后跟任意一个字符 |
| `^..$` | 恰好两个字符的行 |
| `\.` | 字面的点 |
""",
  see=["bracket-expr", "quoting"])

c("bracket-expr", "Bracket expressions [ ]", "方括号表达式 [ ]", exam=True,
  en=r"""
| Item | Matches one character… |
|---|---|
| `[nigel]` | any of n, i, g, e, l |
| `[^nigel]` | anything **except** those |
| `[a-z0-9]` | in the range a–z or 0–9 |
| `[[:alpha:]]` `[[:digit:]]` `[[:space:]]` `[[:upper:]]` | POSIX character classes |
- Lab: "kp" but not "ckp" → `[^c]kp`; three-letter words without vowels → `^[^aeiou]\{3\}$`.
""",
  zh=r"""
| 写法 | 匹配一个字符…… |
|---|---|
| `[nigel]` | n、i、g、e、l 中任一个 |
| `[^nigel]` | 这些字符**以外**的任一个 |
| `[a-z0-9]` | 在 a–z 或 0–9 范围内 |
| `[[:alpha:]]` `[[:digit:]]` `[[:space:]]` `[[:upper:]]` | POSIX 字符类 |
- 实验：含 “kp” 但不含 “ckp” → `[^c]kp`；不含元音的三字母词 → `^[^aeiou]\{3\}$`。
""",
  see=["regex-basics", "regex-quantifiers"])

c("regex-quantifiers", "Quantifiers", "量词", exam=True,
  en=r"""
| BRE | ERE | Repeats the previous item |
|---|---|---|
| `*` | `*` | 0 or more |
| `\+` | `+` | 1 or more |
| `\?` | `?` | 0 or 1 (`colou\?r` → color, colour) |
| `\{n\}` | `{n}` | exactly n |
| `\{n,m\}` | `{n,m}` | n to m; leave a side empty for open range `\{2,\}` |
- Applies to the single preceding item unless grouped: `squ\(ee\)\+` = even number of e's; `squ\(e\{2,3\}\)\+` = multiple of 2 or 3.
- `why does the standalone bit matter\?` matches "…matte" or "…matter": the `\?` binds only to `r`.
- Lab: P-words with ≥4 a's → `grep -i '^p.*a.*a.*a.*a'` (not `a*`, which also matches zero).
""",
  zh=r"""
| BRE | ERE | 重复前一项 |
|---|---|---|
| `*` | `*` | 0 次或多次 |
| `\+` | `+` | 1 次或多次 |
| `\?` | `?` | 0 或 1 次（`colou\?r` → color、colour） |
| `\{n\}` | `{n}` | 恰好 n 次 |
| `\{n,m\}` | `{n,m}` | n 到 m 次；一侧留空表示开区间 `\{2,\}` |
- 只作用于紧前面的一项，除非分组：`squ\(ee\)\+` = 偶数个 e；`squ\(e\{2,3\}\)\+` = e 的个数是 2 或 3 的倍数。
- `why does the standalone bit matter\?` 匹配 “…matte” 或 “…matter”：`\?` 只作用于 `r`。
- 实验：以 P 开头且至少 4 个 a 的词 → `grep -i '^p.*a.*a.*a.*a'`（不能用 `a*`，它也匹配 0 个）。
""",
  see=["regex-groups", "regex-matching", "globbing"])

c("regex-groups", "Groups & back-references", "分组与反向引用", exam=True,
  en=r"""
- `\( … \)` makes the contents **one standalone unit** (for quantifiers) and **captures** what it matched.
- `\n` (normally 1–9) matches the same text again as the n-th group: `\(.\)\1` = a double letter.
- `\([[:alpha:]]\+\) \1 \1` matches triple tautonyms ("gorilla gorilla gorilla").
- Lecture: words with ≥2 double letters `\(\(.\)\2.*\)\{2\}` (4137); ≥3: 170; ≥4: 4 (killeekillee, possessionlessness, subbookkeeper, successlessness).
- In sed replacements `\1` inserts the captured text ([[sed]]).
""",
  zh=r"""
- `\( … \)` 把内容作为**一个整体**（供量词使用），并**捕获**其匹配到的文本。
- `\n`（通常 1–9）再次匹配第 n 个分组捕获的同一段文本：`\(.\)\1` = 双写字母。
- `\([[:alpha:]]\+\) \1 \1` 匹配三重同名（“gorilla gorilla gorilla”）。
- 讲座：含至少 2 处双字母的词 `\(\(.\)\2.*\)\{2\}`（4137 个）；至少 3 处：170；至少 4 处：4 个（killeekillee、possessionlessness、subbookkeeper、successlessness）。
- 在 sed 的替换部分，`\1` 插入捕获的文本（[[sed]]）。
""",
  code=r"""
grep -i '\(.\)\1' /usr/share/dict/words | wc -l      # 50988
grep -ic '\(\(.\)\2.*\)\{3\}' /usr/share/dict/words  # 170
""",
  see=["regex-quantifiers", "sed"])

S("grep", "grep: search", "grep：搜索")
c("grep", "grep", "grep 搜索", exam=True,
  en=r"""
- Name from the `ed` command `g/re/p` (**g**lobal / **re**gexp / **p**rint). Prints every input line that matches the regex.
| Option | Meaning |
|---|---|
| `-i` | case-insensitive |
| `-v` | invert: lines that don't match |
| `-o` | print only the matching part (each match on its own line) |
| `-c` | count matching **lines** |
| `-w` | match whole words only |
| `-n`, `-H` | show line numbers / file names |
| `-R` | search a directory recursively |
| `-l` | list files that contain a match |
| `-E`, `-P` | extended / Perl regex (non-POSIX) |
- `grep -c x` vs `grep -o x | wc -l` differ when a line has several matches (lines vs matches).
- Faster alternatives (ripgrep `rg`) exist but behave differently.
""",
  zh=r"""
- 名字来自 `ed` 编辑器的命令 `g/re/p`（**g**lobal 全局 / **re**gexp 正则 / **p**rint 打印）。打印所有匹配正则的输入行。
| 选项 | 含义 |
|---|---|
| `-i` | 忽略大小写 |
| `-v` | 反选：不匹配的行 |
| `-o` | 只打印匹配部分（每个匹配一行） |
| `-c` | 统计匹配的**行数** |
| `-w` | 只匹配完整单词 |
| `-n`、`-H` | 显示行号 / 文件名 |
| `-R` | 递归搜索目录 |
| `-l` | 列出含匹配的文件 |
| `-E`、`-P` | 扩展 / Perl 正则（非 POSIX） |
- 一行有多个匹配时，`grep -c x` 与 `grep -o x | wc -l` 结果不同（行数 vs 匹配数）。
- 有更快的替代品（ripgrep `rg`），但行为不完全相同。
""",
  code=r"""
grep 'Q' words                 # contains capital Q
grep -i '^r' words             # starts with r/R
grep 'j$' words                # ends in j
grep -ic 'q' words             # how many contain q, any case
grep 'cl' words | head -n 5
grep '^..$' words | tail -n 15
grep '^..e.ded$' words         # 7 letters, 3rd 'e', ends 'ded'
""",
  see=["regex", "filters", "sed", "quoting"])

S("sed", "sed: stream editing", "sed：流编辑")
c("sed", "sed", "sed 流编辑器", exam=True,
  en=r"""
- **S**tream **ed**itor: reads lines, applies a program, writes the result. Syntax like single-letter assembly; 99% of uses are search-and-replace.
- `s/target/replacement/flags`: flags `g` = every match on the line (not just the first), `i` = case-insensitive.
- In the replacement: `&` = whole match; `\1`, `\2` = captured groups.
- Addresses: `/re/p` with `-n` prints matching lines (grep with sed).
- Options: `-n` don't print by default, `-E` extended regex, `-i` edit files in place, `-e` add a script.
- `y/ABCDEF/abcdef/` transliterates characters (but `tr` is simpler). GNU sed extras like `\U` (uppercase) are not POSIX.
""",
  zh=r"""
- **流编辑器**（stream editor）：逐行读入，执行程序，输出结果。语法像单字母汇编；99% 的用途是查找替换。
- `s/目标/替换/标志`：`g` = 替换行中所有匹配（而非只第一个），`i` = 忽略大小写。
- 替换部分：`&` = 整个匹配；`\1`、`\2` = 捕获的分组。
- 地址：`-n` 配合 `/re/p` 只打印匹配行（用 sed 实现 grep）。
- 选项：`-n` 默认不打印，`-E` 扩展正则，`-i` 原地修改文件，`-e` 添加脚本。
- `y/ABCDEF/abcdef/` 逐字符替换（用 `tr` 更简单）。GNU sed 的 `\U`（转大写）等扩展不是 POSIX。
""",
  code=r"""
grep 'ay$' words | sed 's/day/week/'
sed 's/^s.*/sway/'                     # words starting with s -> sway
sed 's/.*day.*/& day/'                 # saturday -> saturday day
sed 's/\(.*\)day$/\1day or \1week/'    # Xday -> Xday or Xweek
sed 's/\(.*\)\([wd]ay\)$/\2 (\1)/'     # someday -> day (some)
sed -n '/\(\(.\)\2.*\)\{4\}/p' words   # grep with sed
echo "0x1FFF3BB0" | sed 'y/ABCDEF/abcdef/'
""",
  see=["regex-groups", "grep", "find-xargs", "awk"])

S("awk", "awk: fields & records", "awk：字段与记录")
c("awk", "awk", "awk 文本处理语言", exam=True,
  en=r"""
- For **semi-structured** data: a programming language focused on line-based input. Named after **A**ho, **W**einberger, **K**ernighan.
- Program = `pattern { action }` pairs, run on every line (record). No pattern = every line; no action = print.
- `-F,` sets the field separator; `$1, $2…` fields, `$0` whole line, `NF` number of fields, `NR` line number.
- `BEGIN { }` runs before input, `END { }` after. Variables need no declaration (`sum` starts at 0).
- `$2 ~ /re/` field matches regex; `!~` doesn't; `/re/` alone tests the whole line.
- Spreadsheet-like jobs on the command line (receipt totals, subtotals per person).
""",
  zh=r"""
- 处理**半结构化**数据：一种面向逐行输入的编程语言。名字取自 **A**ho、**W**einberger、**K**ernighan。
- 程序 = 若干 `模式 { 动作 }`，对每一行（记录）执行。没有模式 = 每行都执行；没有动作 = 打印。
- `-F,` 设字段分隔符；`$1, $2…` 各字段，`$0` 整行，`NF` 字段数，`NR` 行号。
- `BEGIN { }` 在读输入前执行，`END { }` 在之后。变量无需声明（`sum` 初值为 0）。
- `$2 ~ /re/` 字段匹配正则；`!~` 不匹配；单独写 `/re/` 测试整行。
- 在命令行完成类似电子表格的工作（收据总额、每人小计）。
""",
  code=r"""
awk -F, '{print $1}' < receipt
awk -F, '
  $2 ~ /^$/  { if (sum > 0) { print "-----," sum; sum = 0 }; print }
  $2 !~ /^$/ { sum += $2; print $0 "," sum }
  END        { print "-----," sum }' < receipt | column -ts,
""",
  see=["filters", "sed", "perl"])

S("perl", "Perl & the UNIX philosophy", "Perl 与 UNIX 哲学")
c("unix-philosophy", "UNIX philosophy", "UNIX 哲学",
  en=r"""
- Write small tools that **do one thing well**, and connect them with text streams ([[pipes]]).
- shell, grep, sed, awk exist separately because they were "written in anger" for a specific job.
- Downside: 12 tools = 12 syntaxes to remember → motivation for [[perl]].
""",
  zh=r"""
- 写只**做好一件事**的小工具，用文本流把它们连起来（[[pipes]]）。
- shell、grep、sed、awk 各自独立，是因为它们都是为了解决某个具体问题“一气之下”写出来的。
- 缺点：12 个工具 = 要记 12 套语法 → 于是有了[[perl]]。
""",
  see=["pipes", "cmd-groups"])

c("perl", "Perl & Raku", "Perl 与 Raku",
  en=r"""
- General-purpose language with lots of built-in text-manipulation features (PCRE regexes); a more stable, portable shell-script.
- Raku (formerly Perl 6): a fork with more features (PEG grammars). Practice: theweeklychallenge.org.
""",
  zh=r"""
- 通用编程语言，内置大量文本处理功能（PCRE 正则）；可视为更稳定、更可移植的 shell 脚本。
- Raku（原 Perl 6）：分支语言，功能更多（PEG 文法）。练习网站：theweeklychallenge.org。
""",
  see=["regex-flavours", "unix-philosophy"])

for n, e, z, k in [
    (". ^ $", "any char / start / end of line", "任意字符 / 行首 / 行尾", "regex-basics"),
    ("[abc] [^abc] [a-z] [[:alpha:]]", "bracket expressions", "方括号表达式", "bracket-expr"),
    ("* \\+ \\? \\{n,m\\}", "BRE quantifiers (ERE: * + ? {n,m})", "BRE 量词（ERE：* + ? {n,m}）", "regex-quantifiers"),
    ("\\( \\) \\1", "group / back-reference", "分组 / 反向引用", "regex-groups"),
    ("grep -i -v -o -c -w -n -R -l -E -P", "search with regex", "正则搜索", "grep"),
    ("sed 's/re/rep/g'", "substitute (g = all matches)", "替换（g = 全部匹配）", "sed"),
    ("sed -n '/re/p'; sed -i; sed -E", "print matches / in place / ERE", "打印匹配 / 原地修改 / 扩展正则", "sed"),
    ("sed 'y/abc/xyz/'", "transliterate", "逐字符转换", "sed"),
    ("awk -F, '{print $1}'", "print a field", "打印字段", "awk"),
    ("awk 'BEGIN{} /re/{} END{}'", "awk program structure", "awk 程序结构", "awk"),
    ("column -ts,", "align CSV into columns", "把 CSV 对齐成列", "filters"),
    ("seq 2 6", "print a number sequence", "生成数字序列", "control-flow"),
]:
    cmd(n, e, z, k)
