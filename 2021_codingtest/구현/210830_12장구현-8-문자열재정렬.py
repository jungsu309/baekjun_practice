#20210830-12장 구현 08 문자열 재정렬

#문자 오름차순으로 정렬 + 숫자끼리 더해서 마지막에 붙이기

S = list(input())#문자열 리스트로 받기

S.sort()#숫자가 앞으로 오게 된다

print(S)
sum_int = 0
cnt=0
for i in (S):
    if ord(i) >= ord('0') and ord(i) <= ord('9'):
        sum_int = sum_int + int(i)
        cnt = cnt+1

S2 = S[cnt:]
S2.append(str(sum_int))
print(S2)

print(''.join(S2))
