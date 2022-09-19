from collections import deque
T = int(input())

#이동방법 8가지
dx=[1, 1, 2, 2, -1, -1, -2, -2]
dy=[-2, 2, -1, 1, -2, 2, -1, 1]


def bfs(queue, graph):
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx>-1 and nx<i and ny>-1 and ny<i and graph[nx][ny] == 0:#아직 방문 안한곳
                graph[nx][ny] = graph[x][y] + 1#한번 턴 지난거 표시
                #print(graph[nx][ny], nx, ny)
                queue.append((nx,ny))

    
knight=deque()

for i in range(T):
    i = int(input())
    chess = [[0]*i for k in range (i)]
    #print(chess)
    
    #처음 좌표
    src = list(map(int, input().split()))
    chess[src[0]][ src[1]] = 1
    knight.append((src[0], src[1]))
    
    #가고싶은 좌표
    dest = list(map(int, input().split()))
    bfs(knight, chess)
    #구하고싶은 위치의 값을 출력하면됨,
    #print(chess)
    print(chess[dest[0]][dest[1]]-1)




