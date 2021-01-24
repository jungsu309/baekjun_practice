N = int(input())


for i in range (0, N):
    word_list =[]
    word = list(map(str, input().split()))
    for i in word[1]:
        word_list.append(i)
  
    for k in range (0, len(word_list)):
        print(word_list[k]*int(word[0]), end="")
        if k == len(word_list)-1:
            print()

  
