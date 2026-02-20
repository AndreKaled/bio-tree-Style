from parser import parser_json

if __name__ == "__main__":
    root = parser_json("examples/example.json")
    print(root)