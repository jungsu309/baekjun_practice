N,M = map(int, input().split())

li=[]

def backtracking():
    if len(li) == M:#수열의 길이를 만족하면
        #print(li)
        for i in li:
            print(i, end=' ')
        print()
    else:
        for i in range(1, N+1):#1부터 시작이라서
            if i not in li : #현재 리스트에 i가 없어야해서!
                li.append(i)
                backtracking()
                li.pop()
backtracking()
