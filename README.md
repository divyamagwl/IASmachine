# IAS Computer Architecture

Implementation of IAS machine in python.

## Requirements
  * python3
  * bitstream module

## Installing dependancies 
    pip3 install bitstream

## Run the program
    python3 Test.py
    Enter 1 or 2 on the terminal for corresponding program (See below for the programs)

## Programs

#### Program 1

  _C code :_

  ```
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
  ```

  _Assembly code :_

  ```
  LOAD M(501)     SUB M(502)
  JUMP+M(6,0:19)  LOAD M(501)
  ADD M(502)      STOR M(503)
  LOAD MQ M(503)  MUL M(501)
  LOAD MQ         STOR M(504)     
  HALT
  STOR M(503)     LOAD MQ M(503)
  MUL M(501)      LOAD MQ
  STOR M(504)     HALT
  ```

#### Program 2

  Random instructions to show the functionality of most of the instructions left.

  ```
  LOAD M(501)       LSH
  ADD |M(502)|      DIV M(503)
  LOAD MQ           JUMP M(4,20:39)
  HALT         
  HALT              SUB |M(504)|
  JUMP M(6,0:19)    HALT
  RSH               STOR M(505)
  STOR M(506,8:19)  HALT
  ```

<b>Note:</b> I have implemented the following programs but feel free to implement more in the Test file and send me PR.

## Assumptions 

* PC starts from 0 and PC is stored in integer form rather than bits.
* Data part of memory starts from M(501).
* HALT has opcode "11111111".
* Data is in 2s complement form.

