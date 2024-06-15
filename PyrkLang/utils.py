DIGITS = '0123456789.'
def onlyDigits(s):
    return all(char in DIGITS for char in s)

class Token:
    def __init__(self, type_, value=None) -> None:
        self.type = type_
        self.value = value

    def __repr__(self) -> str:
        if self.value: return f'{self.type}: {self.value}'
        return f'{self.type}'
TOK_PRINT = "PRINT"
TOK_NUMBER = "NUMBER"
TOK_STRING = "STRING"
TOK_ENDINSTRUCTION = "ENDINSTRUCTION"