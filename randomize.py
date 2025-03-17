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
    
    return output_seed

print(randomize())