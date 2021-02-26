def solution(clothes):
    #clothes - dict(hash)모양.
    answer = 1
    newdict={}
    for i in clothes:
        if i[1] not in newdict:
            newdict[i[1]] = 1
        else:
            newdict[i[1]] = newdict[i[1]]+1


    V = newdict.values()

    for i in V:
        answer = answer * (i+1)

    answer = answer-1
    
    return answer


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))


