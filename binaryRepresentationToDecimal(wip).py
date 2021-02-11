#convert from binary representation to decimal

print("Pls enter the number of bits to represent exponent")
expBits = input()
expBits = int(expBits)

print("Pls enter the number of bits to represent significant")
sigBits = input()
sigBits = int(sigBits)

print("Pls enter a hexadecimal number")
number = input()
number = int(number,16)
number = bin(number)[2:] #string of the number in binary

if number[0] == '1':
    negative = True
else:
    negative = False

exp = number[1:expBits+1]
exp = int(exp,2)
exp = exp - (2**(expBits-1) - 1)
print("exponent =",exp)

sig = number[expBits+1:]
sig = "1." + str(sig)
print("significand =",sig)

value = 
print(value)
