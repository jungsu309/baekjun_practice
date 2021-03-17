from collections import deque
#다리(bridge)가 큐 인듯 하다.
#맨 앞에 있는거 빼기 : queue.popleft()
def solution(bridge_length, weight, truck_weights):
    #bridge_length, weight, truck_weights 모두 리스트
    #다리에 해당하는 빈 queue만들기
    queue = deque(maxlen=bridge_length)
    #맨 처음에 숫자 넣어줄때 포함해서 시작.
    time=1
    
    #truck_weights 순서대로 다리에 들어가기(마지막 전까지)
    for i in range (len(truck_weights)):
        queue.append(truck_weights[i])
        print("넣어주는구간")
        print(queue)
        for k in range(bridge_length):
            #꽉차서 못들어가는 상태
            if i < len(truck_weights)-1 and sum(queue) + truck_weights[i+1] > weight:
                print("더들어오면 꽉차서 앞으로 밀어주는 구간")
                print(queue)
                queue.append(0)
                time = time+1
                print("밀어준 결과")
                print(queue)
            #들어갈 수 있는상태
            elif i < len(truck_weights)-1 and sum(queue) + truck_weights[i+1] <= weight:
                time = time+1
                #1초 지나게 해주고 윗부분에서 큐에 넣어주기
                break
    #포문 다돌아서 마지막 까지 잘 들어갔을 때 마지막 친구가 나와야하므로
    time = time+bridge_length
    

    answer = time
    return answer


#print(solution(2, 10, [7,4]))#답 5
#print(solution(2, 10, [7,3]))#답 4
print(solution(2, 10, [7,4,5,6]))#답 8
