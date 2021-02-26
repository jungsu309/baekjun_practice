N = input()
list_N = list(N)

half = (len(list_N))//2
print(half)

#앞부분
front = 0
for i in range(0, half):
    front = front + int(list_N[i])

back = 0
for j in range(half, len(list_N)):
    back = back + int(list_N[j])

if front == back :
    print("LUCKY")
else:
    print("READY")
