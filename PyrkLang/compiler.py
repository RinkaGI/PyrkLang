from pyrkparser import *
from utils import *
from lexer import lexer
import sys, os

filepath = sys.argv[1]

with open(filepath, "r") as f:
    code = f.read()

cFilepath = filepath[:-5] + '.c'
out = open(cFilepath, "w")

tokens = lexer.lex(code)
ast = parser.parse(tokens)

class Compiler:
    def __init__(self, ast) -> None:
        self.printArgs = []
        
        out.write("""
// -- header --
#include <stdio.h>
        """)

        out.write("""
// -- variables --

""")


        out.write("""
// -- constants --

        """)

        out.write("""
// -- Entry point --
int main() {

""")

    def visit(self, node):
        if isinstance(node, PrintNode):
            out.write(f'// -- PRINT --\n')
            value = self.visit(node.value)
            out.write(f'printf("{str(value)}");')
        if isinstance(node, NumberNode):
            if onlyNumbers(node.value):
                return int(node.value)
            elif onlyDigits(node.value):
                return float(node.value)
            else:
                raise Exception('Unexpected error understanding this: ', str(node.value))
        if isinstance(node, StringNode):
            return node.value[1:-1]
    
    def compile(self):
        for node in ast:
            self.visit(node)

comp = Compiler(ast)
comp.compile()
out.write('return 0;\n}')
out.close()

os.system(f"gcc {cFilepath[:-2] + '.c'} -o {cFilepath[:-2] + '.exe'}")
os.system(f"{cFilepath[:-2] + '.exe'}")
os.remove(f"{cFilepath[:-2] + '.c'}")