def numberOfSteps(self, num):
    steps = 0
    while (num > 0):
        if (num % 2) == 0:
            num >>= 1 #faster equivalent of num /= 2
        else:
            num -= 1
        steps += 1
    return steps