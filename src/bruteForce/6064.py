# 카잉 달력
# M과 N보다 작거나 같은 두개의 자연수 X,Y를 가지고 각 년도를 
# <x:y>와 같은 형식으로 표현하였다.
# x < M이면 X' = x+1 아니면 1 
# x, y에 1을 뻈을때와 안뺐을때의 차이를 모르겠음 (반례는 찾음 10 12 2 12)
# 다시 풀어보기
t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    k = x
    while k < n * m:
        if k % n == y: 
            print(k+1)
            break
        k += m
    else:
        print(-1) 


 