# 예제 - 팩토리얼
def factorial(num):
  if num > 1:
    return num * factorial(num - 1)
  else:
    return num

for num in range(10):
  print(factorial(num))

# 연습 1 - 다음 함수를 재귀 함수를 활용해 완성하고 1부터 num까지 곱이 출력되게 만들기
def multiple(data):
  if data <= 1:
    return data
  return data * multiple(data - 1)

print(multiple(10))

# 연습 2 - 숫자가 들어있는 리스트가 주어졌을 때 리스트의 합을 리턴하는 함수 만들기
import random
data = random.sample(range(100), 10)
print(data)

def sum_list(data):
  if len(data) == 1:
    return data[0]
  return data[0] + sum_list(data[1:])

print(sum_list(data))

# 연습 3 - 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만들기
string = 'Dave'
print(string[-1]) # e
print(string[0]) # D
print(string[1:-1]) # av
print(string[:-1]) # 

def palindrome(string):
  if len(string) <= 1:
    return True

  if string[0] == string[-1]:
    return palindrome(string[1:-1])
  else:
    return False

# 연습 4
# 정수 n에 대해 n이 홀수면 3*n+1을 하고, n이 짝수면 n을 2로 나눈다.
# 이렇게 계속 진행해서 n이 결국 1이 될 때까지 과정을 반복한다.
# 정수 n을 입력받아 위 알고리즘에 의해 1이 되는 과정을 모두 출력하는 함수를 작성하기
def func(n):
  print(n)
  if n == 1:
    return n 

  if n % 2 == 1:
    return(func(3*n+1))
  else:
    return(func(int(n/2)))

print(func(3))

# 연습 5
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하기
# (1+1+2, 1+2+1, 2+1+1 은 모두 다름)
# (정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n)이라고 하면, f(n-1) + f(n-2) + f(n-3)과 동일하다는 패턴 찾기)
def func(data):
  if data == 1:
    return 1
  elif data == 2:
    return 2
  elif data == 3:
    return 4
  return func(data-1) + func(data-2) + func(data - 3)
print(func(5))