from typing import Any

class Node:
    def __init__(self, name, value: Any = None, children: list["Node"] | None = None) -> None:
        self.name = name
        self.value = value 
        self.children = children if children is not None else []
