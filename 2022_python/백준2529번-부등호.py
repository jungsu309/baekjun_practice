K= int(input())
sign = list(map(str, input().split()))

#print(k,sign)

li = []

def check(k,s,l):
    flag = 0
    for i in range(k):
        if s[i] =='<' and l[i] < l[i+1]:
            flag = flag +1
        elif s[i] =='>' and l[i] >l[i+1]:
            flag = flag +1

    if flag == len(s):
        return True
    else:
        #print(flag)
        return False

#c = check(k,sign,[7,6,8])
#print(c)


#cnt = 0
def bt(size):
    global cnt
    if size > 1:#li에 한개만 있으면 등호 비교가 안되서 맞고 틀리고가 없음..
        #print("size, sign[0:size-1], li 차례대로 : ", size,sign[0:size-1],li )
        #print("전단계 까지의 answerlist", answerlist)
        if check(size-1,sign[0:size-1],li)==True:
            #계속 포문 돌기
            #print("부등호에 맞음!",li)
            if size ==(K+1):
                #cnt = cnt+1
                #print("정답중하나임",li)
                #answerlist.append(li)
                li_str = ''.join(map(str,li))
                answerlist.append(li_str)
                #print(answerlist)
                #이건 되는데 왜 위에건안되는거야.? 리스트라그런가..?
                #tq.append(cnt)
                #print(tq)
                
                #정답이기 때문에 포문쪽으로 갈 필요 없다(for문 안에있는 if문에서 어차피 걸리긴하지만.)
                return 
        else:
            #더이상 뒤를 돌 필요가 없음 아랫쪽 건너뛰기-pop해줘야함!
            return 
    #print(answerlist)
    for i in range (0,10):
        if (i not in li) and (len(li) <= K):
            li.append(i)
            #print(li)
            bt(len(li))
            li.pop()

#맨첨에는 비어있는 상태이니까.
answerlist=[]
#tq=[]
bt(0)
#print(answerlist)
#print(a)
#print(cnt)
#print(tq)

#보통 사전순이기때문에.. 제일 앞과 제일 끝만 출력하면 될듯.
print(answerlist[len(answerlist)-1])
print(answerlist[0])

            
        
