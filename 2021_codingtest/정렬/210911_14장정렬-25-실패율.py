def solution(N, stages):
    answer = []
    stages.sort()
    #각 스테이지의개수세기 -> 계수정렬

    counts = [0] * (N+2)#스테이지 클리어한 사람들 마지막자리에 옴
    #0이 없어서..자리 계산 불편하니까 한칸씩 밀기 (N이 5인 경우 0 1 2 3 4 5 6) 
    for i in stages:
        counts[i] +=1
    #print(counts)

    failure=[]
    Sum = len(stages)#전체 인원 넣어놓기
    for i in range(1, len(counts)-1):#12345범주
        if Sum != 0:
            failure.append(counts[i]/Sum)
            Sum -= counts[i]
        else:
            failure.append(0)

    f_dict={}
    for i in range(N):
        f_dict[i+1] = failure[i]

    #정렬해주기
    f_dict = sorted(f_dict.items(), key=lambda x: -x[1])
    #print(f_dict)

    for i in range (N):
        answer.append(f_dict[i][0])
    #print(answer)
    return answer
