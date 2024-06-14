from utils import onlyDigits
import sys

def tokenize(code: str):
    programInstructions = []
    tokenPosition = -1

    programLines = [line.strip() for line in code.splitlines()]

    for line in programLines:
        tokenPosition += 1
        words = line.split(" ")

        ################# SEARCHING FOR BUILT-IN FUNCTIONS ####################
        if words[0] == "print":
            programInstructions.append("print")

            if words[1].startswith('"'):
                stringLiteral = ' '.join(words[1:])[1:-1]
                programInstructions.append(stringLiteral)
            elif not words[1].startswith('"'):
                if onlyDigits(words[1]):
                    programInstructions.append(words[1])
                else:
                    # TODO: IMPLEMENT AN ERROR MANAGEMENT SYSTEM
                    print('print should receive a string or a number, not that!')
                    sys.exit(1)
    
    return programInstructions, tokenPosition