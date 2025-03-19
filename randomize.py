import time
import math
from decimal import Decimal

input_seed = 0
output_seed = 0

def randomize():
    # Figure out file loading later, having trouble converting to string
    #file = open("random-data-set.txt","r")
    #print(file.read())
    #input_seed = int(''.join(file.readlines()))
    input_seed = 745612673567489501234019283
    output_seed = input_seed**input_seed.bit_length()
    output_seed = output_seed // int(str(output_seed).count('0'))
    #cut output_seed down a little
    output_seed = math.ceil(output_seed // (input_seed ** 50))
    output_seed = output_seed * (math.ceil(time.time()) + (input_seed))
    output_seed = output_seed * math.ceil(math.sqrt(input_seed) * 100000)
    
    return output_seed

print(randomize())
