from parser import parser_json

if __name__ == "__main__":
    tree = parser_json("examples/example.json")
    tree.print_tree()