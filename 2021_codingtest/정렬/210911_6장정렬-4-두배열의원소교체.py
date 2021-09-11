#20210911-6장 정렬 4. 두 배열의 원소 교체

#A 합이 가장 커야 하니까 A에서 제일 작은거, B에서 가장큰거 둘이 스왑하기. 최대 K번의 기회가 있다.

N, K = map(int, input().split())


a = map(int,input().split())
A = list(a)
b = map(int,input().split())
B = list(b)

#print(A)
#print(B)

#A를 오름차순, B를 내림차순 정렬 시킴
A.sort()
B.sort(reverse = True)

#최대 K번이니까 불필요하다면 서로 안바꿔도됨.
for k in range(K):
    if A[k] >= B[k]:
        #바꿀 필요가 없음.
        break
    else:
        #서로 자리 바꿔주기
        A[k], B[k] =  B[k], A[k]


print(sum(A))
