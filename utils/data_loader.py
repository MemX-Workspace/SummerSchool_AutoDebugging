from typing import List
from interface.schema import Issue, FixedSolution
import os
import json


class IssueLoader:
    def __init__(self, root_path: str = "data"):
        self.root_path = root_path

    def load_issue(self, issue_id: str) -> Issue:
        issue_path = os.path.join(self.root_path, issue_id)

        buggy_code_path = os.path.join(issue_path, "buggy_code.py")
        prefix_code_path = os.path.join(issue_path, "prefix_code.py")
        query_path = os.path.join(issue_path, "query.txt")

        with open(buggy_code_path, "r") as f:
            buggy_code = f.read()
        with open(prefix_code_path, "r") as f:
            prefix_code = f.read()
        with open(query_path, "r") as f:
            query = f.read()

        return Issue(
            issue_id=issue_id,
            prefix_code=prefix_code,
            buggy_code=buggy_code,
            query=query,
        )

    def load_issues(self) -> List[Issue]:
        issues = []
        for issue_id in os.listdir(self.root_path):
            issues.append(self.load_issue(issue_id))
        return issues


class TestCaseLoader:
    def __init__(self, root_path: str = "data"):
        self.root_path = root_path

    def load_test_case(self, issue_id: str) -> Issue:
        issue_path = os.path.join(self.root_path, issue_id)

        buggy_code_path = os.path.join(issue_path, "buggy_code.py")
        prefix_code_path = os.path.join(issue_path, "prefix_code.py")
        query_path = os.path.join(issue_path, "query.txt")

        with open(buggy_code_path, "r") as f:
            buggy_code = f.read()
        with open(prefix_code_path, "r") as f:
            prefix_code = f.read()
        with open(query_path, "r") as f:
            query = f.read()

        return Issue(
            issue_id=issue_id,
            prefix_code=prefix_code,
            buggy_code=buggy_code,
            query=query,
        )

    def load_test_cases(self) -> List[Issue]:
        issues = []
        for issue_dir in os.listdir(self.root_path):
            issues.append(self.load_test_case(issue_dir))
        return issues


class FixedSolutionLoader:
    def __init__(self, out_path: str = "out"):
        self.out_path = out_path

    def load_fixed_solution(self, issue_id: str) -> FixedSolution:
        issue_path = os.path.join(self.out_path, issue_id)

        fixed_solution_path = os.path.join(self.out_path, f"{issue_id}_fixed.json")
        with open(fixed_solution_path, "r") as f:
            fixed_solution_dict = json.load(f)

        return FixedSolution(**fixed_solution_dict)

    def load_fixed_solutions(self) -> List[FixedSolution]:
        fixed_solutions = []
        for json_file in os.listdir(self.out_path):
            if not json_file.endswith("_fixed.json"):
                continue
            issue_id = json_file.split("_")[0]
            fixed_solutions.append(self.load_fixed_solution(issue_id))
        return fixed_solutions


if __name__ == "__main__":
    issue_loader = IssueLoader()
    issues = issue_loader.load_issues()
    for issue in issues:
        print(issue.dict())
        print()
