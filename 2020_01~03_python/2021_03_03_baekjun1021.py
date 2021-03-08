N, M = map(int, input().split())

wish = list(map(int, input().split()))

queue = list(range(1,N+1))

cnt = 0


for i in wish:
    while True:
    #맨 앞자리에 있을때
        if i == queue[0]:
            queue.pop(0)
            break
        else:
            #전반부에 위치
            if queue.index(i) <= len(queue)/2:
                front = queue.pop(0)
                queue.append(front)
                #print(queue)
                cnt = cnt+1
            #후반부에 위치
            else:
                end = queue.pop(len(queue)-1)
                queue.insert(0,end)
                #print(queue)
                cnt = cnt+1

print(cnt)
