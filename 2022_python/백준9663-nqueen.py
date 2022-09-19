from collections import deque
N = int(input())

queen=deque()
cnt = 0

def bt(y):
    global cnt
    flag =True
    flaglist=[]
    #검사
    now = queen[-1]#방금 막 들어온 것
    row = len(queen)-1
    #print("now : ",now, "row:",row)
    #print("now : ",now, "queen:", queen)
    #조건을 만족하면 계속 진행해도되고, 조건을 만족하지 못하면 포문을 돌지 못하고 pop되야함.
    
    for i in range (len(queen)-1):
        #print("queen[i]와 i",queen[i],i)
        #print("flag상태", flag)
        if now != queen[i]:
            #대각선 오른쪽
            if (queen[i] + (row-i)) < N:
                if now != (queen[i] +(row-i)):
                    #print("성공! now : ",now)
                    flag = flag & True
                    #print("****성공일때 flag",flag,type(flag))
                else:
                    flag = flag & False
                    #print("오른쪽 실패 - falg", flag)
            #대각선 왼쪽
            if (queen[i] - (row-i)) > -1:
                if now != (queen[i] - (row-i)):
                    #print("성공! now : ",now)
                    flag = flag & True
                    #print("*****성공일때 flag",flag, type(flag))
                else:
                    flag = flag & False
                    #print("왼쪽 대각 위치 값",queen[i] - (row-i))
                    #print("왼쪽 실패,-flag",flag)
        else:
            flag=False
            #print("실패일때 flag-그냥보려고..",flag, type(flag))


    #if flag ==True:
        #print("falg가 true일때 now, queen",flag, now, queen)

      
    #어디선가 만족하지 못한경우
    if flag == False:
        #print("어디선가 false가 된 now. 더이상 포문이 돌면 안되고 now 가 바뀌어야함!!",now)
        return

    if flag == True and len(queen) ==N:#방금 들어왔던게 모든 조건을 만족하면서 전체 queen 리스트가 N개가되면-전부다한것임
        cnt = cnt+1
        #print("cnt세주기 제발",cnt)
        return


    
    #지금 놓은곳의 두번째 행부터 검사
    for col in range (N):# 각 열을 확인
        queen.append(col)
        #print("포문에서의 col", col, "포문에서의 queen",queen)
        bt(col)
        queen.pop()

       
#시작 : 0,0부터. ->행은 항상 고정순서라서 열만 봐주자.
#첫번째는 그냥 넣어줘야함
for i in range(N):
    queen=[]
    queen.append(i)
    bt(i)

print(cnt)
