T = int(input())

list_a = []
list_b = []
list_sum = []
for i in range(1,T+1):
    a,b = map(int, input().split())
    sum = a+b

    list_a.append(a)
    list_b.append(b)
    list_sum.append(sum)


for n in range (0,T):
    print("Case #" + str(n+1) + ": "+ str(list_a[n]) + " + " + str(list_b[n]) + " = " + str(list_sum[n]))

