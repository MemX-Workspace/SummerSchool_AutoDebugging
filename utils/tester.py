import os
from typing import List
import yaml
import unittest
from interface.schema import Issue, FixedSolution


class IssueTester(unittest.TestCase):
    def __init__(self, methodName: str, fixed_solution: FixedSolution = None) -> None:
        super().__init__(methodName)

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
        exec(all_code, self.__dict__)

    def runTest(self):
        for case in self.test_cases["cases"]:
            # print(case)
            kwargs = case["input"]
            expected_output = case["output"]
            result = self.run_test(**kwargs)  # call `test_code.py` in issue folder
            self.assertEqual(result, expected_output, case.get("explanation", ""))


def suite(fixed_solutions: List[FixedSolution]):
    suite = unittest.TestSuite()
    for fixed_solution in fixed_solutions:
        suite.addTest(IssueTester("runTest", fixed_solution))
    return suite


def run_tests(fixed_solutions: List[FixedSolution]):
    runner = unittest.TextTestRunner()
    res = runner.run(suite(fixed_solutions))
    return res


if __name__ == "__main__":
    from utils.data_loader import FixedSolutionLoader

    fixed_solution = FixedSolutionLoader(out_path="example/out").load_fixed_solution(
        "issue1"
    )

    res = run_tests([fixed_solution])
    print(res)
