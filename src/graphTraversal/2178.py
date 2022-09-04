# 최단거리 구하는 문제를 DFS가 아닌 BFS로 풀어야하는 이유.
# BFS는 현재 노드에서 가장 가까운곳부터 찾기 때문에 가장 먼저 찾아지는것이 최단경로이다.
# BFS는 방문한 노드는 재 방문할 필요가 없기 때문에 훨씬 적은 시간으로 찾을 수 있다.
# BFS는 큐 자료구조 사용! 
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소 칸 수를 구하는 프로그램을 작성하시오.

import sys
from collections import deque

n, m = map(int, input().split())
graph = []
visited = [[0]* m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    graph.append(list(map(int, input()))) #붙어서 들어옴


def bfs(x, y):
    queue = deque([(x, y)]) # 큐에 넣음으로서 방문처리
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft() #현재 방문한 x,y를 꺼내서 이제 활용해보자. (인접한곳 방문)

        if x == n-1 and y == m - 1:
            return visited[n-1][m-1]

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if xx >=0 and xx < n and yy >= 0 and yy < m :
                if graph[xx][yy] == 1 and not visited[xx][yy]:
                    queue.append([xx, yy]) # 조건만족 -> 여기도 방문
                    visited[xx][yy] = visited[x][y] + 1


print(bfs(0, 0))


