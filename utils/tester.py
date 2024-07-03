import os
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
            result = self.run_test(**kwargs)
            self.assertEqual(result, expected_output, case.get("explanation", ""))


def suite(fixed_solution: FixedSolution):
    suite = unittest.TestSuite()
    suite.addTest(IssueTester("runTest", fixed_solution))
    return suite


if __name__ == "__main__":
    from utils.data_loader import IssueLoader

    issue = IssueLoader().load_issue("issue1")

    fixed_solution = FixedSolution(
        issue_id="issue1",
        fixed_code=issue.buggy_code,
        explanation="Dummy fixer does nothing.",
    )
    runner = unittest.TextTestRunner()
    res = runner.run(suite(fixed_solution))
    print(res)
