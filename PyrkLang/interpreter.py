import sys, os
from lexer import lexer
from pyrkparser import *
from utils import *

# TODO: Create a good interface for the coder

filepath = sys.argv[1]

f = open(filepath, "r")
code = f.read()
f.close()

class Interpreter:
    def __init__(self):
        pass

    def visit(self, node):
        if isinstance(node, PrintNode):
            value = self.visit(node.value)
            value = str(value)
            value = value.replace(r'\n', '\n')
            sys.stdout.write(str(value))
        elif isinstance(node, NumberNode):
            if onlyNumbers(node.value):
                return int(node.value)
            elif onlyDigits(node.value):
                return float(node.value)
            else:
                raise Exception('Unexpected error understanding this: ', str(node.value))
        elif isinstance(node, StringNode):
            return node.value[1:-1]
        else:
            raise Exception(f"Unknown node: {node}")
        
    def interpret(self, ast):
        for node in ast:
            self.visit(node)

tokens = lexer.lex(code)
ast = parser.parse(tokens)
interp = Interpreter()
interp.interpret(ast)