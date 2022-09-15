# N과 M (1)
# 1부터 N까지 중복없이 M개를 고른 수열을 모두 구하자
from cmath import pi
from operator import truediv
import sys
n, m = map(int, input().split())

pick = [False] * 10 # 뽑았는지 여부 (중복없이 뽑기 위함)
ans = [0] * m
def select(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans))+ '\n')
        return
    for i in range(1, n+1):
        if pick[i]:
            continue
        pick[i] = True
        ans[index] = i
        select(index+1, n, m)
        pick[i] = False


select(0, n, m)

   

## join 함수
# '구분자'.join(['a', 'b', 'c']) a구분자b구분자c