N,S =map(int,input().split())

Z = list(map(int, input().split()))

li=[]
cnt = 0
def backtracking(start):
    global cnt
    #print(li)
    if sum(li) ==S:
        #print(li)
        cnt = cnt+1
        
    for i in range (start, N):
        li.append(Z[i])
        #print(li)
        backtracking(i+1)
        li.pop()
            
backtracking(0)
if S ==0:
    cnt = cnt-1 #아무것도 없을때도 인식하기 때문..(공집합)
print(cnt)
