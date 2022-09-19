N,M = map(int, input().split())
#print(N,M)

li=[]
def backtracking():
    if len(li) == M:
        for i in li:
            print(i,end = " ")
        print()
    else:
        for n in range(1, N+1):
            #print("포문",n)
            #맨 첨에
            if len(li) ==0:
                #print(n,li)
                li.append(n)
                backtracking()
                li.pop()
                #print("pop함",li)
            else:
                if li[len(li)-1]<n:
                    li.append(n)
                    backtracking()
                    li.pop()

backtracking()
