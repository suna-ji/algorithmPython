# n과 m(3)
# 1~n 까지의 자연수 중 m개를 고른 수열
# 중복허용
# N과 M (1)
# 1부터 N까지 중복없이 M개를 고른 수열을 모두 구하자

import sys
n, m = map(int, input().split())

ans = [0] * m

def select(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans))+ '\n')
        return
    for i in range(1, n+1):
        ans[index] = i
        select(index+1, n, m)


select(0, n, m)
