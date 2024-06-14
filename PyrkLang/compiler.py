import sys
import tokenizer
import os

# TODO: Create a good interface for the coder

# print("[X] Reading file...")
filepath = sys.argv[1]

with open(filepath, "r") as f:
    code = f.read()

asmFilepath = filepath[:-5] + '.asm'
out = open(asmFilepath, "w")

# print("[X] Tokenizing file...")
programInstructions = tokenizer.tokenize(code)
position = -1
printArgs = []
printCounter = -1

# Getting print args
for instruction in programInstructions:
    if isinstance(instruction, list):
        for pos, instr in enumerate(instruction):
            if instr == "print" and pos + 1 < len(instruction):
                printArgs.append(instruction[pos + 1])

out.write("""; -- header --
bits 64
default rel
""")

out.write("""; -- variables --
section .bss
""")

out.write("""; -- constants --
section .data
""")
for i, printarg in enumerate(printArgs):
    out.write(f"print_arg_{i} db \"{printarg}\", 10, 0\n")

out.write("""; -- Entry point --
section .text
global main
extern ExitProcess
extern printf
          
main:
\tPUSH rbp
\tMOV rbp, rsp
\tSUB rsp, 32
""")

# print("[X] Executing...")

for instruction in programInstructions:
    if isinstance(instruction, list):
        for instr in instruction:
            if instr == "print":
                printCounter += 1
                out.write(f"; -- PRINT --\n")
                out.write(f"\tLEA rcx, [print_arg_{printCounter}]\n")
                out.write(f"\tXOR eax, eax\n")
                out.write(f"\tCALL printf\n")

out.write("""
\tXOR rax, rax
\tCALL ExitProcess

\tMOV rsp, rbp
\tPOP rbp
\tRET
""")
out.close()

# Assembling and linking the generated ASM code
os.system(f"nasm -f elf64 {asmFilepath}")
os.system(f"gcc -o {asmFilepath[:-4] + '.exe'} {asmFilepath[:-4] + '.o'}")
os.system(f"{asmFilepath[:-4] + '.exe'}")

os.remove(f"{asmFilepath[:-4] + '.o'}")
os.remove(f"{asmFilepath[:-4] + '.asm'}")