def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    newdict={}

    cnt = 0
    for i in participant:
        try:
            newdict[i] = completion[cnt]
            if i != newdict[i]:
                answer = i
                break
            cnt = cnt+1
        except:#크기가 다를경우
            answer = i

    return answer


print(solution(["kiki","eden","eden"],["eden","kiki"]))

#정확도 50, 효율성 50 -> 100점
