from model import W, S, c, cmd

# =====================================================================  W6
W(6)
S("what", "What testing asks", "测试要回答什么")
c("testing-question", "Does the code do what it should?", "代码是否做了该做的事？", exam=True,
  en=r"""
- Rephrased: **for all valid inputs, does the code produce the intended outputs?** Two sub-questions: what are the valid inputs? what behaviour is expected for them?
- Most problems found in testing come from the programmer **not knowing those answers precisely** (an under-specified spec).
- Parable of `mean`: "mean of an array of ints" → "…as a float" → "…and when the sum exceeds INT_MAX it should…". Each refinement is a decision a test can pin down.
""",
  zh=r"""
- 换个说法：**对所有合法输入，代码是否产生预期输出？**两个子问题：哪些输入合法？对这些输入期望什么行为？
- 测试中发现的问题，大多源于程序员**并不确切知道这些答案**（规格不完整）。
- `mean` 的寓言：“求 int 数组的平均值” → “……以 float 返回” → “……当总和超过 INT_MAX 时应当……”。每一步细化都是一个可以用测试固定下来的决定。
""",
  see=["assert", "unit-test", "tdd"])

S("assert", "Assertions", "断言")
c("assert", "assert()", "断言 assert()", exam=True,
  en=r"""
- A logical statement about variables at a point in the program: "it is true that `strlen(extension) > 0` here". C: `#include <assert.h>`.
- If true: nothing happens. If false: the program complains (file, line, expression) and **aborts** — roughly `if (!cond) { complain(); exit(1); }`.
- Compile with `-DNDEBUG` to remove all assertions (production) — the logic they guarded is then unchecked.
- Strengths: access to internal state at runtime; test assumptions during development.
- Limits: embedded in the code, hard to review, and don't show that the code produces the **right behaviour** → need an external view: [[unit-test]].
""",
  zh=r"""
- 关于程序某处变量的逻辑陈述：“此处 `strlen(extension) > 0` 一定成立”。C 语言：`#include <assert.h>`。
- 为真：什么也不发生。为假：程序报错（文件、行号、表达式）并**中止**——大致相当于 `if (!cond) { complain(); exit(1); }`。
- 用 `-DNDEBUG` 编译会移除所有断言（用于生产环境）——但它们守护的逻辑就不再被检查。
- 优点：运行时能访问内部状态；开发时检验自己的假设。
- 局限：嵌在代码里，难以审查；也不能证明代码产生了**正确的行为** → 需要外部视角：[[unit-test]]。
""",
  code=r"""
#include <assert.h>
static void add_mime_mapping(const char *extension, const char *mimetype) {
    assert(strlen(extension) > 0);
    assert(strlen(mimetype) > 0);
    ...
}
""",
  see=["unit-test", "debugging"])

S("unit", "Unit testing with Unity", "用 Unity 做单元测试")
c("unit-test", "Unit tests & regressions", "单元测试与回归", exam=True,
  en=r"""
- Run your code against a set of inputs and compare the **actual** result with the **declared expected** result, from outside, through the code's interfaces (what users care about: does it do what the docs say?).
- Any failing test = the current version is broken.
- **Regression**: code that passed all tests before your change and fails some after — you broke previously working behaviour.
- Frameworks exist for most languages; writing good tests is a skill (QA teams).
""",
  zh=r"""
- 用一组输入从外部、通过接口运行代码，把**实际**结果与**声明的期望**结果比较（这是用户关心的：它是否如文档所说？）。
- 任何测试失败 = 当前版本有问题。
- **回归（regression）**：改动前全部测试通过，改动后有测试失败——你破坏了原本正常的行为。
- 大多数语言都有测试框架；写好测试是一门手艺（QA 团队专做这个）。
""",
  see=["unity", "tdd", "git-hooks", "github-actions"])

c("unity", "Unity (C test framework)", "Unity（C 测试框架）", exam=True,
  en=r"""
- Unity by ThrowTheSwitch (not the game engine). Install: `git clone …/Unity.git; cd Unity; cmake .; sudo make install` (headers in `/usr/local/include/unity/`).
- Test file includes `unity.h` and the code under test; defines `setUp()` / `tearDown()` (run before/after each test), test functions with assertions, and a `main` with `UNITY_BEGIN(); RUN_TEST(test_x); return UNITY_END();`.
- Build: `gcc -I /usr/local/include/unity/ -o tests test.c -l unity` (`-I` header path, `-l` link library). Or `export CPATH=/usr/local/include/unity/`.
- Output per test `test.c:13:test_add:PASS` / `FAIL: Expected 0 Was 2`, then a summary; exit status non-zero if any fail.
- Assertions: `TEST_ASSERT_EQUAL`, `TEST_ASSERT_EQUAL_FLOAT`, `TEST_ASSERT_EQUAL_STRING`, `TEST_ASSERT_TRUE`… (see the Unity assertions reference).
""",
  zh=r"""
- ThrowTheSwitch 出品的 Unity（不是那个游戏引擎）。安装：`git clone …/Unity.git; cd Unity; cmake .; sudo make install`（头文件在 `/usr/local/include/unity/`）。
- 测试文件包含 `unity.h` 和被测代码；定义 `setUp()` / `tearDown()`（每个测试前/后运行）、带断言的测试函数，以及 `main`：`UNITY_BEGIN(); RUN_TEST(test_x); return UNITY_END();`。
- 编译：`gcc -I /usr/local/include/unity/ -o tests test.c -l unity`（`-I` 头文件路径，`-l` 链接库）。或 `export CPATH=/usr/local/include/unity/`。
- 每个测试输出 `test.c:13:test_add:PASS` / `FAIL: Expected 0 Was 2`，最后是汇总；有失败则退出状态非 0。
- 断言：`TEST_ASSERT_EQUAL`、`TEST_ASSERT_EQUAL_FLOAT`、`TEST_ASSERT_EQUAL_STRING`、`TEST_ASSERT_TRUE`……（见 Unity 断言手册）。
""",
  code=r"""
#include "unity.h"
#include "calc.c"
void setUp(void) {}
void tearDown(void) {}
void test_add(void) { TEST_ASSERT_EQUAL(4, add(2, 2)); }
int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_add);
    return UNITY_END();
}
/* gcc -o tests test.c -l unity; ./tests */
""",
  see=["unit-test", "tdd", "makefile"])

S("tdd", "Test-driven development", "测试驱动开发")
c("tdd", "TDD: red → green → refactor", "TDD：红 → 绿 → 重构", exam=True,
  en=r"""
- Bad usual process: write code → write tests → occasionally run them (by then it's already implemented the wrong way).
- TDD: **write the test for the behaviour first**, then the code. Pick one specific behaviour (spec item, edge case, bug), then:
| Step | Do |
|---|---|
| RED | write one test; run; confirm it **currently fails** |
| GREEN | make the **simplest change** that passes; run; confirm pass |
| REFACTOR | make the code good while **all** tests still pass |
- Keep every test → a growing **test suite** that documents intent and catches regressions.
- Forces you to decide the desired output (design) before hacking. Example: `test_sub` fails with a copy of `add` ("Expected 0 Was 2") → fix → passes. Edge case `add(INT_MAX, 1)`: decide, write the assert, then implement.
""",
  zh=r"""
- 常见的坏流程：写代码 → 写测试 → 偶尔跑一下（这时已经按错误的方式实现了）。
- TDD：**先为目标行为写测试**，再写代码。选一个具体行为（规格条目、边界情况、bug），然后：
| 步骤 | 做什么 |
|---|---|
| 红 RED | 写一个测试；运行；确认它**目前失败** |
| 绿 GREEN | 做**最简单的修改**让它通过；运行；确认通过 |
| 重构 REFACTOR | 在**所有**测试仍通过的前提下把代码改好 |
- 保留每一个测试 → 不断增长的**测试套件**，记录意图并捕获回归。
- 迫使你在动手前先决定期望输出（设计）。例：用 `add` 的副本冒充 `sub`，`test_sub` 失败（“Expected 0 Was 2”）→ 修复 → 通过。边界情况 `add(INT_MAX, 1)`：先决定行为，写断言，再实现。
""",
  see=["unit-test", "unity", "testing-question"])

S("beyond", "Beyond example tests", "超越示例测试")
c("property-testing", "Property testing", "属性测试", exam=True,
  en=r"""
- Spot tests check a few chosen inputs; the input space is huge. Instead, generate **many random inputs** and check that a **property** holds for all, without knowing exact outputs — e.g. `a*b == b*a` (commutativity).
- QuickCheck (originally Haskell); C port `quickcheck4c`: `QCC_testForAll(100, 1000, mulCommutativity, 2, QCC_genInt, QCC_genInt)`.
""",
  zh=r"""
- 抽样测试只检查少数挑选的输入；而输入空间巨大。改为生成**大量随机输入**，检查某个**性质**对所有输入都成立，而不必知道确切输出——如 `a*b == b*a`（交换律）。
- QuickCheck（源自 Haskell）；C 版本 `quickcheck4c`：`QCC_testForAll(100, 1000, mulCommutativity, 2, QCC_genInt, QCC_genInt)`。
""",
  see=["fuzzing", "unit-test"])

c("fuzzing", "Fuzzing", "模糊测试", exam=True,
  en=r"""
- **Fuzzers** generate deranged inputs to break programs, trying to reach every path through the conditionals. Random input often makes code crash.
- "Interesting" behaviour (unexpected path, impossible value, protected state reached) is often the first step to a **vulnerability**.
- AFL taught itself valid JPEGs starting from the input "hello".
- Lesson: "being very careful" isn't enough; you are not more inventive than fuzzer authors → need proof: [[formal-verification]].
""",
  zh=r"""
- **模糊测试器**生成稀奇古怪的输入来搞崩程序，试图走遍条件分支的每条路径。随机输入经常能让代码崩溃。
- “有趣”的行为（不该走的路径、本不可能的值、访问到受保护状态）往往是发现**漏洞**的第一步。
- AFL 从输入 “hello” 出发，自己摸索出了合法的 JPEG 文件。
- 教训：“非常小心”是不够的；你不比模糊测试工具的作者更有想象力 → 需要证明：[[formal-verification]]。
""",
  see=["property-testing", "crackme", "sql-injection"])

c("formal-verification", "Formal verification", "形式化验证",
  en=r"""
- Mathematically **prove** desired properties always hold under specified conditions — the highest standard of certainty.
- Reasoning about programs in general is essentially impossible; even specific properties of constrained programs are HARD. Rare, used for high-stakes software.
- Tools: proof assistants such as **Lean** (a programming language where proving correctness is part of writing the code).
""",
  zh=r"""
- 用数学**证明**在特定条件下所需性质总是成立——最高标准的确定性。
- 对一般程序做推理基本不可能；即使只针对受限程序的特定性质也非常难。很少使用，多见于高风险软件。
- 工具：证明助手，如 **Lean**（一种编程语言，证明正确性是写代码的一部分）。
""",
  see=["fuzzing", "testing-question"])

S("auto", "Automating tests", "自动化测试")
c("git-hooks", "Git hooks: pre-commit", "Git 钩子：pre-commit", exam=True,
  en=r"""
- Scripts in `.git/hooks/` that Git runs at certain events; samples provided (`pre-commit.sample`).
- `.git/hooks/pre-commit` runs **before** a commit is created: exit 0 → commit proceeds; **non-zero → commit aborted**.
- Put "build + run tests" there and `chmod +x` it → impossible (well…) to commit code failing the tests, since `./tests` exits non-zero on failure.
- Bypass once: `git commit --no-verify`. Hooks are local (not pushed) — teammates may not have them → [[github-actions]].
""",
  zh=r"""
- `.git/hooks/` 中的脚本，Git 在特定事件发生时运行；目录里有示例（`pre-commit.sample`）。
- `.git/hooks/pre-commit` 在提交创建**之前**运行：返回 0 → 继续提交；**非 0 → 中止提交**。
- 在里面写“编译 + 运行测试”，并 `chmod +x` → 测试不通过的代码就（几乎）无法提交，因为 `./tests` 失败时退出码非 0。
- 临时跳过：`git commit --no-verify`。钩子只在本地（不会被推送）——队友可能没装 → [[github-actions]]。
""",
  code=r"""
#!/bin/sh
gcc -I /usr/local/include/unity -o tests test.c -l unity
./tests
# then: chmod +x .git/hooks/pre-commit
""",
  see=["shell-script", "control-flow", "commit", "github-actions"])

c("github-actions", "GitHub Actions (CI)", "GitHub Actions（持续集成）", exam=True,
  en=r"""
- **Continuous integration**: the central repo runs the test suite on every push and shows the status (green tick / red cross, email) — everyone sees when "YouKnowWho" pushed a bad commit.
- A **workflow** file in `.github/workflows/tests.yml`: `name`, `on:` trigger (push to `main`), `jobs:` → `runs-on: ubuntu-latest` → `steps:` (`uses:` an action such as `actions/checkout`, or `run:` a shell command).
- The example checks out your code and Unity, installs gcc, compiles against Unity's source, runs `./tests`. Watch it under the **Actions** tab.
- A failing test and a compile error both fail the job, at different steps.
""",
  zh=r"""
- **持续集成**：中心仓库在每次推送时运行测试套件并显示状态（绿勾/红叉、邮件）——大家都能看到“某人”推了坏提交。
- **工作流**文件 `.github/workflows/tests.yml`：`name`、`on:` 触发条件（推送到 `main`）、`jobs:` → `runs-on: ubuntu-latest` → `steps:`（`uses:` 某个 action，如 `actions/checkout`；或 `run:` 一条 shell 命令）。
- 示例：检出你的代码和 Unity、安装 gcc、用 Unity 源码编译、运行 `./tests`。在 **Actions** 标签页查看。
- 测试失败和编译错误都会让任务失败，只是失败在不同步骤。
""",
  code=r"""
name: Compile and Test Under Unity
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
        with: { path: main }
      - uses: actions/checkout@v7
        with: { repository: ThrowTheSwitch/Unity, path: unity }
      - run: sudo apt-get install -y gcc
      - run: gcc -I unity/src/ main/test.c unity/src/unity.c -o tests
      - run: ./tests
""",
  see=["git-hooks", "unit-test", "remote"])

for n, e, z, k in [
    ("#include <assert.h>; assert(x)", "runtime assumption check", "运行时检查假设", "assert"),
    ("gcc -DNDEBUG", "compile assertions out", "去除断言", "assert"),
    ("cmake .; sudo make install", "build & install Unity", "构建并安装 Unity", "unity"),
    ("gcc -I DIR -o tests test.c -l unity", "header path & link library", "头文件路径与链接库", "unity"),
    ("export CPATH=DIR", "default header search path", "默认头文件搜索路径", "unity"),
    ("TEST_ASSERT_EQUAL(exp, act)", "Unity assertion", "Unity 断言", "unity"),
    ("UNITY_BEGIN / RUN_TEST / UNITY_END", "Unity test runner", "Unity 测试运行器", "unity"),
    (".git/hooks/pre-commit", "runs before every commit", "每次提交前运行", "git-hooks"),
    ("git commit --no-verify", "skip hooks", "跳过钩子", "git-hooks"),
    (".github/workflows/*.yml", "GitHub Actions workflow", "GitHub Actions 工作流", "github-actions"),
]:
    cmd(n, e, z, k)

# =====================================================================  W7
W(7)
S("why", "Testing vs debugging", "测试与调试")
c("debugging", "Debugging", "调试", exam=True,
  en=r"""
- **Testing** tells you *that* there is a problem (important to notice). **Debugging** finds out *why* (much harder): "`calculate('2.9 ^ 3')` shouldn't return '27' — why does it?"
- Familiar strategies: run the code in your head, rubber-duck debugging, `print` statements, [[assert]].
- This week: tools that work **even without the source code**, for three kinds of question:
| Question | Tool |
|---|---|
| "What is this program doing on my system?" | [[strace]], [[ltrace]] |
| "Why so slow / so much memory?" | [[valgrind]] |
| "Why isn't it behaving as it should?" | [[gdb]] |
""",
  zh=r"""
- **测试**告诉你*有*问题（发现问题很重要）。**调试**找出*为什么*（难得多）：“`calculate('2.9 ^ 3')` 不该返回 '27'——它为什么这样？”
- 熟悉的策略：在脑中运行代码、小黄鸭调试法、`print` 语句、[[assert]]。
- 本讲：**即使没有源代码**也能用的工具，对应三类问题：
| 问题 | 工具 |
|---|---|
| “这个程序在我的系统上到底干了什么？” | [[strace]]、[[ltrace]] |
| “为什么这么慢 / 占这么多内存？” | [[valgrind]] |
| “为什么它的行为不对？” | [[gdb]] |
""",
  see=["testing-question", "crackme"])

S("strace", "Tracing calls", "追踪调用")
c("strace", "strace", "strace 系统调用追踪", exam=True,
  en=r"""
- "What do you do?" tool. `strace CMD` runs CMD to completion, intercepting and printing every **system call** (calls to basic OS functions: `openat`, `read`, `write`, `execve`…).
- `-e open,openat` show only these calls. `-p PID` attach to an **already running** process (find PID with `ps aux | grep NAME`).
- Pre-reading: `man strace` Description and Notes. Output goes to stderr.
- Each line: `call(arguments) = return value`; failures show `-1` and an error name (`ENOENT` no such file, `EACCES` permission denied).
- Diagnosing a crash: `openat(AT_FDCWD, "data.txt", O_RDONLY) = -1 ENOENT` then `--- SIGSEGV {si_addr=NULL} ---` → the file didn't exist, `fopen` returned `NULL`, and the program used that NULL pointer without checking.
""",
  zh=r"""
- “你在干什么？”工具。`strace 命令` 运行该命令直到结束，拦截并打印每个**系统调用**（对操作系统基本功能的调用：`openat`、`read`、`write`、`execve`……）。
- `-e open,openat` 只显示这些调用。`-p PID` 附加到**正在运行**的进程（用 `ps aux | grep 名字` 找 PID）。
- 预读：`man strace` 的 Description 和 Notes。输出写到 stderr。
- 每行格式：`调用(参数) = 返回值`；失败时返回 `-1` 并带错误名（`ENOENT` 文件不存在，`EACCES` 权限不足）。
- 诊断崩溃：`openat(AT_FDCWD, "data.txt", O_RDONLY) = -1 ENOENT` 之后出现 `--- SIGSEGV {si_addr=NULL} ---` → 文件不存在，`fopen` 返回 `NULL`，程序没检查就用了这个空指针。
""",
  code=r"""
strace ls
strace -e open,openat ls
ps aux | grep myprog
strace -p 4242
""",
  see=["ltrace", "job-control", "everything-file"])

c("ltrace", "ltrace (and dtrace)", "ltrace（及 dtrace）",
  en=r"""
- Like strace but for **library calls** (`strcmp`, `puts`, `malloc`…) — a higher level of abstraction. Many options are the same.
- May need setup to print fancy data structures. macOS/BSD: `dtrace`.
- Crackme: `ltrace ./crackme-1 <<< 'guess'` shows `strcmp("guess", "Beetlejuice")`.
""",
  zh=r"""
- 类似 strace，但追踪的是**库函数调用**（`strcmp`、`puts`、`malloc`……）——抽象层次更高。很多选项相同。
- 打印复杂数据结构可能需要额外配置。macOS/BSD：`dtrace`。
- crackme：`ltrace ./crackme-1 <<< '猜测'` 会显示 `strcmp("猜测", "Beetlejuice")`。
""",
  see=["strace", "crackme"])

S("valgrind", "Memory: valgrind", "内存：valgrind")
c("valgrind", "valgrind memcheck", "valgrind 的 memcheck", exam=True,
  en=r"""
- Valgrind = suite for **dynamic analysis** (understand the process as it runs). Main tool **memcheck**: memory-management errors — **leaks** (allocated, never freed) and illegal reads/writes.
- `gcc -o badcode demo.c; valgrind --leak-check=yes ./badcode`.
- Demo: `malloc(10 * sizeof(int))` then `x[10] = 0` → "Invalid write of size 4 … 0 bytes after a block of size 40 alloc'd"; HEAP SUMMARY "1 allocs, 0 frees, 40 bytes".
| Leak kind | Meaning |
|---|---|
| definitely lost | allocated and lost the pointer |
| indirectly lost | lost the pointer to where you stored the pointer |
| possibly lost | probably lost it (or doing something fancy) |
| still reachable | still have the pointer, never freed |
| suppressed | would report, but told not to |
""",
  zh=r"""
- Valgrind = 一套**动态分析**工具（在进程运行时理解它）。主力工具 **memcheck**：内存管理错误——**泄漏**（分配了却从未释放）以及非法读写。
- `gcc -o badcode demo.c; valgrind --leak-check=yes ./badcode`。
- 示例：`malloc(10 * sizeof(int))` 后写 `x[10] = 0` → “Invalid write of size 4 … 0 bytes after a block of size 40 alloc'd”；HEAP SUMMARY “1 allocs, 0 frees, 40 bytes”。
| 泄漏类型 | 含义 |
|---|---|
| definitely lost | 分配后丢了指针 |
| indirectly lost | 丢了“存放该指针的地方”的指针 |
| possibly lost | 可能丢了（或你在做什么花哨操作） |
| still reachable | 指针还在，但从未释放 |
| suppressed | 本会报告，但你让它别报 |
""",
  code=r"""
#include <stdlib.h>
void tennumbers(void){
  int* x = malloc(10 * sizeof(int));
  for (int i = 0; i <= 10; i++) x[i] = 10 - i;   /* x[10]: invalid write */
}                                               /* never freed: leak    */
int main(void){ tennumbers(); return 0; }
""",
  see=["valgrind-tools", "gdb"])

c("valgrind-tools", "Other valgrind tools", "valgrind 的其它工具",
  en=r"""
| Tool | Purpose |
|---|---|
| `cachegrind` | profile: which instructions run most |
| `callgrind` | profile + call graph |
| `helgrind`, `drd` | thread errors (concurrency) |
| `massif` | memory usage over time |
- Valgrind is best for inefficiencies and problems that accumulate over time.
""",
  zh=r"""
| 工具 | 用途 |
|---|---|
| `cachegrind` | 性能分析：哪些指令执行最多 |
| `callgrind` | 性能分析 + 调用图 |
| `helgrind`、`drd` | 线程错误（并发） |
| `massif` | 内存使用随时间变化 |
- Valgrind 最适合找效率问题和随时间累积的问题。
""",
  see=["valgrind"])

S("gdb", "The GNU debugger", "GNU 调试器 gdb")
c("gdb", "gdb overview", "gdb 概览", exam=True,
  en=r"""
- General-purpose debugger for C/C++ (also Fortran, Modula-2); prototype for debuggers in other languages (macOS: `lldb`). Four activities: **run** the program, **stop** it at chosen points, **inspect** values, **change** values live.
- Compile with debugging symbols and no optimisation: `gcc -g -O0 -o prog prog.c`.
- `gdb ./prog` (or `gdb -p PID`) opens gdb's own shell; the program does **not** start until `run`.
- Pre-reading: `info gdb` → "Sample Session".
""",
  zh=r"""
- C/C++（及 Fortran、Modula-2）的通用调试器；其它语言调试器的原型（macOS 用 `lldb`）。四件事：**运行**程序、在指定位置**停下**、**查看**值、实时**修改**值。
- 编译时加调试符号、关闭优化：`gcc -g -O0 -o prog prog.c`。
- `gdb ./prog`（或 `gdb -p PID`）进入 gdb 自己的命令行；直到 `run` 程序才会启动。
- 预读：`info gdb` → “Sample Session”。
""",
  see=["gdb-break-step", "gdb-inspect", "debugging"])

c("gdb-break-step", "gdb: run, break, step", "gdb：运行、断点、单步", exam=True,
  en=r"""
| Command | Short | Does |
|---|---|---|
| `run [args] [< file]` | `r` | start the program (`run <<< 'input'` feeds stdin) |
| `break FUNC` / `break LINE` | `b` | stop when reached |
| `info functions` | | list functions (to choose breakpoints) |
| `step` | `s` | next source line, **entering** called functions |
| `next` | `n` | next source line, **stepping over** calls (e.g. past `malloc`) |
| `stepi` | `si` | exactly one machine instruction |
| `continue` | `c` | run until the next breakpoint |
| `jump LINE` | | continue at another line (skip code) |
| `quit` | `q` | exit gdb |
""",
  zh=r"""
| 命令 | 缩写 | 作用 |
|---|---|---|
| `run [参数] [< 文件]` | `r` | 启动程序（`run <<< '输入'` 提供 stdin） |
| `break 函数` / `break 行号` | `b` | 到达时停下 |
| `info functions` | | 列出函数（用于选断点） |
| `step` | `s` | 下一行源码，会**进入**被调用的函数 |
| `next` | `n` | 下一行源码，**跳过**函数调用（如越过 `malloc`） |
| `stepi` | `si` | 恰好一条机器指令 |
| `continue` | `c` | 运行到下一个断点 |
| `jump 行号` | | 跳到另一行继续（跳过代码） |
| `quit` | `q` | 退出 gdb |
""",
  see=["gdb", "gdb-inspect"])

c("gdb-inspect", "gdb: inspect & modify", "gdb：查看与修改", exam=True,
  en=r"""
| Command | Does |
|---|---|
| `print EXPR` (`p`) | evaluate any expression: `p x`, `p x[9]` → `$2 = 0` |
| `p x[6] = 100` | change a value (and echo it) |
| `set var x[4] = 30` | change without echo |
| `list` | source around the current line |
| `info registers` (`i r`) | CPU registers |
| `disas` | disassemble the current function (`=>` marks current instruction) |
| `edit` | open your editor at the current line |
| `help CMD`, `apropos WORD` | built-in help |
- Changing values lets you test a fix without rewriting and recompiling. GDB can alter programs on the fly → useful for **reverse engineering** ([[crackme]]).
""",
  zh=r"""
| 命令 | 作用 |
|---|---|
| `print 表达式`（`p`） | 计算任意表达式：`p x`、`p x[9]` → `$2 = 0` |
| `p x[6] = 100` | 修改值（并回显） |
| `set var x[4] = 30` | 修改值（不回显） |
| `list` | 显示当前行附近的源码 |
| `info registers`（`i r`） | CPU 寄存器 |
| `disas` | 反汇编当前函数（`=>` 指示当前指令） |
| `edit` | 在当前行打开编辑器 |
| `help 命令`、`apropos 词` | 内置帮助 |
- 修改值可以在不改代码、不重新编译的情况下验证修复方案。gdb 能动态修改程序 → 适合**逆向工程**（[[crackme]]）。
""",
  code=r"""
$ gcc -g -O0 -o badcode valgrinddemo.c
$ gdb ./badcode
(gdb) break tennumbers
(gdb) r
Breakpoint 1, tennumbers () at valgrinddemo.c:4
(gdb) n
(gdb) p x[0]
$2 = 10
(gdb) set var x[4] = 30
(gdb) c
""",
  see=["gdb-break-step", "crackme"])

S("re", "Reverse engineering: crackmes", "逆向工程：crackme")
c("crackme", "Crackmes", "Crackme 破解练习", exam=True,
  en=r"""
- Small reverse-engineering puzzles: find the password without reading the source. Build with `make` (seven programs: 1, 1A, 1B, 2–5).
| Tool | Reveals |
|---|---|
| `strings -d ./prog` | printable strings in the binary (crackme-1: "Beetlejuice") |
| `ltrace ./prog <<< 'x'` | library calls with arguments (`strcmp(input, secret)`) |
| `strace` | system calls |
| `objdump -d` | compiled instructions |
| `gdb`: `b main`, `run <<< 'x'`, `disas`, `si`, `i r`, `p` | step and inspect the comparison |
- Hints: 1A try another tool; 1B "what does comparing a string really mean?"; 2 no strings/ltrace shortcut; 3 the input isn't compared to the real password directly; 4 is the random number generator used correctly?; 5 infinitely many solutions, try `.`.
- Tools you're examined on: the ones introduced (gdb, strace, valgrind, ltrace…), not lldb / x64dbg.
""",
  zh=r"""
- 小型逆向谜题：不看源码找出密码。用 `make` 编译（七个程序：1、1A、1B、2–5）。
| 工具 | 能看到 |
|---|---|
| `strings -d ./prog` | 二进制中的可打印字符串（crackme-1：“Beetlejuice”） |
| `ltrace ./prog <<< 'x'` | 带参数的库调用（`strcmp(输入, 密码)`） |
| `strace` | 系统调用 |
| `objdump -d` | 编译后的指令 |
| `gdb`：`b main`、`run <<< 'x'`、`disas`、`si`、`i r`、`p` | 单步执行并查看比较过程 |
- 提示：1A 换个工具；1B “比较字符串到底意味着什么？”；2 无法用 strings/ltrace 走捷径；3 输入并没有直接和真正的密码比较；4 随机数生成器用对了吗？；5 解有无穷多个，试试 `.`。
- 考试只考讲过的工具（gdb、strace、valgrind、ltrace……），不考 lldb / x64dbg。
""",
  code=r"""
$ make
cc -g -O0    crackme-1.c   -o crackme-1
$ strings -d ./crackme-1 | less
$ ltrace ./crackme-1 <<< ';*3$'
strcmp(";*3$", "Beetlejuice") = -7
""",
  see=["gdb-inspect", "ltrace", "here-doc", "makefile", "fuzzing"])

c("makefile", "make & Makefiles", "make 与 Makefile",
  en=r"""
- `make` builds targets from rules in a `Makefile` (here `GNUmakefile`), rebuilding only what's out of date. Built-in rules know how to turn `x.c` into `x` using `$(CC) $(CFLAGS)`.
- Lab file: `CFLAGS=-g -O0` (debug symbols, no optimisation); `CRACKMES=$(patsubst %.c,%,$(wildcard *.c))` = every `.c` file minus the extension; `all: $(CRACKMES)`; `clean:` removes them; `.PHONY` targets aren't files.
- **Pattern rule**: `%.o: %.c` then the recipe `$(CC) -c $< -o $@`. Automatic variables: `$@` = the target, `$<` = the first prerequisite, `$^` = all prerequisites. So `%.a: %.b` with `foo $< -b $@` builds `file.a` from `file.b` by running `foo file.b -b file.a`.
- Recipe lines must start with a **tab**. `make` rebuilds a target only if a prerequisite is newer.
- Other build tools: **Maven** (Java) can also fetch dependencies from remote repositories — a past exam asked why you'd use it instead of make.
- The "proper" version of the [[b-script|./b build helper]].
""",
  zh=r"""
- `make` 根据 `Makefile`（这里叫 `GNUmakefile`）中的规则构建目标，只重建过期的部分。内置规则知道如何用 `$(CC) $(CFLAGS)` 把 `x.c` 变成 `x`。
- 实验文件：`CFLAGS=-g -O0`（调试符号、不优化）；`CRACKMES=$(patsubst %.c,%,$(wildcard *.c))` = 所有 `.c` 文件去掉扩展名；`all: $(CRACKMES)`；`clean:` 删除它们；`.PHONY` 目标不是文件。
- **模式规则**：`%.o: %.c`，配方 `$(CC) -c $< -o $@`。自动变量：`$@` = 目标，`$<` = 第一个依赖，`$^` = 全部依赖。所以 `%.a: %.b` 配 `foo $< -b $@` 表示由 `file.b` 生成 `file.a`，执行 `foo file.b -b file.a`。
- 配方行必须以 **Tab** 开头。只有依赖比目标新时 `make` 才重建该目标。
- 其它构建工具：**Maven**（Java）还能从远程仓库下载依赖——往年考题问过为什么用它而不用 make。
- 是[[b-script|./b 构建助手]]的“正规”版本。
""",
  code=r"""
CFLAGS=-g -O0
CRACKMES=$(patsubst %.c,%,$(wildcard *.c))
.PHONY: all clean
all: $(CRACKMES)
clean:
	$(RM) -rf $(CRACKMES)
""",
  see=["b-script", "gdb", "package-manager"])

for n, e, z, k in [
    ("strace [-e CALLS] [-p PID] CMD", "trace system calls", "追踪系统调用", "strace"),
    ("ltrace CMD", "trace library calls", "追踪库函数调用", "ltrace"),
    ("ps aux | grep NAME", "find a PID", "查找进程号", "strace"),
    ("valgrind --leak-check=yes ./prog", "memory errors & leaks", "内存错误与泄漏", "valgrind"),
    ("gcc -g -O0", "debug symbols, no optimisation", "调试符号、不优化", "gdb"),
    ("gdb ./prog / gdb -p PID", "start debugger / attach", "启动调试 / 附加进程", "gdb"),
    ("run (r), break (b), info functions", "start & breakpoints", "运行与断点", "gdb-break-step"),
    ("step (s), next (n), stepi (si), continue (c), jump", "move through execution", "控制执行", "gdb-break-step"),
    ("print (p), set var, list, info registers, disas, edit", "inspect & modify", "查看与修改", "gdb-inspect"),
    ("strings -d BIN", "printable strings in a binary", "二进制中的可打印字符串", "crackme"),
    ("objdump -d BIN", "disassemble", "反汇编", "crackme"),
    ("make / make clean", "build / clean targets", "构建 / 清理", "makefile"),
]:
    cmd(n, e, z, k)

W(7)
for n, e, z, k in [
    ("%.o: %.c  →  $(CC) -c $< -o $@", "make pattern rule; $@ target, $< first prerequisite, $^ all", "make 模式规则；$@ 目标，$< 第一个依赖，$^ 全部依赖", "makefile"),
]:
    cmd(n, e, z, k)
