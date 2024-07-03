# LLM for AutoDebugging
## 环境配置
```bash
# python 3.9
pip install -r requirements.txt
```

## 目录结构
```bash
├── interface/
│   ├── debugger.py        # Debugger接口（实现`fix_issue`方法）
│   ├── schema.py
├── example/
│   ├── dummy_debugger.py   # 一个简单的debugger示例
│   ├── main.py             # 一个完整流程的demo
│   ├── out                 # 输出结果
│   │   ├── issue1_fixed.json   # Debugger输出的修复结果
│   │   ├── test_results.yaml   # 所有issue的测试结果
├── utils/
│   ├── data_loader.py      # 用于加载 issue和 testcases
│   ├── tester.py           # 用于测试修复后的代码
├── data/                   # 题目
│   ├── issue1/
│   │   ├── query.txt       # 对代码功能和约束的描述
│   │   ├── buggy_code.py   # 需要修复的代码（class Solution）
│   │   ├── prefix_code.py  # 该代码所依赖的一些公共代码
│   │   ├── test/
│   │   │   ├── cases.yaml  # 测试用例
│   │   │   ├── test_code.py
├── README.md
```

## Demo
```python
# example/main.py
from example.dummy_debugger import DummyDebugger
from utils.tester import run_tests
from utils.data_loader import IssueLoader, FixedSolutionLoader

OUT_PATH = "example/out"
# 1. Load the issue
issues = IssueLoader().load_issues()

# 2. Initialize the debugger
debugger = DummyDebugger(out_path=OUT_PATH)

# 3. Fix the issues
for issue in issues:
    debugger.run_with_save(issue)

# 4. test the fixed solutions
fixed_solutions = FixedSolutionLoader(out_path=OUT_PATH).load_fixed_solutions()
test_results = run_tests(fixed_solutions, out_path=OUT_PATH)
print(test_results)
```

## 说明
1. 复制`example`文件夹，并重命名为`workspace`
2. 请仿照`example/dummy_debugger.py`实现自己的debugger
3. 仿照`example/main.py`跑通整个流程
4. 最后提交的文件包括：
    - `workspace/your_debugger.py`
    - `workspace/out/`
