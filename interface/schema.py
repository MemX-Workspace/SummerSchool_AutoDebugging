from abc import ABC, abstractmethod
from enum import Enum
import time
from typing import List, Set, Generator, Optional
from pydantic.v1 import BaseModel, Field


class Issue(BaseModel):
    issue_id: str  # 题号
    prefix_code: str  # 前缀公共代码
    buggy_code: str  # 需要修复的代码
    query: str  # 关于题目的说明（question & constraints）


class FixedSolution(BaseModel):
    issue_id: str
    fixed_code: str  # 修复后的代码（对应 Issue.buggy_code）
    explanation: Optional[str]  # 对bug产生原因的解释（可选）
