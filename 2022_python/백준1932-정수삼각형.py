n = int(input())

triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))

#print(triangle)


for i in range(1,n):#0행에는 어차피 선택할게 1개밖에 없기 때문에
    #맨 앞, 맨 뒤 : 받을수 있는곳이 한군데밖에없음.
    triangle[i][0] = triangle[i-1][0] + triangle[i][0]
    triangle[i][i] = triangle[i-1][i-1] + triangle[i][i]
    if i > 1:#2행부터 선택을 할 수 있기 때문
        #print(i)
        #print(triangle[i])
        for k in range(1,i):
            triangle[i][k] = max(triangle[i-1][k-1], triangle[i-1][k]) + triangle[i][k]
            #print(triangle[i])

#print(triangle)
print(max(triangle[n-1]))    
