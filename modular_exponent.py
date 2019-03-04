def FastModularExponentiation(b, e, m):
    binary = str(bin(e))[2:] # get a pure binary representation as a string
    binary = binary[::-1] # reverse the string to start at the lowest place value of 2
    numberOf1s = binary.count('1') # determine whether  this is a power of two
    firstEntry = True # used to determine behavior during first loop iteration
    c = b % m # get the reminder of the base mod m
    d = 1 # initialise the value of d which will hold the value of the mod power multiplications
    if numberOf1s == 1: # execute specific logic if exponent is a power of 2
        d = c # assign first mod value to d
        for digit in binary[1:]: # step through the remaining digits in the binary representation
            c = c * c % m # calculate the new square of the remainder and take the mod of m
            d = c # assign the result to d for returning
    else: # if exponent is not a power of two
        for digit in binary: # step through every digit in the binary representation
            if firstEntry: # if this is the first iteration
                firstEntry = False # change flag to false
                if digit == '0': # and make the decision based on whether the first digit is a 1 or zero

                    continue # if digit is zero, continue
                else: # else, if this is significant in the binary representation
                    d = c # assign the first value of c mod m to d

            else: # continue after the first iteration to calculate the remaining square c mod m
                c = c *c % m # calculate the new square and take the mod of m
                if digit == '1': # if this digit is in the binary representation of e
                    d = d * c # multiply the current value of d by the new c


    return d % m # return the product of the multplications of the significant binary digits mod m


print(FastModularExponentiation(34, 12, 13))