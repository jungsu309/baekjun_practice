def solution(n, lost, reserve):
    #n = 전체 학생수
    #lost = 체육복을 도난당한 학생의 번호(배열) []
    #reserve = 여벌으 체육복을 가지고 있는 학생의 번호(배) []

    answer = 0
    answer = answer + n - len(lost)

    for i in range(0,n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)
            answer= answer +1

    start = str(1)
    end = str(n)

    for i in range(1, n+1):


        if i in lost and (i - 1) in reserve:
            reserve.remove(i-1)
            lost.remove(i)
            answer= answer +1

        if i in lost and (i + 1) in reserve:
            reserve.remove(i+1)
            lost.remove(i)
            answer = answer+1

    return answer


ans = solution(8, [1,2,4,6],[1,2,4,6])
print(ans)
