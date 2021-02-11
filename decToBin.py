#base10 to binary converter
#input is a decimal number, can accept positive or negative
#output is the floating point number in type string
def decToBin(n):
    if n < 0: #dealing with negative input
        output = '-'
        n = n * -1
    else:
        output = ''
    
    if n == int(n): #dealing with integer input
        output += bin(n)[2:]
        return output

    else:
        integer = int(n)
        decimal = n - integer
        output += bin(integer)[2:] + '.'
        decimal = decimal * 2
        while decimal != 1:
            if decimal > 1:
                output += '1'
                decimal = decimal - 1
            else:
                output += '0'
            decimal = decimal * 2
    return(output + '1')
