a = int(input())
b = int(input())
c = int(input())

answer=[]
culculate = a*b*c
#print(culculate)

while True:
    result = culculate % 10 #나머지

    
    culculate = culculate // 10 #다음자리 숫자
    
    answer.append(result)

    if culculate == 0 :
        break

c0 = answer.count(0)
c1 = answer.count(1)
c2 = answer.count(2)
c3 = answer.count(3)
c4 = answer.count(4)
c5 = answer.count(5)
c6 = answer.count(6)
c7 = answer.count(7)
c8 = answer.count(8)
c9 = answer.count(9)

print(c0)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)
