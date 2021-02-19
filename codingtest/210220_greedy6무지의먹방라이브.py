#최소로 생각해보려고 한 코드. 효율성 2번만 성공하고 나머지 다 실패.  정확성 16.1, 효율성 7.1
def solution (food_times,k):
    ans = 0
    food_list=[]
    #최소 기준으로 생각
    min_times = min(food_times)*len(food_times)

    if sum(food_times) <= k:
        ans = -1
        
    elif min_times > k:
        ans = k % len(food_times) +1
    
    else:
        k = k-min_times
        for i in range(0,len(food_times)):
            food_list.append(i)

        #cycle= k//len(food_times)+1
        cycle = sum(food_times)//len(food_times)+1

        for j in range(0, len(food_times)):
           food_times[j] = food_times[j] -min(food_times)


        for i in food_list*cycle:
            if food_times[i] > 0:
                if k == 0:
                    ans = i +1
                    if ans > len(food_times):
                        ans = ans - len(food_times)
                    break
                food_times[i] = food_times[i] -1
                k=k-1
            
    return ans


print(solution([3,1,2], 5)) #3
print(solution([4,2,5,6,3,1,5,8], 13))
print(solution([1,1,1,1], 4))



#정확도는 다 맞는데 효율성 하나도 안맞는 코드
def solution2 (food_times,k):
    ans = 0
    food_list=[]

    if sum(food_times) <= k:
        ans = -1
    
    else:
        
        for i in range(0,len(food_times)):
            food_list.append(i)

        cycle = sum(food_times)//len(food_times)+1

        for i in food_list*max(food_times):
            if food_times[i] >0:
                if k == 0:
                    ans = i +1
                    if ans > len(food_times):
                        ans = ans - len(food_times)
                    break
                food_times[i] = food_times[i] -1
                k=k-1
                
            
    return ans

#print(solution2([4,2,3,6,7,1,5,8], 16)) #3


print(solution2([4,2,5,6,3,1,5,8], 13))
#무난스 한바퀴 3 1 2 5 6 0 4 7 ,8

#2 0 1 4 5 0 4 7, 3

#2 0 1 4 5 0 3 6, 1

#1 0 1 4 5 0 3 6, 0
