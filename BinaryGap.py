num = 4225
print("integer = ", num)

# convert num into binary; remove 0b prefix
in_binary = bin(num)[2:]
print("binary value = ", in_binary)

# check if there are 0s in the binary value
if '0' not in in_binary: 
    print('0') 
    
# check if there are more than one 1s in the binary value
if in_binary.count("1") == 1: 
    print('0')

# set initial values
zero_ctr = 0
start_sw = True
highest_0_ctr = 0

# iterate through the binary digits
bin_len = len(in_binary)
for x in range(1, bin_len):

    if in_binary[x] == '0':
        zero_ctr += 1
        if start_sw:
            start_sw = False            
    else:
        if not start_sw:
            if zero_ctr > highest_0_ctr:
                highest_0_ctr = zero_ctr
            start_sw = True
            zero_ctr = 0
        
print(highest_0_ctr)