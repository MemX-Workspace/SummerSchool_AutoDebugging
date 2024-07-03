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
