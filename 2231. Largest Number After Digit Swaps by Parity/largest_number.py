number = list(str(input()))

for i in range(len(number)):
    maxVal = int(number[i])
    maxIdx = i
    for j in range(i + 1, len(number)):
        if int(number[i]) % 2 == int(number[j]) % 2 and int(number[j]) > maxVal:
            maxVal = int(number[j])
            maxIdx = j
    number[i], number[maxIdx] = number[maxIdx], number[i]
    
anwser = ""

print(anwser.join(number))