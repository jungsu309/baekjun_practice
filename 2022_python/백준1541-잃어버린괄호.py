#연산자와 숫자를 구분해보기..

math = input()
math_list = list(str(math))
print(math_list)

#-를 만나면 바로 괄호를 연다. 그 뒤에 또 -를 만나면 괄호를 닫고
#그 뒤에 +가 나온다면 괄호를 닫지 않는다.
#첫 - 일때와 그 이상일때의 -처리가 다르다. ->cnt로 판별하는게?
cnt = 0
left = 0
right = 0
for i in range (0,len(math_list)):
    if (math_list[i] =='-')& (cnt==0):
        math_list.insert(i+1, "(")
        left = left +1
        cnt = cnt+1
    if (math_list[i] =='-')&(cnt>0):
        math_list.insert(i+1, "(")
        left = left+1
        math_list.insert(i-1, ")")
        right = right+1
if left != right:#-가 있는경우는 항상 끝에 닫지 않는다 그래서 개수가안맞음
    #맨뒤에를 닫아주자
    math_list.append(")")
print(math_list)
        
math_return = ''.join(math_list)
print(math_return)
print(type(math_return))

#괄호를 토대로 진짜로 계산해보기
#모르겠는데?

#다시 해보기-> 진짜 괄호 넣지말고 계산규칙을 생각해보자
#-가 나오기 전까진 다 더하면된다. 괄호를 친다는 거 자체가 연산자를 바꾸겠다는 의미와 유사하므로 - 이후의 값들은 전부 -해주자.
#90+10-20-20+30+40-50+900 이렇게 되도 - 이후부터는 +부분자체를 그냥 다 -로 바꿔버리면 된다는 이야기다. -(20+30+40)-(50+900)하면 결국 모든+가 -로 바뀌기 때문임.

math = input()
answer = 0
math_list = math.split('-')
#-기준으로 쪼개진다. 이때 맨 앞에만 진짜 더하기고 나머지는 더한담에 다 빼면된다.
#나머지가 다 +이므로 +기준으로 쪼개고 더하거나 빼면 된다!

plus = math_list[0]
minus = math_list[1:]

#앞부분 더하는부분
math_plus = plus.split('+')
#print(math_plus)
for i in math_plus:
    answer = answer + int(i)
#print(answer)

#print(minus)

for j in minus:
    #print(j)
    math_minus = j.split('+')
    for k in math_minus:
        answer = answer - int(k)
print(answer)
