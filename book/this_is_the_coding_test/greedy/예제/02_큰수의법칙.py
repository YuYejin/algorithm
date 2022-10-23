# 입출력 예시 -------------------------------------
# 5 8 3
# 2 4 5 4 6
# 6+6+6+5+6+6+6+5=46

# 5 7 2
# 3 4 3 4 3
# 4+4+4+4+4+4+4=28

# 풀이 과정 -------------------------------------
# 2 -> 2, 3-> 3 M개수가 3까지는 M번
# 5 -> 4, 6-> 5, 7 -> 6 M개수가 7까지는 M-1번
# 8 -> 6, 9 -> 7, 11 -> 9 M개수가 11까지는 M-2번
# 12 -> 9, 13 -> 10, 14 -> 11, 15 -> 12 M개수가 15까지는 M-3개

# 8 나누기 4는 2 -> M - 2
# 13 나누기 4는 3 -> M - 3
# 15 나누기 4는 3 -> M - 3

# 내 풀이 -------------------------------------
N, M, K = list(map(int, input().split()))
Nlist = list(map(int, input().split()))

Nlist.sort()
first = Nlist[-1]
second = Nlist[-2]

count = M - M//4 # 가장 큰 수 횟수
print(first * count + second * (M-count))

# 답안 예시 -------------------------------------
# n, m, k = list(map(int, input().split()))
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[n-1]
# second = data[n-2]
#
# # 가장 큰 수가 더해지는 횟수 계산
# count = int(m/(k+1)) * k
# count += m % (k+1)
#
# result = 0
# result += (count) * first
# result += (m - count) * second
#
# print(result)