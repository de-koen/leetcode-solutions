from itertools import chain

s = str(input())
c = str(input())

#two passes concatenated in one
n = len(s)
pos = -n
res = [n] * n
for i in chain(range(n), range(n)[::-1]):
    if s[i] == c:
        pos = i
    res[i] = min(res[i], abs(i - pos))
        
print(res)