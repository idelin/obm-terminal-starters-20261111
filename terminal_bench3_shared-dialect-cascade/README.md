# 双分支推断与OpenFst转写

实现infer.py与compile_bundle.py。先运行python3 infer.py data result，再运行python3 compile_bundle.py data result/result.json bundle。python3 apply_bundle.py bundle从标准输入逐行接收branch、word，输出转写后的word。完整公开契约在proposal的C_agent_task。

transduce.py定义固定单规则语义；data/rules.json和两份TSV是观测输入。fst_runtime.py与apply_bundle.py是固定OpenFst消费者，不能修改；它们不读取候选推断实现。只能修改infer.py、compile_bundle.py以及这两个程序导入的新增模块。环境需要Debian12的libfst-tools=1.7.9-5，Dockerfile可构建，运行时不联网。
