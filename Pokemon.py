from pyboy import PyBoy
import os
#pyboy = PyBoy('ROMs/yellow.gb')
f = open('steps.txt', 'r')
for each in range(20):
    print(f.readline())