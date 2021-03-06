
INSTRUCTIONS = [
    #Instructions for Program 1
    [
        ["00000001", "000111110101", "00000110", "000111110110"],
        ["00001111", "000000000110", "00000001", "000111110101"],
        ["00000101", "000111110110", "00100001", "000111110111"],
        ["00001001", "000111110111", "00001011", "000111110101"],
        ["00001010", "000000000000", "00100001", "000111111000"],
        ["11111111", "000000000000", "11111111", "000000000000"],  
        ["00100001", "000111110111", "00001001", "000111110111"],
        ["00001011", "000111110101", "00001010", "000000000000"],
        ["00100001", "000111111000", "11111111", "000000000000"],
    ],
    #Instructions for Program 2
    [
        ["00000001", "000111110101", "00010100", "000000000000"],
        ["00000111", "000111110110", "00001100", "000111110111"],
        ["00001010", "000000000000", "00001110", "000000000100"],
        ["11111111", "000000000000", "00000000", "000000000000"],
        ["11111111", "000000000000", "00001000", "000111111000"],
        ["00001101", "000000000110", "11111111", "000000000000"],
        ["00010101", "000000000000", "00100001", "000111111001"],
        ["00010010", "000111111010", "11111111", "000000000000"],
    ]
]

DATA = [
    #Data for Program 1
    [
        ["0000000000000000000000000000000000000101"],
        ["0000000000000000000000000000000000000010"],
        ["0000000000000000000000000000000000000000"],
        ["0000000000000000000000000000000000000000"],
    ],
    #Data for Program 2
    [
        ["0000000000000000000000000000000000001111"],
        ["1111111111111111111111111111111111110101"],
        ["0000000000000000000000000000000000000100"],
        ["1111111111111111111111111111111111111011"],
    ]
]


"""
PROGRAM 1 -->

    main() {
        int a = 5, b = 2, c, d;
        if(a >= b) {
            c = a - b;
        }
        else {
            c = a + b;
        }
        d = c * a;
    }

    LOAD M(501)     SUB M(502)
    JUMP+M(6,0:19)  LOAD M(501)
    ADD M(502)      STOR M(503)
    LOAD MQ M(503)  MUL M(501)
    LOAD MQ         STOR M(504)     
    HALT
    STOR M(503)     LOAD MQ M(503)
    MUL M(501)      LOAD MQ
    STOR M(504)     HALT

"""

"""
PROGRAM 2 -->
    RANDOM INSTRUCTIONS

    LOAD M(501)       LSH
    ADD |M(502)|      DIV M(503)
    LOAD MQ           JUMP M(4,20:39)
    HALT         
    HALT              SUB |M(504)|
    JUMP M(6,0:19)    HALT
    RSH               STOR M(505)
    STOR M(506,8:19)  HALT
"""