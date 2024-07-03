from workspace.my_debugger import MyDebugger
from utils.tester import run_tests
from utils.data_loader import IssueLoader, FixedSolutionLoader

OUT_PATH = "workspace/out"
# 1. Load the issue
issues = IssueLoader().load_issues()

# 2. Initialize the debugger
debugger = MyDebugger(out_path=OUT_PATH)

# 3. Fix the issues
for issue in issues:
    debugger.run_with_save(issue)

# 4. test the fixed solutions
fixed_solutions = FixedSolutionLoader(out_path=OUT_PATH).load_fixed_solutions()
test_results = run_tests(fixed_solutions, out_path=OUT_PATH)
print(test_results)
