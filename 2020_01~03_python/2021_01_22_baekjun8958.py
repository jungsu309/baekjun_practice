N = int(input())

for i in range(0,N):
    Quiz=input()
    Quiz_list=[]
    stack=0
    sum = 0
    for i in Quiz:
        Quiz_list.append(i)
        if i=='O':
            stack = stack+1
            sum = sum+stack
        else:
            stack=0
            sum = sum+stack

    print(sum)


    
