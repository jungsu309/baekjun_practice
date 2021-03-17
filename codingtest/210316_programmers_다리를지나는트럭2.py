from collections import deque

def solution(bridge_length, weight, truck_weights):

    #다리에 해당하는 빈 queue만들기
    queue = deque(maxlen=bridge_length)

    time=0

    #truck_weights 순서대로 다리에 들어가기(마지막 전까지)
    for i in range (len(truck_weights)):
        if sum(queue) ==0:
            queue.append(truck_weights[i])
            time= time+1
            #print("맨 처음 들어오기")
            #print(queue)
            continue
        while bridge_length:
            if sum(queue) + truck_weights[i] > weight:
                #한칸씩 내쫓기
                queue.append(0)
                time = time+1
                #print("내쫓기는 모습")
                #print(queue)

            else:
                #전부다 내쫓은경우 들어오면서 time 카운트 안해도 되는데
                #이미 앞에 뭔가 값이 있는데 들어올 수 있으면 초 세줘야된
                if sum(queue) != 0:
                    time = time+1
                queue.append(truck_weights[i])
                #print("새로 들어온 모습")
                #print(queue)

                break
            
    #맨마지막 트럭 내보내기
    time = time + bridge_length
    answer = time
    return answer



#print(solution(2, 10, [7,4]))#답 5
#print(solution(2, 10, [7,3]))#답 4
#print(solution(2, 10, [7,4,5,6]))#답 8
print(solution(10,10,[7,4,5,6]))#답 32
