# [single] [container]
# Integer  List
# Float    Tuple
# String   Dictionary
# Boolean  Set

# <Integer>: 정수 자료형
# 수의 크기 제한 딱히 없음 => overflow 걱정 줄일 수 있음
print(2**10000)
# str()로 쉬운 형변환
print(str(123))
# 연산/함수 사용 시, float로 변환되는 경우를 잘 살펴보자
## 나눗셈은 /가 아닌 //로 안전하게 나누자(또는 divmod 사용)
print(3 / 3) # 1.0
print(type(3 / 3)) # float
print(type(3 // 3)) # int
print(divmod(7, 3)) # (2, 1): 몫과 나머지

# <Float>: 실수 자료형
# 일단 연산에서는 쓰지말자!
## Decimal을 사용하거나 실수 오차를 해결할 자신이 있는 사람만
print(0.1 * 3 == 0.3) # False
# 유리수 연산은?
## 될 수 있다면 tuple 등으로 분자/분모를 따로 처리하자
print(1 / 3) # 0.3333333333333333
tuple = (1, 3), (2, 3)
print(tuple) # ((1, 3), (2, 3)): 후에 대소비교에 가능하기 때문

# <String>: 문자열 자료형
# Immutable 변수
## List로 변환하여 사용하기
a = "an subin"
for i in len(a):
    a[i] = "1"
print(a) # 에러 발생
# + 연산과 * 연산 조심하기
## join() method 활용하기
s = ""
for i in range(10000):
    s = s + str(i) # time: 5.96 마이크로 초
s = s.join([str(i) for i in range(10000)]) # time: 5.01 마이크로 초
# .split(), replace() 등 다양한 method 활용이 초점
# Slicing을 자유롭게 할 수 있는 것
s = 'abcd'
print(s[:1]) # 'a'
# Char를 ord와 chr로 다루기
print(chr(65)) # 'A'
print(ord('A')) # 65

# <Boolean>: 부울 자료형
# 논리 연산과 활용
if 0 and 1//0: # 런타임 에러. divided by zero
    print('hello') # False and 런타임 에러: 앞의 항이 거짓이면 뒤를 무시
if 1 or 1//0:
    print('hello') # True or 런타임 에러: 앞의 항이 참이면 뒤를 무시

# <List>: 리스트 자료형
# List Comprehension 사용하기
list_arr = [i for i in range(100)] # append보다 빠른 경우가 많음
# sort와 sorted 구분하기
list = [3, 5, 6, 9, 2]
print(sorted(list)) # [2, 3, 5, 6, 9]
print(list) # [3, 5, 6, 9, 2]
list.sort()
print(list) # [2, 3, 5, 6, 9]
# len, sum, max, min 등 활용하기
s = 'abs'
len(s) # 3
len(list) # 5
sum(list) # 25
max(list) # 9
min(list) # 2
# Slicing, [-1] 등 음수 인덱스 활용
print(list) # [2, 3, 5, 6, 9]
list = [1] + list
print(list) # [1, 2, 3, 5, 6, 9]
list[:0] = [1]
print(list) # [1, 1, 2, 3, 5, 6, 9]
print(list[-1]) # 9
# reduce, filter도 활용하면 좋음

# <Tuple>: 튜플 자료형
# 초기 상태 표현시 코드가 길어지는 것 방지
## ex) a, b, c = 0, 0, 0
a, b, c = 1, 2, 3
print(a) # 1
print(b) # 2
print(c) # 3
# Map과 함께 사용하여 입력 받기
a, b = map(int, input().split()) # 3 7
print(a, b) # 3 7
print(a) # 3
print(b) # 7
# 동시에 변해야하는 객체에 효율적 표현 가능
a, b = 3, 7
print(a) # 3
print(b) # 7
a = b
b = a
print(a, b) # 7 7
# ------------------
tmp = a
a = b
b = tmp
# ------------------
a, b = 3, 7
a, b = b, a
print(a, b) # 7 3