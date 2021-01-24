N = int(input())


#여태까지 나온 생성자들을 모아논 list
result_final=[]
for i in range (1,N+1):

    result =i
    #각 자리수를 따로 모은 list
    result_list=[]
    while(result > 0):

        #나머지(해당 자리의 자연수)
        result2 = result % 10
        #그 다음 자리를 알기위해 몫을 이용
        result = result // 10
        
        result_list.append(result2)

    if N == i + sum(result_list):
        result_final.append(i)

if sum(result_final) > 0:
    print(result_final[0])
else:
    print("0")

