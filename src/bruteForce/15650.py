# N과 M (2)
# 1~N 까지 자연수 중 중복없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다. -> 순서가 중요

import sys
n, m = map(int, input().split())
pick = [False] * 10
ans = [0] * m
def select(index, start, n , m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(start, n + 1):
        if pick[i]:
            continue
        ans[index] = i 
        pick[i] = True
        start = i
        select(index + 1, start, n , m)
        pick[i] = False

select(0, 1, n, m)