from typing import Any
TEE   = "\u251c"
ELBOW = "\u2514"
PIPE  = "\u2502   "
SPACE = "    "
# peguei daqui https://www.unicode.org/charts/PDF/U2500.pdf


class Node:
    def __init__(self, name, value: Any = None, children: list["Node"] | None = None) -> None:
        self.name = name
        self.value = value 
        self.children = children if children is not None else []

    def print_tree(self, prefix="", is_last=True):
        connector = ELBOW if is_last else TEE
        print(prefix + connector + " " + self.name if prefix else self.name)

        new_prefix = prefix + (SPACE if is_last else PIPE)
        for i, child in enumerate(self.children):
            is_last_child = (i == len(self.children) - 1)
            child.print_tree(new_prefix, is_last_child)