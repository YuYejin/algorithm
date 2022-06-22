# 동적계획법(DP) : 상향식 접근법, Memoization 기법 사용
# 분할 정복 : 하향식 접근법, 일반적으로 재귀함수로 구현

# 동적계획법 알고리즘 이해
# 연습 - n을 입력받았을 때 피보나치 수열로 결과값을 출력하기

# recursive call 활용
def fibo(num):
  if num <= 1:
    return num
  return fibo(num - 1) + fibo(num - 2)

# 동적 계획법 활용
def fibo_dp(num):
  cache = [0 for index in range(num + 1)]
  cache[0] = 0
  cache[1] = 1

  for index in range(2, num + 1):
    cache[index] = cache[index + 1] + cache[index + 2]
  return cache[num]

# 연습 1 - 백준 11726번
# 1) 빈 리스트 만들기(입력값에 따른)
n = int(input())
dp = [0] * 1001

# 2) 초기값을 설정
dp[1] = 1
dp[2] = 2

# 3) 점화식 기반으로 계산값 적용
for index in range(3, 1001):
  dp[index] = dp[index - 1] + dp[index - 2]

# 4) 특정 입력값에 따른 계산값을 리스트에서 추출
print(dp[n] % 10007)

# 연습 2 - 백준 9461번
dp = [0] * 101
dp[1], dp[2], dp[3] = 1, 1, 1
for index in range(1, 98):
  dp[index + 3] = dp[index] + dp[index + 1]
print(dp[2])
print(dp[6])
print(dp[12])