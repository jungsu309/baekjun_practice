#테스트 케이스 수 T
T = int(input())
#주가 담을 list(전부)
S=[]
for i in range(0,T):
    #날의 수 N
    N = int(input())
    S.append(list(map(int, input().split())))

#print(S)

#1 2 3 4 5 1 90 이런식이면 무조건 가지고잇따가 마지막에 파는게 좋다
#맨 앞 숫자랑 하나씩 비교?하다가 가장 큰 수 만나면 팔기- 가장 큰 수가 제일 마지막날이면 끝나는거고
#비교하는데 자기 숫자보다 큰거 없으면 pass
#마지막날이 아닌경우 그 다음날부터 다시 첫날처럼 돌림
# 1 2 3 6 4 5 같이 애매한경우  123을 전부 6에서 판다-> 5+4+3 그리고 4때 사고 5때 판다 1=> 13인듯
#그냥 5때 다판다 -> 4+3+2+-1+1 ->9

for t in range(0,T):
    s = S[t]
    #제일 큰 수 찾는다.
    answer=0
    while True: 
        #제일큰수가 제일 마지막에 위치
        if max(s) == s[len(s)-1]:
            for i in range(0,len(s)):
                answer = answer + (max(s)-s[i])
            break
        #제일 큰 수가 맨 앞에 위치
        elif max(s) == s[0]:
            break
        #제일 큰수가 중간에 위치
        else:
            max_index = s.index(max(s))
            for i in range(0,max_index):
                max_index = s.index(max(s))
                #print("리스트 내 최고 큰 값",s[max_index], "위치-인덱스번호", max_index)
            
                answer = answer + (s[max_index]-s[i])
                #print("주가 합",answer)
                #리스트 재정의 - 제일 큰 수 다음부터 다시 
            s = s[max_index+1:]
            #print("남은 리스트",s)
            if len(s) ==0:
                break
    print(answer)
