# 리모컨 
# 리모컨에는 0~9까지의 숫자와 + -가 있다.

n = int(input())
m = int(input())
broken = [False] * 10

if m > 0:
    a = list(map(int, input().split()))
else:
    a = []

for x in a:
    broken[x] = True

def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c % 10]:
            return 0
        l += 1
        c //= 10
    return l

ans = abs(n-100)

for i in range(0,1000000+1):
    c = i
    l = possible(c)
    if l > 0: # 고장난 버튼이 없어서 누름
        plusminusCnt = abs(c-n)
        if ans > l + plusminusCnt:
            ans = l + plusminusCnt

print(ans)

