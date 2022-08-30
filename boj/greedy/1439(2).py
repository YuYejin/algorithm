# 0 1 : 0, 0 (최소 횟수, 바뀌는 구간 개수)
# 01 10 : 1, 1
# 101, 010 : 1, 2
# 1010 : 2, 3
# 10101 : 2, 4
# 101010 : 3, 5
# 즉, (바뀌는 구간 개수 + 1) // 2

S, tot = input(), 0
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        tot += 1
print((tot+1)//2)
