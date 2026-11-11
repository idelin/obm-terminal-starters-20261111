# SQLite身份日志导出

先检查schema.sql、legacy_reader.py和data/export.sqlite，保留既有投影行为。main.py提供逐行JSON匿名化入口；export.py提供数据库快照到匿名化SQLite库及JSONL的发布入口。完整接口、输出结构与预算见proposal的C_agent_task。

运行python3 main.py，或python3 export.py data/export.sqlite demo out。Python3.12标准库即可，不需安装包；sqlite3必须支持JSON函数。数据为独立合成样例，无真实个人信息。可修改匿名化和发布实现，不能修改固定schema、输入库和legacy_reader.py。整个environment为候选公开输入；提供方验证和参考答案位于包外。
