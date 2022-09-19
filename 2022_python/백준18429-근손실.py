N,K = map(int,input().split())

kit=list(map(int,input().split()))
#print(kit)

weight=500

cnt = 0
li=[]
def bt(weight):
    global cnt
    #500 유지 확인
    if weight >= 500:
        if len(li) ==N:
            #print("만족한것",weight)
            cnt = cnt+1
    else:
        return#뒤에 더 할필요도없음 지금꺼 빼고 다른 키트 넣어야함

    #kit사용 전에 매번 4씩 감소
    weight= weight-K
    
    for i in range(len(kit)):
        #중복으로 사용되면 안됨. 키트번호로 판단함(무게 같아도됨)
        if i not in li:
            li.append(i)
            #print(weight+kit[i],i, li)
            bt(weight + kit[i])
            li.pop()
        
bt(500)
print(cnt)
