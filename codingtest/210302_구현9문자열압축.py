def solution(s):
    answer = 0
    answerList=[]
    if len(s) ==1:#a인경우 답 1이어야함 아니면 아래 포문이 안돔
        answerList = [1]
    for i in range(1, len(s)//2 +1):
        tmp_string = ""
        tmp_string = s[0:i]#비교할 문자열
        answer_len = 0
        cnt = 1 #기본은 0 이아니라 1
        for j in range(i, len(s)+1, i):
            if tmp_string == s[j:j+i]:#같을때
                cnt = cnt+1
            else:#다를때
                #전에 한번도 압축 안되었을 때
                if cnt ==1:
                    #앞에 숫자 안붙고 바로 기준 문자열이 쓰임.
                    answer_len = answer_len + len(tmp_string)
                else:
                    #중복이 된 적 있으면 문자열의 길이 - 숫자(길이) + 압축된문자열
                    answer_len = answer_len + len(tmp_string) + len(str(cnt))
                #기준문자열 바꿔주고 다시 cnt 1로 바꿔줌
            
                tmp_string = s[j:j+i]
                cnt = 1

        answer_len = answer_len + (len(s)%i)
        answerList.append(answer_len)
    #print(answerList)
    answer = min(answerList)
                    
                
    return answer

print(solution("a"))
