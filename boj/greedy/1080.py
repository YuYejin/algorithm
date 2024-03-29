N, M = map(int, input().split())
# A = [list(map(int, list(input()))) for _ in range(N)] # 0을 1로 바꿀 때 문자보다 숫자가 더 쉽기 때문
# B = [list(map(int, list(input()))) for _ in range(N)]

def input_str():
    return [list(map(int, list(input()))) for _ in range(N)]

A, B = input_str(), input_str()

def flip(x, y, A):
    for i in range(3):
        for j in range(3):
            A[x+i][y+j] ^= 1 # 0^1은 1, 1^1은 0임을 이용하며 flip함

ans = 0

for i in range(N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
            flip(i, j, A)
            ans += 1

# if A != B:
#     print(-1)
# else:
#     print(ans)
print(ans if A == B else -1)