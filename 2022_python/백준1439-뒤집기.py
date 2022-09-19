#숫자가 바뀌는 지점 개수 ->짝수면 //2 홀수면 //2 +1
#4->2 6->3 1->1 3->2

#숫자가 바뀌는 지점을 찾는것이 문제

#문자열 S
S = input()

#숫자가 바뀌는 모습 -> 10, 01

#10찾기
count_10 = S.count('10')
#print(count_10)

#01찾기
count_01 = S.count('01')
#print(count_01)

count_change = count_10 + count_01
#짝수
if count_change %2 ==0:
    answer = count_change//2
#홀
else:
    answer = count_change//2 +1

print(answer)
