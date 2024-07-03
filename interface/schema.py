from abc import ABC, abstractmethod
from enum import Enum
import time
from typing import List, Set, Generator, Optional
from langchain_core.pydantic_v1 import BaseModel, Field


class Issue(BaseModel):
    issue_id: str
    prefix_code: str
    buggy_code: str  # to be fixed
    query: str  # question & constraints


class FixedSolution(BaseModel):
    issue_id: str
    fixed_code: str
    explanation: Optional[str]


class TestCase(BaseModel):
    issue_id: str
    kwargs: dict
    buggy_code: str
    query: str  # question & constraints
    expected_output: str
