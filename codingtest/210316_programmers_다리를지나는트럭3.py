from collections import deque

def solution(bridge_length, weight, truck_weights):

    #다리에 해당하는 빈 queue만들기
    queue = deque(maxlen=bridge_length)
    #queue = [0]*bridge_length
    time=1

    #print("시작큐")
    #print(queue)
    #truck_weights가 모두 pop되면 반복문 탈출
    while len(truck_weights) >0:
        #맨 처음 아무것도 없을때 및 다 밀어내서 queue가 0인경우
        if sum(queue) ==0:
            #print("빈 큐")
            #print(queue)
            queue.append(truck_weights.pop(0))
            #print("하나가 추가된 큐")
            #print(queue)
            continue
            
        if sum(queue) + truck_weights[0] > weight:
            #한칸씩 내쫓기
            queue.append(0)
            time = time+1
            #print("내쫓기는 모습")
            #print(queue)

        else:
            #print("추가되기전")
            #print(queue)
            queue.append(truck_weights.pop(0))
            time = time+1
            #print("추가된큐")
            #print(queue)
            
    #truck_weight들이 queue에 다들어가고, 마지막 으로 들어간 애가 나올때까지 걸리는 시간까지 계산
    time = time + bridge_length
        
    return time

#print(solution(2, 10, [7,4]))#답 5
#print(solution(2, 10, [7,3]))#답 4
#print(solution(2, 10, [7,4,5,6]))#답 8
#print(solution(10,10,[7,4,5,6]))#답 32

print("fuck")

