from bitstring import BitStream

from MainMemory import MainMemory
from Registers import Registers
from colors import Colors

"""
IAS machine consists of Registers and Main memory
"""
class IAS:
    def __init__(self):
        self.memory    = MainMemory()
        self.registers = Registers()


"""
Defines the Instruction cycle of IAS program which consists of fetch, decode and execute
"""
class InstructionCycle:

    def __init__(self, IAS):
        self.IAS = IAS

        # 21 instructions of IAS with their opcodes + HALT
        self.opcodeList = {
            '00001010': self.loadMQToAC,
            '00001001': self.loadToMQ,
            '00100001': self.store,
            '00000001': self.loadToAC,
            '00000010': self.loadNegToAC,
            '00000011': self.loadAbsToAC,
            '00000100': self.loadNegAbsToAC,
            '00001101': self.jumpLeft,
            '00001110': self.jumpRight,
            '00001111': self.jumpLeftCond,
            '00010000': self.jumpRightCond,
            '00000101': self.add,
            '00000111': self.addAbs,
            '00000110': self.sub,
            '00001000': self.subAbs,
            '00001011': self.mul,
            '00001100': self.div,
            '00010100': self.lsh,
            '00010101': self.rsh,
            '00010010': self.storLeft,
            '00010011': self.storRight,
            "11111111": 'HALT' #HALT instruction stops the execution of program
        }

    # Decodes the instruction opcode and returns the instruction to be executed
    def Decode(self):
        opcode = self.IAS.registers.IR.bin
        if(opcode in self.opcodeList):
            return self.opcodeList[opcode]
        else:
            return False #Illegal opcode

    # Fetches the instruction and is loaded to appropriate registers
    def Fetch(self):

        # Checks if IBR is empty
        if(self.IAS.registers.IBR == BitStream(int=0, length=20)):
            self.IAS.registers.MAR = BitStream(int=self.IAS.registers.PC, length=12)
            self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]

            # Checks if Left instruction is present
            if(self.IAS.registers.MBR[0:20] != BitStream(int=0, length=20)):
                self.IAS.registers.IBR = self.IAS.registers.MBR[20:40]
                self.IAS.registers.IR  = self.IAS.registers.MBR[0:8]
                self.IAS.registers.MAR = self.IAS.registers.MBR[8:20]

            # Left instruction is not present
            else:
                self.IAS.registers.IR  = self.IAS.registers.MBR[20:28]
                self.IAS.registers.MAR = self.IAS.registers.MBR[28:40]
                self.IAS.registers.PC  += 1

        # IBR is filled already
        else:
            self.IAS.registers.IR  = self.IAS.registers.IBR[0:8]
            self.IAS.registers.MAR = self.IAS.registers.IBR[8:20]
            self.IAS.registers.IBR = BitStream(int=0, length=20) #Empty the IBR again
            self.IAS.registers.PC  += 1

    """
    21 instructions which can be executed and their corresponding functionality with the data flow in IAS
    """
    
    def loadMQToAC(self):
        self.IAS.registers.AC = self.IAS.registers.MQ

        print(f"{Colors.OKGREEN}Executed LOAD MQ{Colors.ENDC}")

    def loadToMQ(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int] 
        self.IAS.registers.MQ = self.IAS.registers.MBR

        print(f"{Colors.OKGREEN}Executed LOAD MQ M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def store(self):
        self.IAS.registers.MBR = self.IAS.registers.AC
        self.IAS.memory.loc[self.IAS.registers.MAR.int] = self.IAS.registers.MBR

        print(f"{Colors.OKGREEN}Executed STOR{Colors.ENDC}")

    def loadToAC(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = self.IAS.registers.MBR

        print(f"{Colors.OKGREEN}Executed LOAD M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def loadNegToAC(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=-self.IAS.registers.MBR.int, length=40)

        print(f"{Colors.OKGREEN}Executed LOAD -M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def loadAbsToAC(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=abs(self.IAS.registers.MBR.int), length=40)

        print(f"{Colors.OKGREEN}Executed LOAD |M({self.IAS.registers.MAR.int})|{Colors.ENDC}")

    def loadNegAbsToAC(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=-abs(self.IAS.registers.MBR.int), length=40)

        print(f"{Colors.OKGREEN}Executed LOAD -|M({self.IAS.registers.MAR.int})|{Colors.ENDC}")

    def jumpLeft(self):
        self.IAS.registers.PC = self.IAS.registers.MAR.int
        self.IAS.registers.IBR = BitStream(int=0, length=20)

        print(f"{Colors.OKGREEN}Executed JUMP M({self.IAS.registers.MAR.int}, 0:19){Colors.ENDC}")

    def jumpRight(self):
        self.IAS.registers.PC = self.IAS.registers.MAR.int
        self.IAS.registers.IBR = self.IAS.memory.loc[self.IAS.registers.MAR.int][20:40]

        print(f"{Colors.OKGREEN}Executed JUMP M({self.IAS.registers.MAR.int}, 20:39){Colors.ENDC}")

    def jumpLeftCond(self):
        if(self.IAS.registers.AC.int >= 0):
            self.IAS.registers.PC = self.IAS.registers.MAR.int
            self.IAS.registers.IBR = BitStream(int=0, length=20)

        print(f"{Colors.OKGREEN}Executed JUMP + M({self.IAS.registers.MAR.int}, 0:19){Colors.ENDC}")

    def jumpRightCond(self):
        if(self.IAS.registers.AC.int >= 0):
            self.IAS.registers.PC = self.IAS.registers.MAR.int
            self.IAS.registers.IBR = self.IAS.memory.loc[self.IAS.registers.MAR.int][20:40]

        print(f"{Colors.OKGREEN}Executed JUMP + M({self.IAS.registers.MAR.int}, 20:39){Colors.ENDC}")

    def add(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=self.IAS.registers.MBR.int + self.IAS.registers.AC.int, length=40)

        print(f"{Colors.OKGREEN}Executed ADD M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def addAbs(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=abs(self.IAS.registers.MBR.int) + self.IAS.registers.AC.int, length=40)

        print(f"{Colors.OKGREEN}Executed ADD |M({self.IAS.registers.MAR.int})|{Colors.ENDC}")

    def sub(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=self.IAS.registers.AC.int - self.IAS.registers.MBR.int, length=40)

        print(f"{Colors.OKGREEN}Executed SUB M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def subAbs(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        self.IAS.registers.AC = BitStream(int=self.IAS.registers.AC.int - abs(self.IAS.registers.MBR.int), length=40)

        print(f"{Colors.OKGREEN}Executed SUB |M({self.IAS.registers.MAR.int})|{Colors.ENDC}")

    def mul(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        product = BitStream(int=self.IAS.registers.MBR.int * self.IAS.registers.MQ.int, length=80)
        self.IAS.registers.MQ = BitStream(int=product[40:80].int, length=40)
        self.IAS.registers.AC = BitStream(int=product[0:39].int, length=40)

        print(f"{Colors.OKGREEN}Executed MUL M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def div(self):
        self.IAS.registers.MBR = self.IAS.memory.loc[self.IAS.registers.MAR.int]
        quotient = BitStream(int=(self.IAS.registers.AC.int // self.IAS.registers.MBR.int), length=40)
        remainder = BitStream(int=(self.IAS.registers.AC.int % self.IAS.registers.MBR.int), length=40)
        self.IAS.registers.MQ = quotient
        self.IAS.registers.AC = remainder

        print(f"{Colors.OKGREEN}Executed DIV M({self.IAS.registers.MAR.int}){Colors.ENDC}")

    def lsh(self):
        self.IAS.registers.AC = BitStream(int=2*self.IAS.registers.AC.int, length=40)

        print(f"{Colors.OKGREEN}Executed LSH{Colors.ENDC}")

    def rsh(self):
        self.IAS.registers.AC = BitStream(int=self.IAS.registers.AC.int//2, length=40)

        print(f"{Colors.OKGREEN}Executed RSH{Colors.ENDC}")

    def storLeft(self):
        self.IAS.registers.MBR = self.IAS.registers.AC
        temp = self.IAS.memory.loc[self.IAS.registers.MAR.int].bin[0:8] + self.IAS.registers.MBR.bin[28:40] + self.IAS.memory.loc[self.IAS.registers.MAR.int].bin[20:40]
        self.IAS.memory.loc[self.IAS.registers.MAR.int] = BitStream(bin=temp)

        print(f"{Colors.OKGREEN}Executed STOR M({self.IAS.registers.MAR.int}, 8:19){Colors.ENDC}")

    def storRight(self):
        self.IAS.registers.MBR = self.IAS.registers.AC
        temp = self.IAS.memory.loc[self.IAS.registers.MAR.int].bin[0:28] + self.IAS.registers.MBR.bin[28:40]
        self.IAS.memory.loc[self.IAS.registers.MAR.int] = BitStream(bin=temp)

        print(f"{Colors.OKGREEN}Executed STOR M({self.IAS.registers.MAR.int}, 28:39){Colors.ENDC}")