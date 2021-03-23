N = int(input())

array = list(map(int, input().split()))

low = 0;
high = len(array)-1
res = -1


while low<=high :
    mid = (low + high)//2
    
    if (array[mid] == mid):
        res = mid
        break
    elif (array[mid] > mid):
        high = mid-1
    else:
        low = mid+1
print(res)

