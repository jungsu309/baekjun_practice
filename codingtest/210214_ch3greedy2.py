#내가 단순하게 생각한 방법

n, m, k = map(int, input().split())

#n만큼의 배열 받기. 근데 파이썬은 여기서 n필요가 없음..
num = list(map(int, input().split()))
#print(num)


num.sort(reverse=True)
#m번 더하기
sum=0
count=0
while count<m:

    for i in range(0,k):
        sum = sum + num[0]
        count = count+1

        if count >= m:
            break

    if count >=m:
        break
    
    sum = sum + num[1]
    count = count+1
print(sum)


#책에서 알려준 처리속도 빠른 계산법
#무조건 제일큰거랑 그다음거만 쓰임 나머진 아예 안쓰임

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
num.sort(reverse=True)

#합은 m/(k+1) 의 몫 은 확실하게  num[0]*k +num[1] 하고
#나머지만큼 num[0]을 더하는 방법

rep = m//(k+1)
div = m %(k+1)

sum = rep*(num[0]*k + num[1]) + div*num[0]
print(sum)
