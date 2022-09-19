N = int(input())

cnt = 0
row = [0]*N

def promising(x):
    #print("왜두번나와?")
    for i in range(x):
        if row[x] == row[i] or abs(row[x]- row[i]) ==abs(x-i):
        # 열이 같은지. 행이랑 열이랑 같은 간격으로 떨어져있는지 확인
            #print("false일때다. x,i : ",x,i)
            return False
        
    return True
            

    
def bt(x):
    global cnt
    if x ==N:#N번째 넣을떄! - nqueen 성공한 경우
        #print("찾음")
        cnt = cnt+1
        return

    else:
        for i in range(N):
            row[x]=i#x:행, i:열
            #print("x,i",x,i)
            if promising(x) == True:
                #print("promising 한 상태라서 x+1도 진행해줄거다")
                #다음 행에 넣을거 고르기
                bt(x+1)#계속 재귀. pop할 필요가없는이유가.. promising에서 전부 만족하기때문이다.
            #print("promising이 false일때다. ",x, promising(x),"얘는 어디로 가지? 그냥 끝나면 어떻게 되는거지?")
        
    


bt(0)
print(cnt)
