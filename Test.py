from bitstring import BitStream

# Importing IAS machine to perform operations
from IAS import IAS, InstructionCycle
# Importing programs to be executed
from programs import INSTRUCTIONS, DATA
from colors import Colors

# Runs the program in the IAS machine
def run(IAS, Program):
    while True:
        print(f"\n{Colors.HEADER}-------------FETCH CYCLE---------------{Colors.ENDC}")

        Program.Fetch()

        # Prints the value of registers after Fetch Cycle
        print(f"MBR {IAS.registers.MBR.bin}")
        print(f"IBR {IAS.registers.IBR.bin}")
        print(f"IR  {IAS.registers.IR.bin}")
        print(f"MAR {IAS.registers.MAR.bin}")

        print(f"\n{Colors.OKBLUE}-------------EXECUTE CYCLE-------------{Colors.ENDC}")

        Execute = Program.Decode()
        if(Execute == 'HALT'):
            print(f"{Colors.FAIL}HALT{Colors.ENDC}\n")
            break
        elif(Execute == False):
            print(f"\n{Colors.FAIL}WRONG OPCODE!!!{Colors.ENDC}")
            break
        Execute()

        # Prints the value of registers after Execute Cycle
        print(f"MBR {IAS.registers.MBR.bin}")
        print(f"MAR {IAS.registers.MAR.bin}")
        print(f"AC  {IAS.registers.AC.bin} int = {IAS.registers.AC.int}")
        print(f"MQ  {IAS.registers.MQ.bin} int = {IAS.registers.MQ.int}")

# Main function to run our python file
def main():
    # Object of IAS class
    ias = IAS()
    # Object of Instruction cycles which will be executed by IAS
    program  = InstructionCycle(ias)
    
    # Performs the corresponding number of program
    number = int(input("Please enter 1 OR 2: "))

    if(number == 1):
        # Preprogram the memory 
        for i in range(len(INSTRUCTIONS[0])):
            ias.memory.loc[i] = BitStream(bin=INSTRUCTIONS[0][i][0]+INSTRUCTIONS[0][i][1]+INSTRUCTIONS[0][i][2]+INSTRUCTIONS[0][i][3])

        for i in range(len(DATA[0])):
            ias.memory.loc[501+i] = BitStream(bin=DATA[0][i][0])

        print(f"{Colors.BOLD}a = {ias.memory.loc[501].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}b = {ias.memory.loc[502].int}{Colors.ENDC}")

        run(ias, program)

        print(f"{Colors.BOLD}c = {ias.memory.loc[503].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}d = {ias.memory.loc[504].int}{Colors.ENDC}")

    elif(number == 2):
        # Preprogram the memory 
        for i in range(len(INSTRUCTIONS[1])):
            ias.memory.loc[i] = BitStream(bin=INSTRUCTIONS[1][i][0]+INSTRUCTIONS[1][i][1]+INSTRUCTIONS[1][i][2]+INSTRUCTIONS[1][i][3])

        for i in range(len(DATA[1])):
            ias.memory.loc[501+i] = BitStream(bin=DATA[1][i][0])

        print(f"{Colors.BOLD}M(501) = {ias.memory.loc[501].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}M(502) = {ias.memory.loc[502].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}M(503) = {ias.memory.loc[503].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}M(504) = {ias.memory.loc[504].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}M(505) = {ias.memory.loc[505].int}{Colors.ENDC}")

        run(ias, program)

        print(f"{Colors.BOLD}M(505) = {ias.memory.loc[505].int}{Colors.ENDC}")
        print(f"{Colors.BOLD}M(506) = {ias.memory.loc[506].bin}{Colors.ENDC}")



if __name__=="__main__":
    main()
