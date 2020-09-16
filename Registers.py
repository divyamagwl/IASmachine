from bitstring import BitStream

"""
Defines all the registers in a IAS machine
"""
class Registers:
    def __init__(self):
        self.AC  = BitStream(int=0, length=40)
        self.MQ  = BitStream(int=0, length=40)
        self.MBR = BitStream(int=0, length=40)
        self.IBR = BitStream(int=0, length=20)
        self.IR  = BitStream(int=0, length=8)
        self.MAR = BitStream(int=0, length=12)
        self.PC  = 0