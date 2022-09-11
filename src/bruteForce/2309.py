# 일곱 난쟁이
# 일곱 난쟁이 키의 합이 100이다
# 9개의 줄에 걸쳐 난쟁이의 키가 주어진다.
# 일곱 난쟁이의 키를 오름차순으로 출력한다.
# 2명의 키는 전체 키의 합 - 100이라는걸 이용해서 문제를 풀면된다.
from re import I


height = []
sum = 0
for i in range(9):
    height.append(int(input()))
    sum += height[i]

res = []

def sol(height):
    for i in range(8):
        for j in range(i+1, 9):
            if (height[i] + height[j] == (sum - 100)):
                res.append(height[i])
                res.append(height[j])
                return

sol(height)

for i in res:
    height.remove(i)

for k in sorted(height):
    print(k)





