#base 10 to binary converter, can accept decimal points
def decToBin(n):
    integer = int(n)
    decimal = n - integer
    output = bin(integer)
    output = str(output)[2:] + '.'
    decimal = decimal * 2
    while decimal != 1:
        if decimal > 1:
            output += '1'
            decimal = decimal - 1
        else:
            output += '0'
        decimal = decimal * 2
    return(output + '1')

