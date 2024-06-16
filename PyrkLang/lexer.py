from utils import onlyDigits, Token, TOK_PRINT, TOK_NUMBER, TOK_STRING, TOK_ENDINSTRUCTION
from rply import LexerGenerator
import sys

lg = LexerGenerator()

lg.add(TOK_PRINT, r'print')
lg.add(TOK_NUMBER, r'\d+(\.\d+)?')
lg.add(TOK_STRING, r'"(?:\\.|[^"\\])*"')
lg.ignore(r'\s+')

lexer = lg.build()