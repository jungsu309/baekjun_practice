N = int(input())

StudentList = []
for i in range (N):
    [name, K,E,M] = map(str, input().split())
    StudentList.append([name, int(K), int(E), int(M)])
#print(StudentList)

#국어 큰->작
for i in range(N-1,0,-1):
    for j in range(i):
        if StudentList[j][1] < StudentList[j+1][1]:
            StudentList[j], StudentList[j+1] = StudentList[j+1],StudentList[j]
        #영어 작->큰    
        elif StudentList[j][1] == StudentList[j+1][1]:
            if StudentList[j][2] > StudentList[j+1][2]:
                StudentList[j], StudentList[j+1] = StudentList[j+1],StudentList[j]
            #수학 큰->작
            elif StudentList[j][2] == StudentList[j+1][2]:
                if StudentList[j][3] < StudentList[j+1][3]:
                    StudentList[j], StudentList[j+1] = StudentList[j+1],StudentList[j]
                #이름 작->큰
                elif StudentList[j][3] == StudentList[j+1][3]:
                    if StudentList[j][0] > StudentList[j+1][0]:
                        StudentList[j], StudentList[j+1] = StudentList[j+1],StudentList[j]
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
        
for i in range(N):
    print(StudentList[i][0])


#정렬 구글링 참고

N = int(input())

StudentList = []
for i in range (N):
    [name, K,E,M] = map(str, input().split())
    StudentList.append([name, int(K), int(E), int(M)])

SortedList = sorted(StudentList, key=lambda s:(-s[1], s[2], -s[3], s[0]))
        
for i in range(N):
    print(SortedList[i][0])
