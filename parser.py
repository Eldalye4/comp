import ply.yacc as yacc
from mylexer import tokens
from tree import BinOp, Number

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = BinOp(p[1], p[2], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = Number(p[1])

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

if __name__ == "__main__":
    data = "3 * (4 + 5)"
    result = parser.parse(data)
    
    def print_tree(node, indent=0):
        if node is None:
            return
        print("  " * indent + f"Type: {node.type}, Leaf: {node.leaf}")
        for child in node.children:
            print_tree(child, indent + 1)
    
    print_tree(result)

