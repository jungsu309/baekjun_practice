#그리디 실전문제 - 숫자 카드 게임
#2021.08.19

#N-행의개수, M-열의개수
N,M = map(int, input().split())

#입력받기 -matrix로 만들어보자. 생각하기는 쉬운 방법
card=[]

#card = list(map(int, input().split()))
for i in range(N):
    card.append(list(map(int, input().split())))

#어떤 행에서의 가장 작은 숫자가 가장 큰 것을 찾기.
#포문을 행만큼 도는데 거기서 가장 작은 숫자를 찾고, 그거끼리 비교해서 제일 큰 숫자 출력하기

minimumlist=[]
for i in range(N):
    #각 행에서의 가장 작은 숫자찾기
    minimumlist.append(min(card[i]))
#작은거중에 큰거
print(max(minimumlist))


#좀더 좋은방법 - 이중리스트 말고 그냥 리스트로 해도 된다! 속도차이는 많이 안날거같지만 공간적으로 낭비 일듯
