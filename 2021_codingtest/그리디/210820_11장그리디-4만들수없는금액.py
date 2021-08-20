#그리디 기출문제 - 만들 수 없는 금액
#2021.08.20

#해당 숫자들로 만들 수 없는 금액의 최솟값을 구하기(1부터 시작)

N = int(input())
Numlist = list(map(int, input().split()))

#정렬 하면 계산이 더 쉬울것 같다
Numlist.sort()

#11188면 4부터 만들 수 없다
#1122 10이면 123456까지 만들수 있다
#자기 앞쪽거 전부 +1 = 자기  이면 틈이 없다 

# 1234 11 -> 10까지 만들고 11 다음 12 13 14 15 16쭉 되고 전부 다 더한게 마지막으로 가능한 정수

costsum=0
for i in Numlist:
    #틈이 없는 경우
    if costsum + 1 >= i:
        costsum = costsum + i
    #못만드는 경우(틈이 있는 경우)
    else:
        print(costsum+1)
        break
    
    #중간에 만들수 없는 금액이 없어서 끝까지 다 구한 경우(마지막까지 더하는 경우)
    if i == max(Numlist):
        print(costsum+1)

#방법이 어려운 문제였다. 저번에 했던 내용이라서 풀 수 있었던 것 같다. 안해봤으면 못풀었을 듯
