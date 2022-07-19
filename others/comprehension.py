# 파이썬의 comprehension 문법:
# 패턴이 있는 list, dictionary, set을 보다 간단하게 작성할 수 있도록 지원

# < list comprehension >
numbers = []
for n in range(1, 11):
    numbers.append(n)
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [x for x in range(1, 11)]
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ------------------------------------------------
even_numbers = []
for n in range(1, 11):
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers) # [2, 4, 6, 8, 10]

# comprehension에서 if 키워드는 for문 다음에 위치해야 함
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers) # [2, 4, 6, 8, 10]
# ------------------------------------------------
for x in ['쌈밥', '치킨', '피자']:
    for y in ['사과', '아이스크림', '커피']:
        print(x, y)

dinner = [(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과', '아이스크림', '커피']] # 다중 for문 지원
print(dinner) # [('쌈밥', '사과'), ('쌈밥', '아이스크림'), ('쌈밥', '커피'), ('치킨', '사과'), ('치킨', '아이스크림'), ('치킨', '커피'), ('피자', '사과'), ('피자', '아이스크림'), ('피자', '커피')]
# ------------------------------------------------
lst = [x for x in range(10) if x < 5 if x % 2 == 0] # if문 중복
print(lst) # [0, 2, 4]