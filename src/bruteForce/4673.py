# 셀프넘버
# 셀프넘버가 아닌 수를  모두 구한 후 그걸 제외한 후 출력하자
# 셀프넘버가 아닌 수를 담을 자료구조로 뭘 선택해야 할까?
# list tuple set
# list: 순서가 존재, indexing존재, 생성 후 인덱스를 지정하여 값 변경 가능
# tuple: 순서가 존재,생성된 후 변경 불가
# set: 순서X, 중복불가
# 중복을 허용하지 않는 set의 특징때문에 자료형이 중복을 제거하기 위한 필터 역할로 종종 사용된다.
all = set(range(1, 10001))
no_self = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    no_self.add(i)

all = all - no_self

for k in sorted(all):
    print(k)