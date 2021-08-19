#그리디 실전문제 - 큰 수의 법칙
#2021.08.19

#N-배열의 크기, M-숫자가 더해지는 횟수, K-연속가능횟수
N,M,K = map(int, input().split())

#N개로 구성된 리스트
numlist = list(map(int, input().split()))

# (제일큰거 *k개 + 그다음 큰거 1개 ) 반복하면 될거라고 생각
# 정렬하면 맨처음거, 그 다음거 두가지만 이용하면 됨
numlist.sort(reverse=True)
#print(numlist)


result=0
#step1. 큰거3개 + 그다음 반복 횟수 이용하여 계산(반복이 안되는 경우 그냥 0상태)
result = (numlist[0]*K + numlist[1]) * (M//(K+1))

# step2.묶음으로 나눠지지 않는 애들은 나머지만큼 큰수곱해서 더해주기
result = result + numlist[0] * (M%(K+1))

print(result)
