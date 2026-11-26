from model import W, S, c, cmd

# =====================================================================  W8
W(8)
S("why", "Why storage decisions matter", "为什么存储决策很重要")
c("bad-storage", "Bad data storage has victims", "糟糕的数据存储会害人", exam=True,
  en=r"""
- Engineers are responsible for what they build (the Calling of the Engineer, after the Quebec Bridge disaster: 75 deaths).
- UK COVID track-and-trace used the old `.xls` format: max **65,536 rows**; extra cases silently dropped. 15,841 referrals missed → est. 125,000–185,000 extra infections, 1,500–2,500 extra deaths (system cost £35m).
- Genomics: Excel auto-converts gene names (`SEPT2` → 2-September, `2310009E13` → 2.31E+13); ~1 in 5 genome datasets affected (2016), rising.
- Building your own storage from scratch ≈ writing your own crypto library: don't. Use a **database**.
""",
  zh=r"""
- 工程师要为自己的作品负责（“工程师召唤”仪式，源于魁北克大桥事故：75 人死亡）。
- 英国新冠追踪系统用旧 `.xls` 格式：最多 **65,536 行**，超出的病例被悄悄丢弃。漏掉 15,841 个转介 → 估计多出 125,000–185,000 例感染、1,500–2,500 人死亡（系统花费 3500 万英镑）。
- 基因组学：Excel 自动转换基因名（`SEPT2` → 9 月 2 日，`2310009E13` → 2.31E+13）；2016 年约五分之一基因数据集受影响，且比例上升。
- 自己从零造存储系统 ≈ 自己写加密库：别这么做。用**数据库**。
""",
  see=["acid", "relational-model"])

c("acid", "ACID transactions", "ACID 事务", exam=True,
  en=r"""
- If multiple applications/people/processes read and write the data, use a **database engine** that provides ACID transactions (MySQL, MariaDB…). An update must be:
| Letter | Property | Meaning |
|---|---|---|
| A | atomic | completes entirely or not at all |
| C | consistent | all constraints of the design are respected |
| I | isolated | doesn't interfere with other concurrent updates |
| D | durable | written to persistent storage |
- Without concurrency needs you may still want a relational system: SQLite, DuckDB. In SQL: [[transactions]].
""",
  zh=r"""
- 若有多个应用/人/进程同时读写数据，就要用提供 ACID 事务的**数据库引擎**（MySQL、MariaDB……）。一次更新必须：
| 字母 | 性质 | 含义 |
|---|---|---|
| A | 原子性 atomic | 要么全部完成，要么完全没发生 |
| C | 一致性 consistent | 遵守设计中的所有约束 |
| I | 隔离性 isolated | 不影响其他并发更新 |
| D | 持久性 durable | 写入持久存储 |
- 不需要并发保证时，也可能需要关系型系统：SQLite、DuckDB。在 SQL 中：[[transactions]]。
""",
  see=["transactions", "bad-storage"])

S("model", "The relational model", "关系模型")
c("relational-model", "Entities, attributes, records", "实体、属性、记录", exam=True,
  en=r"""
| Concept | Example | In a relational DB |
|---|---|---|
| **entity** (type of thing) | Student, Building, Event | a **table** |
| **attribute** | name, address, capacity | a **column** |
| **record** (instance) | 'MVB', Woodland Rd, 400 | a **row** |
| **relationship** | student *studies in* building | columns that **refer to other tables** ([[foreign-key]]) |
- "Relational": tables have columns that reference rows of other tables. How to identify a row? Not "the 4th row" (order changes, rows deleted) → [[keys]].
""",
  zh=r"""
| 概念 | 例子 | 在关系数据库中 |
|---|---|---|
| **实体**（一类事物） | 学生、建筑、活动 | 一张**表** |
| **属性** | 名称、地址、容量 | 一**列** |
| **记录**（实例） | 'MVB'、Woodland Rd、400 | 一**行** |
| **联系** | 学生*在*某建筑上课 | **引用其他表**的列（[[foreign-key]]） |
- “关系型”：表中的列引用其他表的行。怎样标识一行？不能用“第 4 行”（顺序会变、行会被删）→ [[keys]]。
""",
  see=["keys", "er-diagram"])

c("er-diagram", "ER diagrams & cardinality", "ER 图与基数", exam=True,
  en=r"""
- Entity-relationship diagram: tables as boxes with attributes; relationships as lines whose ends show **cardinality** (one / many) and whether they are **mandatory or optional**. Tools: pen and paper, draw.io ("Entity Relation" section).
| Relationship | Implement as |
|---|---|
| one-to-one | FK on either side (usually the optional side), `UNIQUE` |
| one-to-many | FK on the **many** side (e.g. Lecturer → ResearchGroup FK is on Lecturer) |
| many-to-many | a separate **join table** holding two FKs (e.g. Enrolment(student, unit)) |
- Lab: HovSoc (members, committee roles, events with organiser & attendees); university marks (actual vs agreed mark after the exam board). Key rule: **store each fact once** — otherwise updates leave contradictions.
""",
  zh=r"""
- 实体-联系图：表画成带属性的方框；联系画成连线，两端标明**基数**（一 / 多）以及是**必选还是可选**。工具：纸笔、draw.io（“Entity Relation” 分类）。
| 联系 | 实现方式 |
|---|---|
| 一对一 | 外键放任一侧（通常放可选一侧），加 `UNIQUE` |
| 一对多 | 外键放在**多**的一侧（如“讲师属于研究组”，外键在 Lecturer 表） |
| 多对多 | 单独的**连接表**，存两个外键（如 Enrolment(student, unit)） |
- 实验：HovSoc 社团（成员、委员会职位、带组织者和参与者的活动）；大学成绩（考试委员会前的原始分与确认分）。核心原则：**每个事实只存一次**——否则更新时会产生矛盾。
""",
  see=["relational-model", "foreign-key", "create-table"])

S("keys", "Keys", "键")
c("keys", "Keys: candidate, composite, surrogate, primary", "键：候选键、复合键、代理键、主键", exam=True,
  en=r"""
- A **key** = a combination of attributes that uniquely identifies a row.
| Term | Meaning |
|---|---|
| candidate key | a **minimal** set of attributes that uniquely identifies records (one of possibly several) |
| composite key | a key made of **more than one** attribute (e.g. Location + Time) |
| surrogate key | an attribute invented only to be a key (Transaction ID, DegreeID) |
| primary key | the key you actually chose for the table |
| foreign key | a primary key of one table used as a reference in another ([[foreign-key]]) |
""",
  zh=r"""
- **键** = 能唯一标识一行的属性组合。
| 术语 | 含义 |
|---|---|
| 候选键 candidate key | 能唯一标识记录的**最小**属性集（可能有多个） |
| 复合键 composite key | 由**多于一个**属性组成的键（如 地点 + 时间） |
| 代理键 surrogate key | 专门为了做键而创造的属性（交易号、DegreeID） |
| 主键 primary key | 表实际选用的那个键 |
| 外键 foreign key | 某表的主键在另一表中作为引用（[[foreign-key]]） |
""",
  see=["foreign-key", "functional-dependency", "create-table"])

c("foreign-key", "Foreign keys", "外键", exam=True,
  en=r"""
- Student.`Studies` references Degree.`DegreeID` (Degree's PK) → each student row points at one degree row.
| DegreeID | Name | School | Duration |
|---|---|---|---|
| 1001 | Computer Science | COMS | 3 years |
| 1002 | Mathematics | MATH | 4 years |
| StudentNo | Name | Fee Status | Studies |
|---|---|---|---|
| 345212 | Bloggs, Joe | Paid | 1002 |
| 341215 | Doe, Jane | Paid | 1001 |
- Enforced in SQLite only after `PRAGMA foreign_keys = ON;` ([[create-table]]). Natural columns to [[join]] on.
""",
  zh=r"""
- Student 表的 `Studies` 引用 Degree 表的 `DegreeID`（Degree 的主键）→ 每个学生行指向一个专业行。
| DegreeID | Name | School | Duration |
|---|---|---|---|
| 1001 | Computer Science | COMS | 3 years |
| 1002 | Mathematics | MATH | 4 years |
| StudentNo | Name | Fee Status | Studies |
|---|---|---|---|
| 345212 | Bloggs, Joe | Paid | 1002 |
| 341215 | Doe, Jane | Paid | 1001 |
- SQLite 中只有执行 `PRAGMA foreign_keys = ON;` 后才强制检查（[[create-table]]）。也是[[join]]时最自然的连接列。
""",
  see=["keys", "join", "er-diagram"])

S("nf", "Normalisation", "规范化")
c("functional-dependency", "Functional dependencies", "函数依赖", exam=True,
  en=r"""
- **X → Y** (X functionally determines Y) iff for every value of X there is **at most one** value of Y. E.g. StudentID → Grade (many students may share a grade). It's a feature of the process generating the data, not a coincidence of the current rows.
- **Partial** dependency: a non-key attribute depends on only **part** of a composite key. UnitResults(*StudentID, *Unit*, Hairstyle, Grade, HairStyleRating): Hairstyle depends on StudentID alone.
- **Transitive** dependency: X → Y → Z, so Z depends on X only *through* Y (Hairstyle → HairStyleRating).
""",
  zh=r"""
- **X → Y**（X 函数决定 Y）当且仅当对 X 的每个值，Y **至多有一个**值。如 StudentID → Grade（多个学生可以同分）。这是产生数据的过程本身的性质，而不是当前数据碰巧如此。
- **部分**依赖：某个非键属性只依赖复合键的**一部分**。UnitResults(*StudentID, *Unit, Hairstyle, Grade, HairStyleRating)：Hairstyle 只依赖 StudentID。
- **传递**依赖：X → Y → Z，Z 只是*通过* Y 依赖 X（Hairstyle → HairStyleRating）。
""",
  see=["normal-forms", "keys"])

c("normal-forms", "Normal forms 0NF → BCNF", "范式 0NF → BCNF", exam=True,
  en=r"""
- Higher normal forms remove **redundancy**, which makes updates safe and queries easier (usually; over-normalisation has costs). 0NF > 1NF > 2NF > 3NF > BCNF > 4NF > 5NF > 6NF.
| Form | Requirement |
|---|---|
| 0NF / UNF | no duplicate records |
| 1NF | + every attribute **atomic** (no lists inside a cell) |
| 2NF | + no **partial** dependencies of non-key attributes on candidate keys |
| 3NF | + no **transitive** dependencies of non-key attributes on candidate keys |
| BCNF (3.5NF) | + every attribute depends on **the whole key and only the whole key** (catches overlapping composite candidate keys) |
| 4NF / 5NF / 6NF | multi-valued deps only on keys / no trivial lossless decomposition / one key + ≤1 attribute per table — rarely needed |
- Typical fix each time: **extract** the offending attributes into a new table and reference it with a foreign key.
""",
  zh=r"""
- 更高的范式消除**冗余**，让更新更安全、查询更方便（通常如此；过度规范化也有代价）。0NF > 1NF > 2NF > 3NF > BCNF > 4NF > 5NF > 6NF。
| 范式 | 要求 |
|---|---|
| 0NF / UNF | 没有重复记录 |
| 1NF | + 每个属性都是**原子**的（单元格里没有列表） |
| 2NF | + 非键属性对候选键没有**部分**依赖 |
| 3NF | + 非键属性对候选键没有**传递**依赖 |
| BCNF（3.5NF） | + 每个属性都依赖**整个键，且只依赖整个键**（能抓到复合候选键重叠的情况） |
| 4NF / 5NF / 6NF | 多值依赖只在键上 / 不能无损地平凡分解 / 每表一个键 + 至多一个属性——很少需要 |
- 每一步的典型修法：把出问题的属性**拆**到新表中，再用外键引用。
""",
  see=["nf-example", "functional-dependency", "keys"])

c("nf-example", "Worked example: the Event table", "实例：Event 表逐步规范化", exam=True,
  en=r"""
- Start (0NF): Event(*Location, *Time, Organiser, OrganiserEmail, Attendees, SafetyOfficer, Name) with Attendees = "jay; rob; mary".
| Step | Problem | Fix |
|---|---|---|
| 0NF → 1NF | Attendees is a list (not atomic) | new table EventAttendances(Attendee, EventLoc, EventTime), FK → Event |
| 1NF → 2NF | SafetyOfficer depends only on Location (part of the key) | new table LocationSafety(*Location, SafetyOfficer) |
| 2NF → 3NF | Organiser depends on OrganiserEmail (transitive) | new table Organiser(*OrganiserEmail, Name); keep OrganiserEmail in Event as FK |
| 3NF | Event(*Location, *Time, OrganiserEmail, Name) | also BCNF: only dependency is on the candidate key |
- Win: Rob Money's name is no longer repeated; "which events did jay attend?" is a lookup, not a text search.
""",
  zh=r"""
- 起点（0NF）：Event(*Location, *Time, Organiser, OrganiserEmail, Attendees, SafetyOfficer, Name)，其中 Attendees = "jay; rob; mary"。
| 步骤 | 问题 | 修法 |
|---|---|---|
| 0NF → 1NF | Attendees 是列表（不原子） | 新表 EventAttendances(Attendee, EventLoc, EventTime)，外键 → Event |
| 1NF → 2NF | SafetyOfficer 只依赖 Location（键的一部分） | 新表 LocationSafety(*Location, SafetyOfficer) |
| 2NF → 3NF | Organiser 依赖 OrganiserEmail（传递依赖） | 新表 Organiser(*OrganiserEmail, Name)；Event 中保留 OrganiserEmail 作外键 |
| 3NF | Event(*Location, *Time, OrganiserEmail, Name) | 同时满足 BCNF：唯一的依赖就是对候选键的依赖 |
- 好处：Rob Money 的名字不再重复出现；“jay 参加过哪些活动？”变成查表，而不是文本搜索。
""",
  see=["normal-forms", "create-table"])

S("ddl", "Creating tables in SQLite", "在 SQLite 中建表")
c("sqlite-cli", "The sqlite3 shell", "sqlite3 命令行",
  en=r"""
- `sqlite3 test.db` opens (creates) a database file; `sqlite3` alone = temporary in-memory DB.
- Dot-commands (not SQL): `.tables`, `.schema [table]`, `.headers on`, `.mode column`, `.quit`. Also `ATTACH DATABASE 'x.db' AS x;`.
- Run a script: `sqlite3 test.db < myscript.sql` (without a file name nothing persists).
- Convention: CAPITALISE SQL keywords; statements end with `;`.
""",
  zh=r"""
- `sqlite3 test.db` 打开（或新建）数据库文件；只写 `sqlite3` = 临时的内存数据库。
- 点命令（不是 SQL）：`.tables`、`.schema [表]`、`.headers on`、`.mode column`、`.quit`。还有 `ATTACH DATABASE 'x.db' AS x;`。
- 运行脚本：`sqlite3 test.db < myscript.sql`（不给文件名则不会持久保存）。
- 约定：SQL 关键字大写；语句以 `;` 结尾。
""",
  see=["create-table", "redirection"])

c("create-table", "CREATE TABLE", "CREATE TABLE 建表", exam=True,
  en=r"""
- Columns with types and constraints; `PRIMARY KEY` on a column, or `PRIMARY KEY(a, b)` at the end for a **composite** key.
- `FOREIGN KEY(col) REFERENCES other(col)` must be declared at creation → create the **referenced** table first.
- Turn on enforcement: `PRAGMA foreign_keys = ON;` (then inserting a non-existent degree fails).
- CREATE/DROP script: start with `DROP TABLE IF EXISTS t;` lines in the **reverse** of creation order (drop referencing tables first), then the CREATEs → re-running always gives fresh empty tables.
""",
  zh=r"""
- 列带类型和约束；`PRIMARY KEY` 写在列后，或在末尾写 `PRIMARY KEY(a, b)` 定义**复合**主键。
- `FOREIGN KEY(列) REFERENCES 另一表(列)` 必须在建表时声明 → 先建**被引用**的表。
- 开启外键检查：`PRAGMA foreign_keys = ON;`（之后插入不存在的专业号会失败）。
- 建表/删表脚本：先按建表**相反**顺序写 `DROP TABLE IF EXISTS t;`（先删引用别人的表），再写各个 CREATE → 每次重跑都得到全新的空表。
""",
  code=r"""
PRAGMA foreign_keys = ON;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS degree;
CREATE TABLE degree (degreeID INTEGER UNIQUE PRIMARY KEY,
                     name TEXT, school TEXT, durationYears INTEGER);
CREATE TABLE student (studentNo INTEGER UNIQUE PRIMARY KEY,
                      name TEXT, feeStatus TEXT, studies INTEGER,
                      FOREIGN KEY(studies) REFERENCES degree(degreeID));
""",
  see=["insert", "foreign-key", "sqlite-types", "sqlite-cli"])

c("insert", "INSERT INTO", "INSERT INTO 插入", exam=True,
  en=r"""
- `INSERT INTO degree VALUES (1001, 'Computer Science', 'COMS', 3);` — values in column order. Name columns explicitly: `INSERT INTO t(a, b) VALUES (…)`.
- Several rows at once: `VALUES (…), (…), (…);`.
- Inserting a row whose primary key already exists fails (UNIQUE constraint) — why running the single inserts *and then* the multi-row insert fails.
- Check: `SELECT * FROM degree;`.
""",
  zh=r"""
- `INSERT INTO degree VALUES (1001, 'Computer Science', 'COMS', 3);`——按列顺序给值。也可显式指定列：`INSERT INTO t(a, b) VALUES (…)`。
- 一次插入多行：`VALUES (…), (…), (…);`。
- 插入主键已存在的行会失败（UNIQUE 约束）——这就是先逐条插入、*再*执行多行插入会失败的原因。
- 检查：`SELECT * FROM degree;`。
""",
  code=r"""
INSERT INTO degree VALUES (1001, 'Computer Science', 'COMS', 3),
                          (1002, 'Mathematics', 'MATH', 4),
                          (1003, 'Engineering', 'ENG', 3);
""",
  see=["create-table", "upsert", "select"])

for n, e, z, k in [
    ("sqlite3 FILE.db [< script.sql]", "open DB / run script", "打开数据库 / 执行脚本", "sqlite-cli"),
    (".tables .schema .headers on .mode column", "sqlite3 dot-commands", "sqlite3 点命令", "sqlite-cli"),
    ("CREATE TABLE t (… PRIMARY KEY …)", "create a table", "建表", "create-table"),
    ("PRIMARY KEY(a, b)", "composite primary key", "复合主键", "create-table"),
    ("FOREIGN KEY(x) REFERENCES t(y)", "foreign key", "外键", "foreign-key"),
    ("PRAGMA foreign_keys = ON;", "enforce foreign keys", "强制外键约束", "create-table"),
    ("DROP TABLE IF EXISTS t;", "remove table if present", "存在则删表", "create-table"),
    ("INSERT INTO t VALUES (…), (…);", "add rows", "插入行", "insert"),
]:
    cmd(n, e, z, k)

# =====================================================================  W9
W(9)
S("types", "Types & constraints", "类型与约束")
c("sqlite-types", "SQLite type affinity", "SQLite 类型亲和性", exam=True,
  en=r"""
- Most SQL engines type columns strictly and offer `BOOLEAN`, `CHARACTER(10)`, `DATE`… SQLite is **relaxed**: accepts those keywords but translates/ignores them.
- Each column has an **affinity**: `INTEGER`, `TEXT`, `BLOB`, `REAL`, or `NUMERIC` (mix); any value may be `NULL`. Values are converted to the preferred type when possible: `INSERT INTO t1(a,b) VALUES('123',456)` with `a INT, b VARCHAR(10)` stores 123 and '456'.
- `BOOLEAN` → stored as INTEGER; `CHAR`/`VARCHAR` lengths are **ignored** → enforce with [[constraints|CHECK]].
""",
  zh=r"""
- 多数 SQL 引擎对列类型严格，并提供 `BOOLEAN`、`CHARACTER(10)`、`DATE`…… SQLite 很**宽松**：接受这些关键字，但会转换或忽略。
- 每列有一种**亲和类型**：`INTEGER`、`TEXT`、`BLOB`、`REAL` 或 `NUMERIC`（混合）；任何值都可以是 `NULL`。能转换时会转换成偏好的类型：列 `a INT, b VARCHAR(10)` 执行 `INSERT INTO t1(a,b) VALUES('123',456)` 存的是 123 和 '456'。
- `BOOLEAN` → 以 INTEGER 存储；`CHAR`/`VARCHAR` 的长度被**忽略** → 用[[constraints|CHECK]]约束实现。
""",
  see=["constraints", "create-table"])

c("constraints", "Constraints: CHECK, NOT NULL, UNIQUE, DEFAULT", "约束：CHECK、NOT NULL、UNIQUE、DEFAULT", exam=True,
  en=r"""
- `CHECK(length(shortname) <= 10)` reimplements `CHARACTER(10)`: violating inserts fail with "CHECK constraint failed".
- CHECKs can involve several attributes: `CHECK(length(shortname) <= length(name))`.
- `NOT NULL` forbids missing values; `UNIQUE` forbids duplicates; `DEFAULT 1` supplies a value.
- Constraints = the "C" (consistency) in [[acid]].
""",
  zh=r"""
- `CHECK(length(shortname) <= 10)` 重新实现了 `CHARACTER(10)`：违反的插入会报 “CHECK constraint failed”。
- CHECK 可以涉及多个属性：`CHECK(length(shortname) <= length(name))`。
- `NOT NULL` 禁止缺失值；`UNIQUE` 禁止重复；`DEFAULT 1` 提供默认值。
- 约束就是 [[acid]] 中的 “C”（一致性）。
""",
  code=r"""
CREATE TABLE degree (degreeID INTEGER UNIQUE PRIMARY KEY,
                     name TEXT NOT NULL, shortname TEXT,
                     school TEXT, durationYears INTEGER,
                     CHECK(length(shortname) <= 10));
""",
  see=["sqlite-types", "acid"])

S("select", "SELECT", "SELECT 查询")
c("select", "SELECT, ORDER BY, LIMIT", "SELECT、ORDER BY、LIMIT", exam=True,
  en=r"""
- `SELECT * FROM Customer;` all columns. Choose **result columns**: `SELECT CustomerId, FirstName, Email FROM Customer`.
- `LIMIT 10` caps the rows; `ORDER BY FirstName [ASC|DESC]` sorts — ORDER BY comes **before** LIMIT.
- `DISTINCT` removes duplicate result rows; `AS` renames a column or table (alias).
- The SELECT syntax diagram is so complex the SQLite docs also give a simplified one. Practice DB: `sqlite3 chinook.db`.
""",
  zh=r"""
- `SELECT * FROM Customer;` 所有列。选择**结果列**：`SELECT CustomerId, FirstName, Email FROM Customer`。
- `LIMIT 10` 限制行数；`ORDER BY FirstName [ASC|DESC]` 排序——ORDER BY 写在 LIMIT **之前**。
- `DISTINCT` 去掉重复结果行；`AS` 给列或表起别名。
- SELECT 的语法图复杂到 SQLite 文档还另给了简化版。练习库：`sqlite3 chinook.db`。
""",
  code=r"""
SELECT CustomerId, FirstName, LastName, Email
FROM Customer
ORDER BY FirstName DESC
LIMIT 10;
""",
  see=["where", "aggregate", "select-order"])

c("where", "WHERE filters", "WHERE 过滤", exam=True,
  en=r"""
- Only rows matching the expression are returned: `WHERE Country='France'`, combine with `AND` / `OR`.
- `LIKE` with wildcards: `%` any string, `_` one character (`Email LIKE '%yahoo%'`).
- Comparisons `< <= > >= = !=`; sets `IN ('France','Germany')`; missing values `IS NULL` / `IS NOT NULL` (not `= NULL`).
""",
  zh=r"""
- 只返回满足表达式的行：`WHERE Country='France'`，用 `AND` / `OR` 组合。
- `LIKE` 通配：`%` 任意字符串，`_` 一个字符（`Email LIKE '%yahoo%'`）。
- 比较 `< <= > >= = !=`；集合 `IN ('France','Germany')`；空值用 `IS NULL` / `IS NOT NULL`（不能写 `= NULL`）。
""",
  code=r"""
SELECT CustomerId, City FROM Customer WHERE Country='France' AND City='Paris';
SELECT CustomerId, Email FROM Customer WHERE Email LIKE '%yahoo%';
SELECT CustomerId, Country FROM Customer WHERE Country IN ('France','Germany');
""",
  see=["select", "having", "sql-injection"])

S("agg", "Aggregates", "聚合")
c("aggregate", "Aggregates & GROUP BY", "聚合函数与 GROUP BY", exam=True,
  en=r"""
- **Aggregate query**: uses an aggregate function or `GROUP BY`. Functions: `count()`, `avg()`, `sum()`, `min()`, `max()` (`count(*)` counts rows; `count(col)` ignores NULLs).
- Without GROUP BY the whole table is one group; a non-aggregated column then gives an ill-defined single value (`SELECT avg(CustomerId), Country FROM Customer` is meaningless).
- `GROUP BY col` applies the aggregate **within each group**: `SELECT count(Country), Country FROM Customer GROUP BY Country;`. Several columns → cross-tabulation.
- GROUP BY is applied **after** WHERE. NULLs form their own group — filter with `WHERE x IS NOT NULL`.
""",
  zh=r"""
- **聚合查询**：用了聚合函数或 `GROUP BY`。函数：`count()`、`avg()`、`sum()`、`min()`、`max()`（`count(*)` 数行；`count(列)` 忽略 NULL）。
- 没有 GROUP BY 时整张表是一个组；此时未聚合的列只给出一个含义不明的值（`SELECT avg(CustomerId), Country FROM Customer` 没有意义）。
- `GROUP BY 列` 让聚合在**每个组内**计算：`SELECT count(Country), Country FROM Customer GROUP BY Country;`。多列分组 → 交叉统计。
- GROUP BY 在 WHERE **之后**进行。NULL 会单独成为一组——用 `WHERE x IS NOT NULL` 过滤。
""",
  code=r"""
SELECT count(CustomerId), Country, SupportRepId
FROM Customer GROUP BY SupportRepId, Country;
SELECT count(Company), Company FROM Customer
WHERE Company IS NOT NULL GROUP BY Company;
""",
  see=["having", "subquery", "select-order"])

c("having", "HAVING", "HAVING 分组过滤", exam=True,
  en=r"""
- Filters **groups after** GROUP BY; `WHERE` filters **rows before** grouping.
- Sometimes interchangeable (`HAVING Country = 'Germany'`), but conditions on aggregates need HAVING: `HAVING NoCustomers > 2` — the alias doesn't exist until grouping.
""",
  zh=r"""
- 在 GROUP BY **之后过滤组**；`WHERE` 在分组**之前过滤行**。
- 有时二者可互换（`HAVING Country = 'Germany'`），但针对聚合结果的条件必须用 HAVING：`HAVING NoCustomers > 2`——这个别名在分组之前并不存在。
""",
  code=r"""
SELECT count(CustomerId) AS NoCustomers, Country, SupportRepId
FROM Customer
GROUP BY SupportRepId, Country
HAVING NoCustomers > 2;
""",
  see=["aggregate", "where"])

S("join", "Joins", "连接")
c("join", "JOIN … ON", "JOIN … ON 连接", exam=True,
  en=r"""
- Normalisation spreads information over tables; a **join** builds a temporary combined table to SELECT FROM.
- `FROM Employee JOIN Customer ON Employee.EmployeeId = Customer.SupportRepId` — usually join on a **foreign key** = primary key.
- The join happens **before** WHERE and column selection. Qualify ambiguous columns: `Customer.FirstName`; alias with `AS`.
""",
  zh=r"""
- 规范化让信息分散在多张表；**连接**构造一张临时的组合表供 SELECT 查询。
- `FROM Employee JOIN Customer ON Employee.EmployeeId = Customer.SupportRepId`——通常按**外键** = 主键连接。
- 连接发生在 WHERE 和选列**之前**。有歧义的列要加表名：`Customer.FirstName`；可用 `AS` 起别名。
""",
  code=r"""
SELECT Customer.FirstName, Customer.LastName, Employee.FirstName, Employee.LastName
FROM Employee JOIN Customer ON Employee.EmployeeId = Customer.SupportRepId
WHERE Customer.Country = 'Germany' AND Employee.ReportsTo = 2;

SELECT Album.Title AS AlbumTitle, Artist.Name AS ArtistName
FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId
WHERE Artist.Name LIKE 'Al%' OR Album.Title LIKE 'Al%';
""",
  see=["join-types", "foreign-key", "self-join"])

c("join-types", "Types of join", "连接的类型", exam=True,
  en=r"""
| Join (a ⋈ b on a.id = b.id) | Rows from a | Rows from b | Good for |
|---|---|---|---|
| `INNER JOIN` (default `JOIN`) | only with a match | only with a match | only matches |
| `LEFT [OUTER] JOIN` | **all** | only matches | all a, b optional |
| `RIGHT [OUTER] JOIN` | only matches | **all** | all b, a optional |
| `FULL [OUTER] JOIN` | **all** | **all** | either optional |
| `CROSS JOIN` (no ON) | every a × every b | | Cartesian product |
- OUTER joins fill the missing side with NULL. FULL = every record of a or b at least once; CROSS pairs everything with everything, no matching.
""",
  zh=r"""
| 连接（a ⋈ b，条件 a.id = b.id） | a 中的行 | b 中的行 | 适用 |
|---|---|---|---|
| `INNER JOIN`（默认 `JOIN`） | 只保留有匹配的 | 只保留有匹配的 | 只要匹配 |
| `LEFT [OUTER] JOIN` | **全部** | 只保留匹配 | 要全部 a，b 可无 |
| `RIGHT [OUTER] JOIN` | 只保留匹配 | **全部** | 要全部 b，a 可无 |
| `FULL [OUTER] JOIN` | **全部** | **全部** | 两边都可无 |
| `CROSS JOIN`（无 ON） | 每个 a × 每个 b | | 笛卡尔积 |
- 外连接用 NULL 填补缺失的一侧。FULL = a 或 b 的每条记录至少出现一次；CROSS 把所有行两两配对，不做匹配。
""",
  see=["join", "subquery"])

S("sub", "Sub-queries", "子查询")
c("subquery", "Sub-queries", "子查询", exam=True,
  en=r"""
- Use the result of one SELECT as a **temporary table** for another: `SELECT … FROM (SELECT … GROUP BY …);` — e.g. aggregate an aggregate (albums per artist on average).
- Alternatives: `CREATE TEMPORARY TABLE x AS SELECT …`; sub-query in WHERE: `WHERE id IN (SELECT …)`.
- Stick two results together vertically: `SELECT … UNION SELECT …` (lab: smallest and largest ward in one table).
- Why `RIGHT JOIN` in the example: keep artists with **zero** albums.
""",
  zh=r"""
- 把一个 SELECT 的结果当作另一个查询的**临时表**：`SELECT … FROM (SELECT … GROUP BY …);`——如对聚合结果再聚合（每位艺术家平均专辑数）。
- 其它方式：`CREATE TEMPORARY TABLE x AS SELECT …`；在 WHERE 中用子查询：`WHERE id IN (SELECT …)`。
- 把两个结果纵向拼起来：`SELECT … UNION SELECT …`（实验：最小和最大的选区放在一张表里）。
- 例子中为什么用 `RIGHT JOIN`：保留专辑数为**零**的艺术家。
""",
  code=r"""
SELECT sum(Albums) AS Albums, count(Name) AS Artists,
       round(avg(Albums), 2) AS AlbumsPerArtist
FROM (SELECT count(Album.Title) AS Albums, Artist.Name
      FROM Album RIGHT JOIN Artist ON Album.ArtistId = Artist.ArtistId
      GROUP BY Artist.Name);
""",
  see=["aggregate", "join-types", "recursive-cte"])

c("select-order", "How to build a SELECT", "如何构造 SELECT", exam=True,
  en=r"""
- Work through in this order:
| # | Clause | Ask |
|---|---|---|
| 1 | `FROM` | which table? a JOIN or a sub-query? |
| 2 | `SELECT` | which columns? aggregate → need `GROUP BY`? |
| 3 | `WHERE` | which rows? on aggregates → `HAVING` |
| 4 | `ORDER BY` / `LIMIT` | sort? how many? |
- Logical evaluation: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT. Written: SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT.
- Lab rule: one query per question, join on names rather than hard-coding IDs. Experiment in the shell, save finished queries in a script.
""",
  zh=r"""
- 按这个顺序思考：
| # | 子句 | 要问的问题 |
|---|---|---|
| 1 | `FROM` | 从哪张表？需要 JOIN 还是子查询？ |
| 2 | `SELECT` | 要哪些列？用了聚合 → 需要 `GROUP BY`？ |
| 3 | `WHERE` | 要哪些行？针对聚合结果 → 用 `HAVING` |
| 4 | `ORDER BY` / `LIMIT` | 排序吗？要几行？ |
- 逻辑执行顺序：FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT。书写顺序：SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT。
- 实验要求：每题一个查询，按名称连接而不是硬编码 ID。在命令行里试，把写好的查询存进脚本。
""",
  see=["select", "where", "aggregate", "having", "join"])

S("maint", "Changing data", "修改数据")
c("upsert", "ALTER TABLE, UPDATE & upsert", "ALTER TABLE、UPDATE 与 upsert", exam=True,
  en=r"""
- `ALTER TABLE` renames a table, adds/removes/redefines columns.
- `UPDATE t SET col = value WHERE …;` changes existing records (forget WHERE = every row). `DELETE FROM t WHERE …;` removes them.
- **Upsert**: `INSERT … ON CONFLICT(col) DO UPDATE SET …` = insert, or update if the key already exists.
""",
  zh=r"""
- `ALTER TABLE` 重命名表，增加/删除/重新定义列。
- `UPDATE t SET 列 = 值 WHERE …;` 修改已有记录（忘了 WHERE = 改所有行）。`DELETE FROM t WHERE …;` 删除记录。
- **Upsert**：`INSERT … ON CONFLICT(列) DO UPDATE SET …` = 插入，若键已存在则改为更新。
""",
  code=r"""
CREATE TABLE vocabulary(word TEXT PRIMARY KEY, count INT DEFAULT 1);
INSERT INTO vocabulary(word) VALUES('jovial')
  ON CONFLICT(word) DO UPDATE SET count = count + 1;
""",
  see=["insert", "transactions"])

c("transactions", "Transactions", "事务", exam=True,
  en=r"""
- Group statements so that **all** complete successfully or **none** do — keeps ACID consistency in concurrent applications.
- `BEGIN TRANSACTION; … INSERTs / UPDATEs …; END TRANSACTION;` (`COMMIT` = END; `ROLLBACK` abandons).
""",
  zh=r"""
- 把多条语句打包：要么**全部**成功，要么**全都**不生效——在并发应用中保持 ACID 一致性。
- `BEGIN TRANSACTION; … 若干 INSERT / UPDATE …; END TRANSACTION;`（`COMMIT` 等同 END；`ROLLBACK` 放弃）。
""",
  see=["acid", "upsert"])

for n, e, z, k in [
    ("SELECT cols FROM t", "choose columns", "选择列", "select"),
    ("ORDER BY c [DESC] LIMIT n", "sort / cap rows", "排序 / 限制行数", "select"),
    ("SELECT DISTINCT; AS alias", "unique rows / rename", "去重 / 别名", "select"),
    ("WHERE … AND/OR … LIKE '%x%' IN (…) IS NULL", "filter rows", "过滤行", "where"),
    ("count avg sum min max", "aggregate functions", "聚合函数", "aggregate"),
    ("GROUP BY c HAVING cond", "group / filter groups", "分组 / 过滤组", "having"),
    ("a JOIN b ON a.x = b.y", "inner join", "内连接", "join"),
    ("LEFT / RIGHT / FULL OUTER / CROSS JOIN", "other joins", "其它连接", "join-types"),
    ("FROM (SELECT …)", "sub-query as table", "子查询当表", "subquery"),
    ("SELECT … UNION SELECT …", "stack two results", "合并两组结果", "subquery"),
    ("CHECK(…) NOT NULL UNIQUE DEFAULT", "column constraints", "列约束", "constraints"),
    ("UPDATE t SET c=v WHERE …", "change rows", "修改行", "upsert"),
    ("ALTER TABLE", "change a table's structure", "修改表结构", "upsert"),
    ("INSERT … ON CONFLICT DO UPDATE", "upsert", "插入或更新", "upsert"),
    ("BEGIN TRANSACTION … END TRANSACTION", "all-or-nothing block", "全有或全无", "transactions"),
    ("ATTACH DATABASE 'f.db' AS x", "use several DB files", "同时使用多个库", "sqlite-cli"),
]:
    cmd(n, e, z, k)

# =====================================================================  W10
W(10)
S("code", "Using SQL from a program", "在程序中使用 SQL")
c("sql-from-code", "Database libraries", "数据库接口库",
  en=r"""
- You don't write applications in SQL: it's a domain-specific query language, not (in standard form) Turing-complete, and bad at recursion.
- Languages provide libraries that talk to the DB engine: Python `import sqlite3`; Java `java.sql.*` + `DriverManager.getConnection("jdbc:sqlite:<db>")`; C `sqlite3_open`, `sqlite3_exec`.
""",
  zh=r"""
- 不会用 SQL 写应用程序：它是专门用于查询的领域语言，（标准形式下）不是图灵完备的，也不擅长递归。
- 各种语言提供与数据库引擎通信的库：Python `import sqlite3`；Java `java.sql.*` + `DriverManager.getConnection("jdbc:sqlite:<db>")`；C 语言 `sqlite3_open`、`sqlite3_exec`。
""",
  see=["sql-injection", "prepared-statements"])

c("sql-injection", "SQL injection", "SQL 注入", exam=True,
  en=r"""
- Appointment checker v1 builds the query from user input: `sprintf(sql, "SELECT * FROM Appointment WHERE AppointmentID = %s;", appointmentID);`
- Input `1 OR 1=1` → `WHERE AppointmentID = 1 OR 1=1` → always true → **every** appointment returned. Attackers who know SQL can read or modify the DB at will (xkcd "Bobby Tables": `'); DROP TABLE Students;--`).
- Consistently in the OWASP Top Ten; estimated 10–33% of web application vulnerabilities.
""",
  zh=r"""
- 预约查询程序 v1 用用户输入拼出查询：`sprintf(sql, "SELECT * FROM Appointment WHERE AppointmentID = %s;", appointmentID);`
- 输入 `1 OR 1=1` → `WHERE AppointmentID = 1 OR 1=1` → 恒为真 → 返回**所有**预约。懂 SQL 的攻击者可以随意读取或修改数据库（xkcd “Bobby Tables”：`'); DROP TABLE Students;--`）。
- 长期位列 OWASP 十大风险；估计占 Web 应用漏洞的 10–33%。
""",
  see=["prepared-statements", "where", "fuzzing"])

c("prepared-statements", "Prepared statements", "预编译语句（参数化查询）", exam=True,
  en=r"""
- The fix: write the query with **placeholders** `?`, let the library **prepare** it, then **bind** user input as values. Input can no longer be parsed as SQL clauses.
- Effect: `1 OR 1=1` is treated like `WHERE AppointmentID = '1 OR 1=1'` (a value, matches nothing).
- Always use your DB library's prepared-statement API for user input.
""",
  zh=r"""
- 修复方法：用**占位符** `?` 写查询，让库先**预编译**，再把用户输入作为值**绑定**进去。输入再也不会被解析成 SQL 子句。
- 效果：`1 OR 1=1` 相当于 `WHERE AppointmentID = '1 OR 1=1'`（只是一个值，什么也匹配不到）。
- 处理用户输入时，一律使用数据库库提供的预编译语句接口。
""",
  code=r"""
sqlite3_stmt *stmt;
char *sql = "SELECT * FROM Appointment WHERE AppointmentID = ?";
retval = sqlite3_prepare_v2(db, sql, -1, &stmt, 0);
if (retval == SQLITE_OK)
    sqlite3_bind_text(stmt, 1, appointmentID, strlen(appointmentID), SQLITE_STATIC);
while (sqlite3_step(stmt) == SQLITE_ROW) { /* read columns */ }
sqlite3_finalize(stmt);
""",
  see=["sql-injection", "sql-from-code"])

S("rec", "SQL and recursion", "SQL 与递归")
c("self-join", "Self-joins", "自连接", exam=True,
  en=r"""
- `bosses.db`: table `manager(employee, manager)`. My manager: `SELECT manager FROM manager WHERE employee = 'Matthew Edwards';`.
- Manager's manager in one query = join the table **with itself**, naming the two sides (`a`, `b`).
- All managers? You can keep joining (c, d, …) but must know the depth in advance — 5 more layers? 24?
""",
  zh=r"""
- `bosses.db`：表 `manager(employee, manager)`。我的上级：`SELECT manager FROM manager WHERE employee = 'Matthew Edwards';`。
- 一次查出上级的上级 = 表**与自身**连接，并给两侧命名（`a`、`b`）。
- 查所有上级？可以一直连接下去（c、d……），但必须事先知道层数——再多 5 层？24 层？
""",
  code=r"""
SELECT a.manager, b.manager AS managermanager
FROM manager a JOIN manager b ON a.manager = b.employee
WHERE a.employee = 'Matthew Edwards';
""",
  see=["join", "recursive-data", "recursive-cte"])

c("recursive-data", "Recursive data structures", "递归数据结构",
  en=r"""
- Trees and graphs are efficient representations for: organisational hierarchies, file storage, process relationships.
- Storable in relational tables, but hard to **query** to arbitrary depth.
- What we want is simple: Y manages X if X reports directly to Y, **or** Y manages whoever X reports to → a recursive rule ([[datalog-recursion]]).
""",
  zh=r"""
- 树和图是这些问题的高效表示：组织层级、文件存储、进程关系。
- 可以存进关系表，但很难**查询**任意深度。
- 我们想要的其实很简单：若 X 直接向 Y 汇报，**或者** Y 管理 X 的直接上级，则 Y 管理 X → 一条递归规则（[[datalog-recursion]]）。
""",
  code=r"""
manages(Y, X) :- directreport(Y, X).
manages(Y, X) :- directreport(Z, X), manages(Y, Z).
""",
  see=["self-join", "datalog-recursion"])

c("recursive-cte", "WITH RECURSIVE (bonus)", "WITH RECURSIVE 递归查询（补充）",
  en=r"""
- SQL's escape hatch (file `recurse.sql` in the lecture folder): a recursive common table expression = base query `UNION` a step that joins the table with the CTE itself, repeated until no new rows.
""",
  zh=r"""
- SQL 的“后门”（讲义目录中的 `recurse.sql`）：递归公用表表达式 = 基础查询 `UNION` 一个把原表与该 CTE 自身连接的步骤，反复执行直到不再产生新行。
""",
  code=r"""
WITH RECURSIVE mymanagers(m) AS (
  SELECT manager FROM manager WHERE employee = 'Matthew Edwards'
  UNION
  SELECT manager FROM manager, mymanagers WHERE manager.employee = mymanagers.m)
SELECT * FROM mymanagers;
""",
  see=["self-join", "datalog-recursion", "subquery"])

S("dl", "Datalog", "Datalog")
c("datalog", "Datalog & deductive databases", "Datalog 与演绎数据库", exam=True,
  en=r"""
- A declarative logic-programming language; a strict **subset of Prolog** (Prolog interpreters accept the syntax, but evaluation differs).
- Core idea: declare **facts** and **rules** for deducing new facts → a flexible **deductive database**; then ask **queries**.
- Lab interpreter: **AbcDatalog** (`java -jar AbcDatalog-0.7.0.jar &`, a GUI → over SSH use `ssh -X`).
- Why learn it: you'll meet non-relational databases; it trains thinking about what to store, how, and how to query it; experience with logic programming.
""",
  zh=r"""
- 一种声明式逻辑编程语言；是 **Prolog 的严格子集**（Prolog 解释器接受其语法，但求值方式不同）。
- 核心思想：声明**事实**和推导新事实的**规则** → 灵活的**演绎数据库**；然后提出**查询**。
- 实验用解释器：**AbcDatalog**（`java -jar AbcDatalog-0.7.0.jar &`，有图形界面 → 通过 SSH 要用 `ssh -X`）。
- 为什么学：将来会遇到非关系型数据库；训练你思考存什么、怎么存、怎么查；体验逻辑编程。
""",
  see=["datalog-syntax", "horn-clauses", "ssh"])

c("datalog-syntax", "Datalog terms", "Datalog 的项", exam=True,
  en=r"""
| Kind | Rule | Examples |
|---|---|---|
| atom | starts lowercase, or quoted | `thisIsAnAtom`, `'This is also an Atom'` |
| variable | starts Uppercase or `_` | `ThisIsAVariable`, `_AlsoAVariable` |
| number | integer or float | `20`, `23.4` |
| compound term | atom + arguments | `compoundterm(thisIsATerm, someOtherTerm)` |
- Lists `[]` and strings `""` are fancy compound terms. Comments start with `%`. Clauses end with `.`.
""",
  zh=r"""
| 类别 | 规则 | 例子 |
|---|---|---|
| 原子 atom | 小写字母开头，或用引号括起 | `thisIsAnAtom`、`'This is also an Atom'` |
| 变量 variable | 大写字母或 `_` 开头 | `ThisIsAVariable`、`_AlsoAVariable` |
| 数字 | 整数或浮点数 | `20`、`23.4` |
| 复合项 compound term | 原子 + 参数 | `compoundterm(thisIsATerm, someOtherTerm)` |
- 列表 `[]` 和字符串 `""` 只是花哨的复合项。注释以 `%` 开头。每条子句以 `.` 结尾。
""",
  see=["horn-clauses"])

c("horn-clauses", "Facts, rules & queries (Horn clauses)", "事实、规则与查询（Horn 子句）", exam=True,
  en=r"""
- A Datalog program = list of **Horn clauses** `Head :- Body.` ("Head is true if Body is true").
- **Fact**: compound term with only atoms, known true: `human(socrates).` (short for `human(socrates) :- true.`).
- **Rule**: uses variables: `mortal(X) :- human(X).`; body conjuncts separated by `,` = **AND**; several rules with the same head = **OR**.
- **Query** in the interpreter: `?- human(socrates).` → `true`; `?- mortal(Y).` → `Y = socrates`.
- Lab (Addams family): `parent(pugsley, gomez)` = Pugsley's parent is Gomez; `grandparent(X,Z) :- parent(X,Y), parent(Y,Z).`; cousin = shares a grandparent but isn't a sibling; aunt/uncle = parent's sibling.
""",
  zh=r"""
- Datalog 程序 = 一串 **Horn 子句** `Head :- Body.`（“若 Body 为真，则 Head 为真”）。
- **事实**：只含原子的复合项，已知为真：`human(socrates).`（是 `human(socrates) :- true.` 的简写）。
- **规则**：含变量：`mortal(X) :- human(X).`；规则体中用 `,` 分隔 = **且**；同一个头的多条规则 = **或**。
- 在解释器中**查询**：`?- human(socrates).` → `true`；`?- mortal(Y).` → `Y = socrates`。
- 实验（亚当斯一家）：`parent(pugsley, gomez)` = Pugsley 的父母是 Gomez；`grandparent(X,Z) :- parent(X,Y), parent(Y,Z).`；堂表亲 = 有共同祖父母但不是兄弟姐妹；叔舅姑姨 = 父母的兄弟姐妹。
""",
  code=r"""
father_child(paul, rudy).   mother_child(zenith, rudy).
father_child(paul, norn).   mother_child(zenith, norn).
father_child(paul, aisha).  mother_child(lilia, aisha).
parent_child(X, Y) :- father_child(X, Y).
parent_child(X, Y) :- mother_child(X, Y).
sibling(X, Y) :- parent_child(Z, X), parent_child(Z, Y), X != Y.
?- sibling(rudy, X).
""",
  see=["datalog-syntax", "datalog-recursion", "datalog-negation"])

c("datalog-negation", "Inequality X != Y", "不等 X != Y",
  en=r"""
- Without it, `sibling(wednesday, wednesday)` is true (you share a parent with yourself). Add `X != Y` to the rule body.
- AbcDatalog supports such negation/inequality in rules.
""",
  zh=r"""
- 不加它的话，`sibling(wednesday, wednesday)` 为真（你和自己当然有共同父母）。在规则体中加上 `X != Y`。
- AbcDatalog 支持规则中的这类否定/不等。
""",
  see=["horn-clauses"])

c("datalog-recursion", "Recursive rules", "递归规则", exam=True,
  en=r"""
- A rule may refer to itself: a **base case** plus a **recursive case**.
- `ancestor(X,Y) :- parent_child(X,Y).` / `ancestor(X,Y) :- parent_child(X,Z), ancestor(Z,Y).` — same shape as `manages`.
- Translate `bosses.db` rows to facts `directreport('Inah Omoronyia', 'Matthew Edwards').` and `?- manages(X, 'Matthew Edwards').` finds **all** managers, any depth — what SQL joins couldn't.
""",
  zh=r"""
- 规则可以引用自身：一条**基础规则** + 一条**递归规则**。
- `ancestor(X,Y) :- parent_child(X,Y).` / `ancestor(X,Y) :- parent_child(X,Z), ancestor(Z,Y).`——与 `manages` 形状相同。
- 把 `bosses.db` 的记录转成事实 `directreport('Inah Omoronyia', 'Matthew Edwards').`，再查询 `?- manages(X, 'Matthew Edwards').` 就能找出任意深度的**所有**上级——这正是 SQL 连接做不到的。
""",
  see=["recursive-data", "self-join", "recursive-cte"])

S("acl", "Access control in Datalog", "用 Datalog 做访问控制")
c("datalog-access-control", "UNIX DAC in Datalog", "用 Datalog 表达 UNIX DAC", exam=True,
  en=r"""
- Classic Datalog use: **access control** — every decision can be made, in reasonable time.
- The lecture encodes the [[unix-dac|UNIX read rules]]: owner + user read bit; group member + group owns + group read bit; anyone + other read bit.
- Lab extensions: `file(X)`, `principal(X)`, `owner(F,P)`, `othersCanRead(F)`; **delegation** `saysCanRead(P1,P2,F)` (only valid if P1 owns F) and `delegatesTo(P1,P2)` (which can be re-delegated → recursion); **roles** `holds(P,R)`.
""",
  zh=r"""
- Datalog 的经典用途：**访问控制**——每个访问决策都一定能在合理时间内得出。
- 讲座把 [[unix-dac|UNIX 的读权限规则]]写成 Datalog：属主 + 属主读位；组成员 + 组拥有 + 组读位；任何人 + 其他人读位。
- 实验扩展：`file(X)`、`principal(X)`、`owner(F,P)`、`othersCanRead(F)`；**委托** `saysCanRead(P1,P2,F)`（仅当 P1 拥有 F 时有效）和 `delegatesTo(P1,P2)`（可以再次委托 → 递归）；**角色** `holds(P,R)`。
""",
  code=r"""
canRead(U,F) :- user(U), file(F), owns(U,F), userReadBitSet(F).
canRead(U,F) :- user(U), group(G), file(F), member(U,G), owns(G,F), groupReadBitSet(F).
canRead(U,F) :- user(U), file(F), otherReadBitSet(F).
user(matthew).  group(realusers).  member(matthew, realusers).
file('README.md').  owns(realusers, 'README.md').  groupReadBitSet('README.md').
""",
  see=["unix-dac", "mac-models", "horn-clauses"])

c("mac-models", "Mandatory access control: Bell–LaPadula & Biba", "强制访问控制：Bell–LaPadula 与 Biba",
  en=r"""
- **MAC**: the system, not the owner, decides — files have levels `unclassified < secret < topsecret`; principals have a clearance (`clearance(P, secret)`).
| Model | Protects | Read | Write |
|---|---|---|---|
| Bell–LaPadula | confidentiality | **read down**: clearance ≥ file level | **write up**: clearance ≤ file level (tell superiors, not peers) |
| Biba | integrity | **read up**: only from higher-integrity sources (not influenced from below) | **write down**: send orders to lower levels |
- Contrast with DAC, where the owner decides ([[unix-dac]]).
""",
  zh=r"""
- **MAC（强制访问控制）**：由系统而非属主决定——文件有密级 `unclassified < secret < topsecret`；主体有许可级别（`clearance(P, secret)`）。
| 模型 | 保护 | 读 | 写 |
|---|---|---|---|
| Bell–LaPadula | 机密性 | **向下读**：许可级别 ≥ 文件密级 | **向上写**：许可级别 ≤ 文件密级（可以告诉上级，不泄露给同级） |
| Biba | 完整性 | **向上读**：只从更高完整性来源读（不受下级影响） | **向下写**：向下级下达命令 |
- 与 DAC（属主决定，[[unix-dac]]）对比。
""",
  see=["datalog-access-control", "unix-dac"])

for n, e, z, k in [
    ("sqlite3_open / sqlite3_exec", "C: open DB / run SQL string", "C：打开库 / 执行 SQL 字符串", "sql-from-code"),
    ("sqlite3_prepare_v2 / bind_text / step", "C: prepared statement", "C：预编译语句", "prepared-statements"),
    ("... WHERE id = ?", "placeholder for a bound value", "绑定值的占位符", "prepared-statements"),
    ("FROM t a JOIN t b ON a.x = b.y", "self-join", "自连接", "self-join"),
    ("WITH RECURSIVE r(x) AS (… UNION …)", "recursive query", "递归查询", "recursive-cte"),
    ("java -jar AbcDatalog-0.7.0.jar &", "start the Datalog GUI", "启动 Datalog 图形界面", "datalog"),
    ("fact(a, b).", "a fact", "事实", "horn-clauses"),
    ("head(X) :- b1(X), b2(X).", "a rule (comma = AND)", "规则（逗号 = 且）", "horn-clauses"),
    ("?- p(X).", "a query", "查询", "horn-clauses"),
    ("X != Y", "inequality in a rule body", "规则体中的不等", "datalog-negation"),
]:
    cmd(n, e, z, k)
