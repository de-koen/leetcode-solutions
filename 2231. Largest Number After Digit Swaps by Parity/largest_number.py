"""
Creates list of digits from input number, 
sorts odd and even digits and puts them into original positions 
by their parity and in descending order 
"""
num = int(input())

digits = list(map(int, str(num)))
odd = []
even = []

for digit in digits:
        if(digit % 2 == 0):
            even.append(digit)
        else:
            odd.append(digit)

odd.sort()
even.sort()
result = ""

for digit in digits:
        if(digit % 2 == 0):
            result += str(even.pop())
        else:
            result += str(odd.pop())
            
print(result)
            