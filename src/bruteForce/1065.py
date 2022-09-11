# 한수
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# 1보다 크거나 같고 N보다 작거나 같은 한수의 개수를 출력

n = int(input())
cnt = 0
split_num = []
for i in range(1, n+1):
    if i < 100:
        cnt += 1
    else:
        split_num = list(map(int, str(i)))
        if split_num[1] - split_num[0] == split_num[2] - split_num[1]:
            cnt += 1

print(cnt)

# print (str(123))
# test = list('ㄱㄴㄷㄹ')
# for i in test:
#     print(i)
