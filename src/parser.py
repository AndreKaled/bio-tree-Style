import json
from models import Node
from typing import Any

def parser_json(data_file) -> Node:
    with open(data_file, "r") as f:
        data = json.load(f)
    return build_node("", data)
        

# fun fact: isso e complexidade o(n)
def build_node(name: str, data: Any):
    if isinstance(data,dict):
        node = Node(name)
        for key, value in data.items():
            child = build_node(key, value)
            node.children.append(child)
        return node
    
    elif isinstance(data, list):
        node = Node(name)
        for i, item in enumerate(data):
            child = build_node(f"{data[i]}", item)
            node.children.append(child)
        return node
    
    else:
        return Node(name, value=data)