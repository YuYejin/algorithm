# 입출력 예시 -------------------------------------
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2
#
# 2 4
# 7 3 1 8
# 3 3 3 4

# 내 풀이 -------------------------------------
N, M = list(map(int, input().split()))
min_list = list()
for i in range(N):
    min_list.append(min(list(map(int, input().split()))))
print(max(min_list))

# 입출력 예시 -------------------------------------
## min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

## 2중 반복문 구조를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 #'각 숫자는 10,000 이하의 자연수'라는 조건을 이용
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)


