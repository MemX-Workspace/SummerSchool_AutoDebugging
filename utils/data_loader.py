from typing import List
from interface.schema import Issue
import os


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
        for issue_id in os.listdir(self.root_path):
            issues.append(self.load_test_case(issue_id))
        return issues


if __name__ == "__main__":
    issue_loader = IssueLoader()
    issues = issue_loader.load_issues()
    for issue in issues:
        print(issue.dict())
        print()
