n, k = map(int, input().split())

cnt = 0
while True:

    if n // k < 1:
        cnt = cnt+ (n-1)
        break

    if n % k == 0:
        n = n//k
        cnt = cnt+1

    else:
        div = n%k
        n = n - div
        cnt = cnt+ div

print(cnt)
#시간복잡도랑 관련없는if문이니까 괜찮겠지?

#교안코드좀 알아보기 어려운듯....
n, k = map(int, input().split())

result=0
while True:
    target = (n//k)*k#나머지 다 날려버림. 딱 나눠지는 숫자로 바꿈.
    result = result + (n-target)#나머지부분을 수행 숫자로 넣어줌.
    n = target#n은 앞으로 딱 떨어지는 수 이다.

    if n<k:#한번 나눳을때 몫이 1보다 작은 경우. 한번도 안나뉘는 작은 수 일때 탈출
        break

    result = result +1#나눴을때 값이 1보다 크면 수행 숫자 1더해주고
    n//=k#n은 앞으로 나눈 몫

result = result + n-1#1이 될때까지 빼줌.
print(result)


#if문을 줄여보는 방법으로 다시 코드 짜보기

n, k = map(int, input().split())

cnt = 0
while True:

    div = n%k

    b = n - div#나머지 부분 날려서 딱떨어지는 숫자 만들기. 이미 나눠떨어지는 수여도 괜찮음. 
    cnt = cnt+div

    n = n//k#나눠떨어지니까 나눠줌.
    cnt = cnt+1

    if n < k :# 1이 될때까지 빼줌
        cnt = cnt + (n-1)
        break

print(cnt)
