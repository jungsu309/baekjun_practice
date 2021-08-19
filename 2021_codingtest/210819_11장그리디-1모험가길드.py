#그리디 기출문제 - 모험가 길드
#2021.08.19

#N-모험가 수 ,두번째줄에 그 숫자만큼 각각의 공포도

N = int(input())
traveler = list(map(int, input().split()))

#제일 작은애 기준으로 그룹을 짜보자.
traveler.sort()
#공포도만큼 pop을 해주기
group = 0
for i in traveler:
    #공포도 보다 적은 인원이 남아있을 경우
    if len(traveler) < i:
        break
    #공포도 만큼 같은그룹으로 데려가기
    for j in range (i):
        traveler.pop()
    group = group + 1


print(group)

#문제인부분-이중포문 아니여도 풀수 있을거 같은데, 좋은 방법이 생각이나지 않는다..
