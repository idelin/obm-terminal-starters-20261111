# 证据归并与解释

main.py保留逐行JSON入口。reconcile.py将schema.sql定义的SQLite证据库归并为结果表，explain.py读取已提交结果给出解释。先阅读固定store_reader.py及schema.sql确认现有投影。data/panel.sqlite为独立合成公开样例。完整输出、事务和预算要求见proposal的C_agent_task。候选可改实现，不改固定投影与输入材料；参考求解器和私有验收在包外。
