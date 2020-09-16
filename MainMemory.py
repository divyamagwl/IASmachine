from bitstring import BitStream

"""
Defines the Main memory of IAS machine
"""
class MainMemory:
    def __init__(self):
        self.word = BitStream(int=0, length=40)
        self.loc  = [self.word]*1000
