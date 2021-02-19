N = int(input())

money = list(map(int, input().split()))

money.sort()

#합할애들을 넣어놓는 곳
#sumList=[]
#전 거랑 비교해야됨. 맨 처음은 if문 항상 만족해야되므로 -1시켜준다.
#Sum_temp=money[0]-1

#for i in range(0, len(money)):
    #맨앞에 숫자를 꺼내고 money에서는 제거.
    #Sum_temp = Sum
    #sumList.append(money.pop(0))
    #Sum = sum(sumlist)

    
    #if Sum_temp + 1 != Sum:
        #원소 자체 값이 있는경우
        #if money.index(Sum_temp +1) > 0 :
            #continue
        #앞의 값을 제거해서 얻는 방법
        #for i in range(0, len(sumList)):
            #sumList[i] = 0
            #Sum = sum(sumlist)
        #break

#위는 이상한 짓 한거..

sum = 0
ans = 0

if money[0] != 1:
    ans = 1

else:
    #마지막 전꺼까지 돔
    for i in range(0, len(money)-1):
        sum = sum+money[i]
        ans = sum+1
        # 다음 숫자가 전체 합+1 보다 크면
        if sum + 1 < money[i+1]:
            ans = sum+1
            break
            #마지막 전거일때 마지막 더해줌.
        if i == len(money)-2:
            sum = sum+money[len(money)-1]
            ans = sum+1
            
print(ans)

