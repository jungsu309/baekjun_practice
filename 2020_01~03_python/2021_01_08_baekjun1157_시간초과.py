word = []

strr = input()

#대문자화시키기
sentence = strr.upper()
word = list(sentence)

#정렬
word.sort()

count=[]

for i in range(0, len(word)):
    cnt=1#일단 한번은 무조건 나온거니까.
    count.append(cnt)
    if word[i] != "1":
        for n in range(i+1, len(word)):
            if word[i] == word[n]:
                cnt = cnt+1
                #값을 바꿔버림
                word[n]="1"
                count[i] = cnt

            else:
                continue
    else:
        count[i]="n"

num = word.count('1')

for i in range(0, num):
    word.remove('1')
    count.remove('n')


#최댓값찾기

MAX = 0
for i in count:
    if MAX > i:
        MAX = MAX
    else:
        MAX = i

#최댓값이 많으면 ?출력하게하기
mmax = count.count(MAX)

if mmax == 1:
    position = count.index(MAX)
    print(word[position])

else:
    print("?")
