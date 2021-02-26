def solution(participant, completion):
    answer = ''

    # participant ->list []
    # completion -> list []
    #answer = participant[0] -잘 출력됨.

    participant.sort()
    completion.sort()
    for i in participant:
        if i  not in completion:
             answer = i
             break
        else:
             completion.remove(i)

    return answer


print(solution(["kiki","eden","eden"],["eden","kiki"]))

#정확도 50, 효율성 30 -> 80점

