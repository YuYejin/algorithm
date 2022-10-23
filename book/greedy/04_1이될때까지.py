# 입출력 예시 -------------------------
## 입력
# 25 5
## 출력
# 2

## 입력
# 17 4
## 출력
# 3

# 풀이 과정 -------------------------
# N % K == 0 이면 나누고 count += 1
# N % K != 0 이면 1빼고 count += 1

import time

# 내 풀이 -------------------------
N, K = map(int, input().split())
count = 0

start_time = time.time() # 측정 시작

while N != 1:
    if N % K == 0:
        N //= K
        count += 1
    else:
        N -= 1
        count += 1

end_time = time.time()  # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력

print(count)

# 답안 예시 -------------------------
## 단순하게 푸는 답안 예시
# n, k = map(int, input().split())
# result = 0
#
# start_time = time.time() # 측정 시작
#
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result +=1
#
# while n > 1:
#     n -= 1
#     result += 1
#
# end_time = time.time()  # 측정 종료
# print("time :", end_time - start_time) # 수행 시간 출력
#
# print(result)

## 답안 예시
# n, k = map(int, input().split())
# result = 0
#
# while True:
#     target = (n // k) * k
#     result += (n - target)
#     n = target
#
#     if n < k:
#         break
#     result += 1
#     n //= k
#
# result += (n - 1)
# print(result)