N = input()

number=[]
if len(N) == 1 :
    number.append(0)
    number.append(int(N))
else:
    for i in str(N):
        number.append(int(i))


i=0

while True:
 
    culculate = number[i] + number[i+1]
    #맨 뒷자리 숫자
    last = culculate % 10
    number.append(last)
    i=i+1

    result = number[i]*10 + number[i+1]
    if str(result) == str(N):
        print(i)
        break
    

