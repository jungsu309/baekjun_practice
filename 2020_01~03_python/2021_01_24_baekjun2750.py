NList=[]
N = int(input())

for i in range (0,N):
    n = int(input())
    NList.append(n)


NList.sort()
for i in NList:
    print(i)
