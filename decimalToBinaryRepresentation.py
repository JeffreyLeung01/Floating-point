import decToBin

print("Pls enter the number of bits to represent exponent")
expBits = input()
expBits = int(expBits)

print("Pls enter the number of bits to represent significant")
sigBits = input()
sigBits = int(sigBits)

print("Pls enter a decimal number")
number = input()
number = float(number)
if number < 0:
    negative = True
    number = number * -1
else:
    negative = False
    
number = decToBin.decToBin(number) #string of the number in binary(positive)
if negative:
    print(f"binary form = -{number}")
else:
    print(f"binary form = {number}")

exp = number.find('.') - 1
exp = 2**(expBits - 1) -1 + exp
exp = bin(exp)[2:]
print("exponent =", exp)

sig = number.replace('.','')
sig = sig[1:]
length = len(sig)
if length > sigBits: #if the significant is too long then shorten it
    sig = sig[:sigBits-1]
if length < sigBits: #add trailing zeros if nessasary
    for i in range(sigBits - length):
        sig = sig + '0'
print("significant =", sig)

if negative:
    binary = '1' + exp + sig
else:
    binary = '0' + exp + sig

print("bit pattern =", hex(int(binary,2))[2:])
