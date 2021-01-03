from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class TreeNode:
    name: str
    progress: str = ''
    children: List[TreeNode] = field(default_factory=list)
