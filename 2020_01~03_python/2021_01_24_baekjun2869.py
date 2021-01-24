A, B, V = (map(int, input().split()))

cnt = 0
if (V-B)%(A-B) ==0:
    cnt = (V-B)//(A-B)
else: 
    cnt = (V-B)//(A-B)+1
print(cnt)
