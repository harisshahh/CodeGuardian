import ast

def parse_code(code_string: str):
    try:
        return ast.parse(code_string)
    except SyntaxError as e:
        return {"error": f"Syntax Error: {e}"}
    
