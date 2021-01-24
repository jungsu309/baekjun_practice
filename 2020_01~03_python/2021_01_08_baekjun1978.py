Case = int(input())
num_list = list(map(int, input().split(' ')))

res_counting = 0

for i in num_list:
    cnt = 0
    if(i == 1):
        continue
    for j in range(2, i + 1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        res_counting += 1
print(res_counting)
