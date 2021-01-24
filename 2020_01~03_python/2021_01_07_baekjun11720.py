T = int(input())
number = int(input())

num=[]
for i in range(0, T):
    num.append(number%10)
    number = number//10

#평균구하기
sum = 0
for m in num:
    sum = sum + m

print(sum)
