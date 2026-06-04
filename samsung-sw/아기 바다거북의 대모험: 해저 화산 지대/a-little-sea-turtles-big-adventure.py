from collections import deque

N,M,K = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

turtles = {}
for i in range(M):
    x,y = map(int,input().split())
    board[x][y] = -1
    turtles[i] = (x,y)

volcanos = {}
for j in range(K):
    x,y,press = map(int,input().split())
    volcanos[(x,y)] = [press,0]

ans = [-1] * M

dir = [(0,1),(1,0),(0,-1),(-1,0)]

def find_road(x,y):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    next_que = deque()
    visited[x][y] = 0
    next_que.append((x,y))
    while next_que:
        now_x,now_y = next_que.popleft()
        if (now_x,now_y) == (N-1,N-1):
            return visited[now_x][now_y]

        for dir_x,dir_y in dir:
            next_x = now_x + dir_x
            next_y = now_y + dir_y
            if 0 <= next_x < N and 0 <= next_y < N:
                if visited[next_x][next_y]==-1 and board[next_x][next_y]==0:
                    next_que.append((next_x,next_y))
                    visited[next_x][next_y] = visited[now_x][now_y] + 1
    return -1
    

for turn in range(100):
    if not turtles:
        break

    for i in list(turtles.keys()):
        now_x,now_y = turtles[i]

        board[now_x][now_y] = 0

        min_dist = 10**9
        move_x,move_y=now_x,now_y

        for dir_x,dir_y in dir:
            next_x = now_x + dir_x
            next_y = now_y + dir_y
            if 0 <= next_x < N and 0 <= next_y < N and board[next_x][next_y] ==0:
                dist = find_road(next_x,next_y)

                if dist != -1 and dist < min_dist:
                    min_dist = dist
                    move_x,move_y = next_x,next_y

        if min_dist == 10**9:
            board[now_x][now_y] = -1
            continue
        
        turtles[i] = (move_x,move_y)

        if (move_x,move_y) == (N-1,N-1):
            ans[i] = turn + 1
            turtles.pop(i)
        else:
            board[move_x][move_y] = -1
        
    for volcano in volcanos:
        volcanos[volcano][1] += 10

    heat = [[0 for _ in range(N)] for _ in range(N)]
    exploded = set()

    changed = True
    while changed:
        changed = False

        for volcano in volcanos:
            if volcano in exploded:
                continue
            
            x,y = volcano
            press = volcanos[volcano][0]
            now_pressure = volcanos[volcano][1]

            if now_pressure + heat[x][y] >= press:
                exploded.add(volcano)
                changed = True

                heat[x][y] += press

                for dir_x,dir_y in dir:
                    value = press
                    next_x,next_y = x,y

                    while True:
                        value //= 2

                        if value == 0:
                            break

                        next_x += dir_x
                        next_y += dir_y

                        if not(0 <= next_x < N and 0 <=next_y < N):
                            break

                        if board[next_x][next_y] == 1:
                            break

                        heat[next_x][next_y] += value
        fossil_turtles = []

        for turtle in turtles:
            x,y = turtles[turtle]

            if heat[x][y] >= 20:
                board[x][y] = -2
                fossil_turtles.append(turtle)
        
        for turtle in fossil_turtles:
            turtles.pop(turtle)


        for volcano in exploded:
            volcanos[volcano][1] = 0
    
    
for i in ans:
    print(i)  