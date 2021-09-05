#20210830-12장 구현 07. 럭키스트레이트

#반으로 나눴을 때 양쪽 합이 같을 때. 럭키, 아닐때 레디

#입력값
N = input()#리스트형태

front=0
back=0

for i in range (len(N)):
    if i <len(N)/2:
        front = front + int(N[i])
    else:
        back = back + int(N[i])

if front == back:
    print("LUCKY")
else:
    print("READY")

