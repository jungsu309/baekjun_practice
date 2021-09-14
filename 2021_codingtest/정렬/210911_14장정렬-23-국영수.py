#20210911- 14장 정렬 23.국영수

#이름, 국어, 영어, 수학 순으로 입력받음
#국어 감소, 영어 증가, 수학 감소 순으로 정렬 후 이름만 출력
import sys
input = sys.stdin.readline

N = int(input())
array=[]
for n in range(N):
    n,k,e,m = input().split()
    array.append([n,int(k),int(e),int(m)])
#print(array)

#구글에 검색해봄.
array.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
#print(array)

for i in range(N):
    print(array[i][0])
