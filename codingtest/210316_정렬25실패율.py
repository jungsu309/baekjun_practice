def solution(N, stages):
    answer = []
    stages.sort()
    stage_dict={}
    for i in range(1, N+2):
        stage_dict[i] =0

    for i in stages:
        try: stage_dict[i] = stage_dict[i]+1
        except: stage_dict[i] = 1
        
    stage_values= list(stage_dict.values())

    failure_list=[]
    for i in range(0,N):
        #0으로나눌때!
        if sum(stage_values[i:]) ==0:
            failure_list.append(0)
            continue
        failure = stage_values[i] /sum(stage_values[i:])
        failure_list.append(failure)

    failure={}
    for i in range(1, N+1):
        failure[i] =failure_list[i-1]

    failure = sorted(failure.items(), key=lambda x: -x[1])

    for i in range(N):
        answer.append(failure[i][0])
    
    return answer


print(solution(5,[2,1,2,6,2,4,3,3]))
