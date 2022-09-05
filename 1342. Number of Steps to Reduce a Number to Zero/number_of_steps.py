#Simple solution
"""
def numberOfSteps(self, num):
    steps = 0
    while (num > 0):
        if (num % 2) == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps
"""

#Wise solution
#Explanation:
'''
Last digit in binary representation of a number tells us if it's even or odd. If the last digit is 0 then it's even, 
if it's 1 then it's odd. When the number is odd we subtract 1 which makes last the last digit 0. When the number is 
even we divide it by 2 which equivelent to shifting bits to the right by 1. To make the binary representation shorter
(which means bringing our number closer to zero) for each 1 in it we need to make 2 steps (substract then divide) 
while for 0 number of steps is 1 (divide). So the anwser will be the (length of the binary representation - 1) + 
the number of 1 in it. Exception: zero as input.
'''
"""
def numberOfSteps(self, num):
        if (num != 0): 
            return(num.bit_length() - 1 + bin(num).count("1"))
        else:
            return 0
"""