# 易腐物料排产与记账

main.py为逐行JSON排产入口；dispatch.py接收数据库和run标识，把计划与库存预留提交；report.py读取历史计划和当前库存。schema.sql和warehouse_reader.py定义起点实际资源投影，data/warehouse.sqlite是合成样例。完整接口与预算见proposal的C_agent_task。可改三个入口及实现模块，不改固定schema、读取器和样例；参考解和私有验收在包外。
