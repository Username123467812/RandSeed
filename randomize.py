import time
import math

def randomize(input=0):
    # Figure out file loading later, having trouble converting to string
    #file = open("random-data-set.txt","r")
    #print(file.read())
    #input_seed = int(''.join(file.readlines()))
    input_seed = 745612673567489501234019283
    output_seed = 0

    # check if there is a speicifed input seed
    if input != 0:
        input_seed = input

    # starting stuff to make the number substantially bigger
    output_seed = input_seed**input_seed.bit_length()
    if str(output_seed).count('0') > 0:
        output_seed = output_seed // int(str(output_seed).count('0'))

    # cut output_seed down a little
    output_seed = math.ceil(output_seed // (input_seed ** 50))

    # add in the current time in seconds (with some input seed mixed in)
    output_seed = output_seed * (math.ceil(time.time()) + (input_seed))

    # multiply in the (rounded) sqrt of input seed
    output_seed = output_seed * math.ceil(math.sqrt(input_seed) * 100000)
    
    return output_seed

print(randomize())