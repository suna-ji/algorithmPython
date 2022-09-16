# n과 m(6)
# 고른 수열은 오름차순이여야 한다.

# N과 M (4)
# N개의 서로 다른 자연수 중 M개를 고른 수열을 모두 구하자

import sys

# 입력 
n, m = map(int, input().split())

list = list(map(int, input().split()))
check = [False] * 8
ans = [0] * m
list.sort() # 사전식으로 증가하는 순서로 출력
# 로직
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(start, n):
        if check[i]:
            continue
        ans[index] = list[i]
        check[i] = True
        go(index + 1, i + 1, n, m)
        check[i] = False

go(0, 0, n, m)

