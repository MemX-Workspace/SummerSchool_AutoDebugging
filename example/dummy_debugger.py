from interface.debugger import Debugger
from interface.schema import Issue, FixedSolution


class DummyDebugger(Debugger):
    def fix_issue(self, issue: Issue) -> FixedSolution:
        # Implement Here: Call LLM to fix the issue

        return FixedSolution(
            issue_id=issue.issue_id,
            fixed_code=issue.buggy_code,
            explanation="Dummy fixer does nothing.",
        )


if __name__ == "__main__":
    issue = Issue(
        issue_id="0",
        prefix_code="",
        buggy_code="print('Hello, world!')",
        query="Show 'Hello, world!'",
    )
    debugger = DummyDebugger(out_path="example/out")
    fixed_solution = debugger.run_with_save(issue)
