#20210830-12장 구현 9 문자열 압축

#이거 저번에도 몰랐었는데 답지를 본적이 한번도 없어서... 전혀 감을 못잡고있어가지고 그냥 답지보고 공부함.
#페이지 코드

def solution(s):
    answer = []
    
    #한 문자로 된 경우
    if len(s) ==1:
        answer = 1

    for i in range (1,(len(s)//2)+1):#마지막 미포함이니까.. 1 더해줌 1부터 차례대로 크기 키워가면서.
        each_result=''#포문을 한번씩 돌때마다 생기는 결과 str을 담는곳
        cnt=1#맨 첫번째 길이 잡을때 한번 겹치고 시작하기때문
        check=s[:i]#자르는 문자

       for j in range(i, len(s), i):#i부터 끝까지 i 마다 건너뛰면서 찾기
           if check == s[j:j+i]:# 어느시점 j부터 i글자가 check랑 같은지 확인-> 중복되는지 확인
               cnt = cnt+1
            else:#check랑 달라지는 순간 each_result에 저장시킴
                if cnt !=1:#한번이라도 겹친게 있었다
                    each_result = each_result + str(cnt) + check
                else : #겹친게 없었던 경우 따로 숫자를 넣어줄 필요없음(1인경우 생략해도되기때문)
                    each_result = each_result + check
                #check를 다음꺼로 바꿔주고 나머지 랑 계속 비교해주기. aabb면 check가 a였다가 b로 바뀌는 거임.
                check = s[j:j+i]
                #세는거도 다시 세는거니까 cnt 초기화 해줌
                cnt=1
        if cnt != 1:#마지막 check에 대한거 처리 해줘야함 왜냐면 달라지는 포인트에 each_result 뒤에 적는건데
                #마지막의 경우 달라지는 포인트가 없기 때문에 한번 따로 해줘야함
            each_result = each_result + str(cnt) + check
        else:
            each_result = each_result  + check
        #길이가 i였을때 한번 끝난거임. 포문이 한번 끝날때마다 그때 수행 결과를 넣어준다. 근데 이때 길이가 제일 중요하니
        #길이만 취급해준다
        answer.append(len(each_result))

    #answer 리스트 중 제일 숫자가 작은것이 답이다.
    return min(answer)

#중복이 끝나는 시점에서 새로운 중복찾기를 하는 포인트가 핵심이었던거같다. 그리고 i있는 포문에서 한번씩 돌때마다 결과를
#모으면 비교를 쉽게 할수 있겠다는 걸 느꼈다....
