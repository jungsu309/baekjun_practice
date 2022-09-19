s = input()
w = input()

#print(s,w)


cnt =0
def bt(s):
    global cnt
    #시작하는지점 찾아야한다.
    start_point = s.find(w)#첫등장의 첫시점을 알려줌.
    

    if start_point == -1:#없는거임
        return

    else:
        #찾은부분 이후부터 다시 찾아야함
        s = s[start_point+ len(w):]
        #print(s)
        cnt = cnt+1
        bt(s)
    
bt(s)
print(cnt)
