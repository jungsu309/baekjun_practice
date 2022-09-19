from sys import stdin
T = int(input())

testcase=[]
for t in range(T):
    testcase.append(int(stdin.readline()))
#print(testcase)
#print(max(testcase))
count_0=[0]*(41)
count_1=[0]*(41)

#0과 1일때 각각 초기화
count_0[0] = 1
count_1[0] = 0

count_0[1] = 0
count_1[1] = 1


for i in range(2, 41):
    count_0[i] = count_0[i-2] + count_0[i-1]
    count_1[i] = count_1[i-2] + count_1[i-1]

#print(count_0)
#print(count_1)

for test in testcase:
    print(count_0[test], count_1[test])
