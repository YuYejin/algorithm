# 영어 문제 해석:
# 세 개의 병, 각각 차 있는 용량
# 다음 병이 꽉 차거나 현재 용량이 없을 때 까지 다음 병에 부어 주는 과정을 100번 수행

C, M = [0, 0, 0], [0, 0, 0]

for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx = i % 3  # 0, 1, 2, 0, 1, 2, ...
    nxt = (i+1) % 3  # 1, 2, 0, 1, 2, 0, ...

    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]), 0), min(C[nxt], M[nxt] + M[idx])

for i in M:
    print(i)