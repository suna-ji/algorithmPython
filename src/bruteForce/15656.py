# N과 M (7)
# N개의 서로 다른 자연수 중에서 M개를 고른 수열을 모두 구하는 문제 (중복가능)
# 수열을 사전순으로 증가하는 순서로 출력해야 한다.
import sys

n, m = map(int, input().split())
ans = [0] * m
nums = list(map(int, input().split()))
nums.sort()

def go(index, n, m):
    if index == m:
        sys.stdout.write(" ".join(map(str, ans)) + "\n")
        return
    for i in range(n):
        ans[index] = nums[i]
        go(index + 1, n, m)


go(0, n , m)