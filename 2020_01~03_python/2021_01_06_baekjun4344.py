T = int(input())


score=[]
result =[]

for i in range(0,T):
    sum = 0
    cnt = 0
    score = list(map(int,input().split()))
    n = score[0]#해당 숫자만큼 숫자받음..

    for i in range (1,n+1):
        sum = sum + score[i]

    avg = sum/n

    for i in range(1,n+1):
        if score[i] > avg :
            cnt= cnt+1
            
    percent =(cnt/n) * 100
    result.append(percent)

    
for i in range(0, len(result)):
    print(str(format(result[i], "5.3f")) + "%")
