from abc import ABC, abstractmethod
import os
from interface.schema import Issue, FixedSolution


class Debugger(ABC):
    """Abstract class for a debugger that fixes issues."""

    def __init__(self, output_path: str = "out"):
        self.output_path = output_path

    @abstractmethod
    def fix_issue(self, issue: Issue) -> FixedSolution:
        pass

    def save_solution(self, fixed_solution: FixedSolution):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        output_file = f"{self.output_path}/{fixed_solution.issue_id}_fixed.json"
        with open(output_file, "w") as f:
            f.write(fixed_solution.json())

    def run_with_save(self, issue: Issue) -> FixedSolution:
        fixed_solution = self.fix_issue(issue)
        self.save_solution(fixed_solution)
        return fixed_solution
