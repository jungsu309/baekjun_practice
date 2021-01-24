N = int(input())

cnt = 0
while N != 1:
    if N % 3 == 0:
        N = N // 3
    elif N%2 ==0:
        N = N // 2
    else :
        N = N-1
        
    cnt = cnt+1

print(cnt)
