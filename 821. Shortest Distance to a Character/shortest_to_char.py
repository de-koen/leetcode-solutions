string = str(input())
letter = str(input())

indices = [i for i, char in enumerate(string) if letter == char]

result = []

for i in range(len(string)):
    if (len(indices) > 1):
        if abs(i - indices[0]) >= abs(i - indices[1]):
            indices.pop(0)
    result.append(abs(i - indices[0]))
        
print(result)