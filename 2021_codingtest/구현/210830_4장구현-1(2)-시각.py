#20210830-4장 그리디 예제문제 2) 시각

#N시 59분 59초까지 3이 들어가는 횟수를 구하기
#완전탐색이용한다고 한다
#전부 다 세도 2초안에 셀수 있어서 괜찮다고 한다.

N = int(input())
count=0

for i in range (N+1):#H(끝자리 미포함이기 때문)
    for j in range(60):#M
        for k in range (60):#S
            if '3' in str(k)+str(j)+str(i):
                #str(k) or str(j) or str(i)
                #왜 더하기 말고 or로 하면 안될까? 어차피 한번 씩 돌아가면서 계속 하는데 ..... 잘모르겠다!!!
                count= count+1
print(count)
