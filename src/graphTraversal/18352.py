# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다.
# 이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시중에서,
# 최단거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# *모든 도로의 거리가 1 -> BFS
# BFS사용하여 특정 도시 X에서 시작해서 모든 도시까지의 최단거리를 구하자

from collections import deque
import sys

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)