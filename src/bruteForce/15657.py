# N과 M (8)
# N개의 서로 다른 자연수 중에서 M개를 고른 수열을 모두 구하는 문제
# 중복 가능, 비 내림차순 
# 이전 문제에서 비 내림차순이 추가  A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 비내림차순이라고 한다.


import sys

n, m = map(int, input().split())
ans = [0] * m
nums = list(map(int, input().split()))
nums.sort()

def go(index, start, n, m): # start가 추가됨
    if index == m:
        sys.stdout.write(" ".join(map(str, ans)) + "\n")
        return
    for i in range(start, n): 
        ans[index] = nums[i]
        go(index + 1, i, n, m)


go(0, 0, n , m)
