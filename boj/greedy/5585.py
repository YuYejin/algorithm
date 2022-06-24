# 거스름돈의 최소 개수를 계산해야 함
# 가장 기초적인 탐욕 알고리즘 문제 유형
# 단순히 '큰 화폐 단위' 순서대로 잔돈을 거슬러 주면 최적의 해 얻을 수 있음
changes = 1000 - int(input())
count = 0

for i in [500, 100, 50, 10, 5, 1]:
    count += changes // i
    changes %= i

print(count)