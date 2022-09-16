# N과 M (4)
# N개의 서로 다른 자연수 중 M개를 고른 수열을 모두 구하자

import sys

# 입력 
n, m = map(int, input().split())

list = list(map(int, input().split()))
check = [False] * 8
ans = [0] * m
list.sort()
# 로직
def go(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(n):
        if check[i]:
            continue
        ans[index] = list[i]
        check[i] = True
        go(index + 1, n, m)
        check[i] = False

go(0, n, m)