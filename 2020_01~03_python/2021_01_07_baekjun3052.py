result = []
result2 = []
for i in range (0,10):
    n = int(input())
    res = n%42
    result.append(res)

cnt = 0
for i in result:
    if i not in result2:
        result2.append(i)

print(len(result2))
