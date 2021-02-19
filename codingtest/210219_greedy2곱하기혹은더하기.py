S = input()
num = list(S)
num = list(map(int, num))

cul = num[0]

#처음껀 cul에 저장해줬으므로 맨 앞에껀 없어도된다!
for i in range(1, len(num)):
    if cul == 1 or cul == 0:
        cul = cul + num[i]
    else:
        if num[i] == 1 or num[i] ==0:
            cul = cul + num[i]
        else:
            cul = cul *num[i]

print(cul)
