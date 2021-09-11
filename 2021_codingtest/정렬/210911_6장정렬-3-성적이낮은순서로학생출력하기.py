#20210911-6장 정렬 3. 성적이 낮은 순서로 학생 출력하기

#숫자 개수가 500개 이하로 적고, 숫자 범위는 1~100000개. 라이브러리를 써되 무방하다고 한다.

N = int(input())

array=[]
#이름, 숫자 각각 받기
for i in range(N):
    n,s = input().split()
    array.append([n,int(s)])
print(array)

#array를 오름차순 정렬

array.sort()

for i in range(len(array)):
    print(array[i][0], end=' ')
