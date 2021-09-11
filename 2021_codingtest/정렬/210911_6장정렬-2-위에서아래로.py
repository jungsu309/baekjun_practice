#20210911-6장 정렬 2. 위에서 아래로

#숫자 개수가 500개 이하로 적고, 숫자 범위는 1~100000개. 라이브러리를 써되 무방하다고 한다.

N = int(input())

array=[]
#숫자 받기
for i in range(N):
    n = int(input())
    array.append(n)

#array를 내림차순 정렬하기

array.sort(reverse = True)
print(array)
