# LLM for AutoDebugging
## 目录结构
```bash
├── interface/
│   ├── debugger.py        # Debugger接口（实现`fix_issue`方法）
│   ├── schema.py
├── example/
│   ├── dummy_debugger.py   # 一个简单的debugger示例
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
from example.dummy_debugger import DummyDebugger
from utils.tester import run_tests
from utils.data_loader import IssueLoader, FixedSolutionLoader

# 1. Load the issue
issues = IssueLoader().load_issues()

# 2. Initialize the debugger
debugger = DummyDebugger(out_path="example/out")

# 3. Fix the issues
for issue in issues:
    debugger.run_with_save(issue)

# 4. test the fixed solutions
fixed_solutions = FixedSolutionLoader(out_path="example/out").load_fixed_solutions()
test_results = run_tests(fixed_solutions)
print(test_results)
```
