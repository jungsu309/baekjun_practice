#20210907 - 15장 DFS/BFS 18 괄호변환

#() 개수가 같으면 균형잡힌
#() 짝까지 맞으면 올바른

#P = list(input())#입력이 균형잡힌 상태->올바르게 고치
#answer = ""

def solution(String):

    answer = ""
    
    u=[]
    v=[]
    if len(String) ==0:
        #빈 문자열 반환..
        answer = answer + ''
        return answer
    else:
        #먼저 문자열을 u와 v로두개로 분리해야함. 더이상 분리할 수 없는 균형잡힌 상태여야함.
        right=0#(
        left=0#)
        cnt=0
        for p in String:

            if p ==  '(':
                right += 1
                cnt += 1
        
            elif p == ')':
                left += 1
                cnt += 1
        
            #균형잡힌 u를 획득. 첫 발견시 바로 break
            if right == left:
                u = String[:cnt]
                break

        #print(u)
        v = String[cnt:]
        #print(v)

        #u가 올바른 상태인지 확인하기->앞 뒤가 ( ) 이면 되는것 같다..
        #올바른경우
        if u[0] == '(' and u[cnt-1] == ')' :
            answer += ''.join(u)
            answer += solution(v)
            #print(answer)
            return answer
            #print(answer)
        
        else:
            v_answer = '(' + solution(v)+')'

            #u[1:cnt-1]에 해당하는 요소들 전부 방향을 뒤집어준다
            for i in range(1,cnt-1):
                if u[i] == '(':
                    v_answer += ')'
                elif u[i] == ')':
                    v_answer += '('
            answer = v_answer
            return answer


print(solution("()))((()"))
                        
