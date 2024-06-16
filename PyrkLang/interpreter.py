from lexer import lexer
from pyrkparser import *
from utils import *
import sys, os, colorama

colorama.init(True)

if not sys.argv[1]:
    print("""
    ########  ##    ## ########  ##    ##    #### ##    ## ######## ######## ########  ########  ########  ######## ######## ######## ########  
    ##     ##  ##  ##  ##     ## ##   ##      ##  ###   ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ##     ##   ####   ##     ## ##  ##       ##  ####  ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ########     ##    ########  #####        ##  ## ## ##    ##    ######   ########  ########  ########  ######      ##    ######   ########  
    ##           ##    ##   ##   ##  ##       ##  ##  ####    ##    ##       ##   ##   ##        ##   ##   ##          ##    ##       ##   ##   
    ##           ##    ##    ##  ##   ##      ##  ##   ###    ##    ##       ##    ##  ##        ##    ##  ##          ##    ##       ##    ##  
    ##           ##    ##     ## ##    ##    #### ##    ##    ##    ######## ##     ## ##        ##     ## ########    ##    ######## ##     ## 
    ---------------------------------------------------------------------------------------------------------------------------------------------       

            it seems ur lost, relax bro, just do this: python3 interpreter.py bestprogram.pyrk                                                                                                                                                                                 
    """ + colorama.Fore.BLUE)
elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
    print("""
    ########  ##    ## ########  ##    ##    #### ##    ## ######## ######## ########  ########  ########  ######## ######## ######## ########  
    ##     ##  ##  ##  ##     ## ##   ##      ##  ###   ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ##     ##   ####   ##     ## ##  ##       ##  ####  ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ########     ##    ########  #####        ##  ## ## ##    ##    ######   ########  ########  ########  ######      ##    ######   ########  
    ##           ##    ##   ##   ##  ##       ##  ##  ####    ##    ##       ##   ##   ##        ##   ##   ##          ##    ##       ##   ##   
    ##           ##    ##    ##  ##   ##      ##  ##   ###    ##    ##       ##    ##  ##        ##    ##  ##          ##    ##       ##    ##  
    ##           ##    ##     ## ##    ##    #### ##    ##    ##    ######## ##     ## ##        ##     ## ########    ##    ######## ##     ## 
    ---------------------------------------------------------------------------------------------------------------------------------------------       

            it seems ur lost, relax bro, just do this: python3 interpreter.py bestprogram.pyrk                                                                                                                                                                                 
    """ + colorama.Fore.BLUE)
elif sys.argv[1][-4:] != 'pyrk':
    print("""
    ########  ##    ## ########   ##    ##    #### ##    ## ######## ######## ########  ########  ########  ######## ######## ######## ########  
    ##     ##  ##  ##  ##     ## ##   ##      ##  ###   ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ##     ##   ####   ##     ## ##  ##       ##  ####  ##    ##    ##       ##     ## ##     ## ##     ## ##          ##    ##       ##     ## 
    ########     ##    ########  #####        ##  ## ## ##    ##    ######   ########  ########  ########  ######      ##    ######   ########  
    ##           ##    ##   ##   ##  ##       ##  ##  ####    ##    ##       ##   ##   ##        ##   ##   ##          ##    ##       ##   ##   
    ##           ##    ##    ##  ##   ##      ##  ##   ###    ##    ##       ##    ##  ##        ##    ##  ##          ##    ##       ##    ##  
    ##           ##    ##     ## ##    ##    #### ##    ##    ##    ######## ##     ## ##        ##     ## ########    ##    ######## ##     ## 
    ---------------------------------------------------------------------------------------------------------------------------------------------       

            it seems ur lost, relax bro, just do this: python3 interpreter.py bestprogram.pyrk btw, use a .pyrk script, i really hate other languages                                                                                                                                                                          
    """ + colorama.Fore.BLUE)
else:
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