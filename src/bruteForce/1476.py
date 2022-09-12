# 날짜계산
e, s, m = map(int, input().split())
year = 0
while True:
    year+=1
    if ((year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0):
        print(year)
        break