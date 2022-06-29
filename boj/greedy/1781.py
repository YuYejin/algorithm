import heapq

n = int(input())
array = []
q = []

# 문제 정보 입력 받은 이후, 데드라인 기준으로 오름차순 정렬
for i in range(n):
    a, b = map(int, input().split(' '))
    array.append((a, b))
array.sort()

for i in array:
    a = i[0]
    # 데드라인 초과하는 경우 최소 원소 제거
    heapq.heappush(q, i[1])
    if a < len(q):
        heapq.heappop(q)

print(sum(q))