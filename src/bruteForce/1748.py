# 수 이어쓰기 1
n = int(input())
ans = 0
start = 1
length = 1
while start <= n:
    end = start * 10 -1
    if end > n:
        end = n
    ans += (end - start + 1) * length
    length += 1
    start  *= 10
print(ans)