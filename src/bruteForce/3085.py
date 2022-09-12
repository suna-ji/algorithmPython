# N * N 크기에 사탕을 채워 넣는다.
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 그 다음 두 사탕을 서로 교환한다.
# 이제 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분을 먹는다.
# 이때, 먹을 수 있는 사탕의 최대 개수를 구해라


n = int(input())
graph = []
ans = 0
for _ in range(n):
    graph.append(list(input()))

def check(graph, start_row, end_row, start_col, end_col):
    n = len(graph)
    ans = 1
    for i in range(start_row, end_row+1): # 행검사
        cnt = 1
        for j in range(1, n): # 1부터 시작하니까 이전 사탕과 계속 비교
            if graph[i][j] == graph[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    for i in range(start_col, end_col+1):
        cnt = 1
        for j in range(1, n):
            if graph[j][i] == graph[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans





# 한점을 고른 후 인접한 곳 중 색상이 다른경우 찾아서 바꾸기
for i in range(n):
    for j in range(n): # 한점을 고르고
        if j + 1 < n: # 오른쪽
            graph[i][j], graph[i][j+1] =  graph[i][j+1], graph[i][j] # 교환
            temp = check(graph, i, i , j, j+1) # 모두 같은 색으로 채워진 사탕 길이 구하기
            if ans < temp:
                ans = temp
            graph[i][j], graph[i][j+1] =  graph[i][j+1], graph[i][j] # 원상복귀
        if i + 1 < n: # 아래
            graph[i][j], graph[i+1][j] =  graph[i+1][j], graph[i][j] # 교환
            temp = check(graph, i, i+1 , j, j) # 모두 같은 색으로 채워진 사탕 길이 구하기
            if ans < temp:
                ans = temp
            graph[i][j], graph[i+1][j] =  graph[i+1][j], graph[i][j] # 원상복귀
            

        
print(ans)