# LLM for AutoDebugging
## 目录结构
```bash
├── interface/
│   ├── debugger.py        # Debugger接口（实现该接口）
│   ├── schema.py
├── example/
│   ├── dummy_debugger.py   # 一个简单的debugger示例
├── utils/
│   ├── data_loader.py
│   ├── __pycache__/
│   │   ├── data_loader.cpython-39.pyc
│   ├── tester.py
├── data/
│   ├── issue1/
│   │   ├── query.txt
│   │   ├── buggy_code.py
│   │   ├── prefix_code.py
│   │   ├── test/
│   │   │   ├── cases.yaml
│   │   │   ├── test_code.py
├── README.md
```
