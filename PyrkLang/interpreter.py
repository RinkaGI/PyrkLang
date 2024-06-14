import sys, tokenizer

# TODO: Create a good interface for the coder

# print("[X] Reading file...")
filepath = sys.argv[1]

f = open(filepath, "r")
code = f.read()
f.close()

# print("[X] Tokenizing file...")
programInstructions = tokenizer.tokenize(code)
position = -1

# print("[X] Executing...")
for instruction in programInstructions:
    if type(instruction) == list:
        for instr in instruction:
            position += 1

            def getInstruction(pos):
                if type(instruction) == list:
                    return instruction[pos]
                else:
                    pass
            
            if instr == "print":
                print(getInstruction(position + 1))
                pass