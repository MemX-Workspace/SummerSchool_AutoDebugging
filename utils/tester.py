import os
from typing import List
import yaml
import unittest
from interface.schema import Issue, FixedSolution


class TestCase(unittest.TestCase):
    def __init__(self, methodName: str, testcode: str, case: dict) -> None:
        super().__init__(methodName)
        self.case = case

        exec(testcode, self.__dict__)

    def runTest(self):
        # print(case)
        kwargs = self.case["input"]
        expected_output = self.case["output"]
        result = self.run_test(**kwargs)  # call `test_code.py` in issue folder
        self.assertEqual(result, expected_output, self.case.get("explanation", ""))


class IssueTester(unittest.TestSuite):
    def __init__(self, fixed_solution: FixedSolution = None) -> None:
        super().__init__()
        issue_path = os.path.join("data", fixed_solution.issue_id)
        testcase_file = os.path.join(issue_path, "test/cases.yaml")
        with open(testcase_file, "r") as file:
            self.test_cases = yaml.safe_load(file)

        # load the target function
        prefix_code_path = os.path.join(issue_path, "prefix_code.py")
        prefix_code = open(prefix_code_path, "r").read()
        solution_code = fixed_solution.fixed_code

        test_code_path = os.path.join(issue_path, "test/test_code.py")
        test_code = open(test_code_path, "r").read()  # run_test()
        all_code = "\n".join([prefix_code, solution_code, test_code])

        for case in self.test_cases["cases"]:
            self.addTest(TestCase("runTest", all_code, case))


def run_tests(fixed_solutions: List[FixedSolution], out_path: str = "out"):

    runner = unittest.TextTestRunner()
    run_results = {}
    for fixed_solution in fixed_solutions:
        issue_id = fixed_solution.issue_id
        suite = IssueTester(fixed_solution=fixed_solution)
        res = runner.run(suite)
        run_results[issue_id] = {
            "run": res.testsRun,
            "failures": len(res.failures),
            "errors": len(res.errors),
        }
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    with open(os.path.join(out_path, "test_results.yaml"), "w") as file:
        yaml.dump(run_results, file)
    return run_results


if __name__ == "__main__":
    from utils.data_loader import FixedSolutionLoader

    fixed_solution = FixedSolutionLoader(out_path="example/out").load_fixed_solution(
        "issue1"
    )
    res = run_tests([fixed_solution])
    print(res)
