#음수가 짝수개면 무조건 -끼리 곱하기
#음수가 홀수개면 - 곱할때 큰수부터 곱해주기 ->이때 0이 있으면 남은 음수 하나랑 곱해서 없애주기
#음수가 없으면 그냥 큰수끼리 묶어서 곱하기
#양수중 1이있으면 곱하지말고 더하기

#길이 N
N = int(input())
Negative=[]#음수 담는곳
Positive=[]#양수 담는곳
for i in range(0,N):
    n = int(input())
    if n <0:
        Negative.append(n)
    else:
        Positive.append(n)
#print(Negative,Positive)

#정렬시켜주기 - 오름차순 
Negative_sort = sorted(Negative)#오름차순
Positive_sort = sorted(Positive, reverse = True)#내림차순

#print(Negative_sort)
#print(Positive_sort)

#음수가 있을때 ->짝수개일때 홀수개일때 나눠서 생각해보자
answer=0
if len(Negative_sort)>0:
    #홀수개일때
    if len(Negative_sort)%2 != 0:
        #positive에 0이 없을때 - 먼저 더해주기
        if 0 not in Positive_sort:
            answer = answer + Negative_sort[len(Negative_sort)-1]

        #0이 있으면 둘이 곱한다침 -음수쪽에서 따로 하는 일 없음 
            
        #방금 계산한 그 음수중에서 제일 큰값 지우기
        #print(Negative_sort[len(Negative_sort)-1])#제일 큰값
        Negative_sort.pop(len(Negative_sort)-1)

    #위 작업을하면 무조건 짝수개가된다.

    #혹시 다 지워버려서 0일수도있으니까
    if len(Negative_sort)>0: 
        #두개씩 곱하기 
        for i in range(0,len(Negative_sort),2):
            answer = answer + Negative_sort[i]*Negative_sort[i+1]

#print("음수부분계산",answer)

#양수 부분
#홀수이면 제일 뒤에거 먼저 계산하고 똑같이 2개씩 곱해서 계산.
#다만 1이 있을때 미리 빼고 시작한다.
#0도 미리 처리해준다.
if len(Positive_sort)>0:
    #음수부분에서0을 처리하지 않은경우- 음수가 아예없을때
    if Positive_sort[len(Positive_sort)-1] ==0:
        #0 그냥 빼버리기- 여러개일 수 있다.
        Positive_sort = [i for i in Positive_sort if i != 0]
        #위 작업을통해 리스트에 아무것도 남지 않게 된 경우

    #1 미리 계산. 곱하는거보다 더하는게 나은 숫자이기 때문-->1이 여러개일 수 있다.
    if (len(Positive_sort)>0) and (Positive_sort[len(Positive_sort)-1] ==1):
        #1의 개수를 세기
        count_1 = Positive_sort.count(1)
        answer = answer + count_1
        #1만 전부 지워주기(구글코드 참고)
        Positive_sort = [i for i in Positive_sort if i != 1]
        #print("1지우기!!",Positive_sort)

    #홀수일때 뒤 숫자 미리 더해주기
    if len(Positive_sort)%2 !=0:
        answer = answer + Positive_sort[len(Positive_sort)-1]
        Positive_sort.pop(len(Positive_sort)-1)

    #위 작업을 하면 무조건 짝수개가된다
    #혹시 다 지워버려서 0일수도있으니까
    if len(Positive_sort)>0:  
        #두개씩 곱하기
        for i in range(0,len(Positive_sort),2):
            answer = answer + Positive_sort[i]*Positive_sort[i+1]
#정답
print(answer)
