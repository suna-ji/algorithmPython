# 단지번호 붙이기
# 단지수를 출력하고 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력
# !! 방문한 노드를 0으로 바꾸어서 다시 방문하지 않도록 해야함 !!
# !! 1이면 무조건 시작이 가능하기 때문에 bfs자체를 여러번 해야하고 graph를 인자로 넘겨야함

from collections import deque


# 입력
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 변수 정의
res = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 로직
def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >=n:
                continue
            if graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(bfs(graph, i, j))

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])


# 메모
# deque([1,2,3,4,5])
# deque.append((item))