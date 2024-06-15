from rply import ParserGenerator
from rply.token import BaseBox
from lexer import lexer

# some nodes
class PrintNode(BaseBox):
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"PrintNode({self.value})"
    
class NumberNode(BaseBox):
    def __init__(self, value) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f"NumberNode({self.value})"
    
class StringNode(BaseBox):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"StringNode({self.value})"
    
# parser
pg = ParserGenerator(
    ['PRINT', 'NUMBER', 'STRING'],
    precedence=[
        ('left', ['PRINT']),
    ]
)

# some rules
@pg.production('program : statement')
@pg.production('program : program statement')
def program(p):
    if len(p) == 1:
        return [p[0]]
    else:
        return p[0] + [p[1]]
    
@pg.production('statement : PRINT expression')
def statement_print(p):
    return PrintNode(p[1])

@pg.production('expression : NUMBER')
def expression_number(p):
    return NumberNode(p[0].getstr())

@pg.production('expression : STRING')
def expression_string(p):
    return StringNode(p[0].getstr())

@pg.error
def error_handler(token):
    raise ValueError(f"Error de sintaxis: {token}")

parser = pg.build()