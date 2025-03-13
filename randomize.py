input_seed = 0
output_seed = 0

def randomize():
    file = open("random-data-set.txt","r")
    print(file.read())
    input_seed = int(file.read())
    output_seed = input_seed^input_seed.bit_length
    
    return output_seed

print(randomize())