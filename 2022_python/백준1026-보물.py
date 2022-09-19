#list 의 length N
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


#B를 재배열 하지 말라고 햇지만, 재배열 하자 어차피 상관없음.
B = sorted(B)# 오름차순 정렬
#제일 큰 B에 제일 작은 A가 와야 하므로
A = sorted(A,reverse=True)

multi_sum=0
for i in range(0,N):
    multi_sum = multi_sum + (A[i] * B[i])

print(multi_sum)
