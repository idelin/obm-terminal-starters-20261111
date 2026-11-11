# 会话修订与数据库物化

实现engine.py与materialize.py，保留固定main.py、legacy.py和replay.py。main.py支持逐行JSON会话回放；python3 replay.py data out读取实际seed.sqlite和corrections.jsonl产生修订账本与报告；再运行python3 materialize.py out/materialized.sqlite out/ledger.jsonl建立下游SQLite视图。后续可用新的账本批次重复调用物化入口。完整事件、封存、账本和事务契约见proposal的C_agent_task。

SQLite历史表的代码与数值解释见legacy.py，数据是合成交换夹具。程序可用Python3.12标准库，无需联网或GPU。sources不包含参考答案或私有验收。
