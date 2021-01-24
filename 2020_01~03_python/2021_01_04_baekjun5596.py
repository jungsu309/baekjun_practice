a,b,c,d = map(int, input().split())
A,B,C,D = map(int, input().split())

sum1 = a+b+c+d
sum2 = A+B+C+D

if sum1 >= sum2 :
    print(sum1)

else:
    print(sum2)
