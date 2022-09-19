#테스트 케이스 수 T
T = int(input())
#주가 담을 list(전부)
S=[]
for i in range(0,T):
    #날의 수 N
    N = int(input())
    S.append(list(map(int, input().split())))

#print(S)


#뒤에서 부터 하는게 좋다.- 구글봄
#맨뒤수가 max일때 ->앞 값이랑 차이 구하기
#맨 뒤수가 max가 아닐때 - max가 중간에 있을 때 -> max 업데이트 시키기
for t in range(0,T):
    answer = 0
    s = S[t]
    max_ = 0#자연수라서 0이하 안나옴
    for i in range(len(s), 0,-1):
        #뒷쪽부터 볼때- 지금 보고있는 곳이 max일때
        if max_<s[i-1]:
            #max update
            max_ = s[i-1]
        #지금값이 max보다 작은 경우 차이를 더해준다
        else:
            answer = answer +(max_-s[i-1])
    print(answer)
    
