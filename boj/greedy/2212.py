import sys

n = int(input())
k = int(input())

# 집중국 개수가 n 이상일 때
if k >= n:
    print(0) # 각 센서 위치에 설치하면 되므로 정답은 0
    sys.exit()

# 모든 센서 위치를 입력 받아 오름차순 정렬
array = list(map(int, input().split(' ')))
array.sort()

# 각 센서 간 거리 계산해 내림차순 정렬
distances = []
for i in range(1, n):
    distances.append(array[i] - array[i - 1])
distances.sort(reverse=True)

# 가장 긴 거리부터 하나씩 제거
for i in range(k - 1):
    distances[i] = 0
print(sum(distances))