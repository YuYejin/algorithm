# 입출력 예시 -----------------------------------
## 입력
# a1
## 출력
# 2

# 내 풀이 -----------------------------------
input = input() #a1
col, row = input[0], int(input[1]) #a, 1

col_type = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(len(col_type)):
    if col == col_type[i]: col = i+1

# 수평 방향으로 먼저 2만큼 움직일 경우
hdx, hdy = [2, -2], [1, -1]
# 수직 방향으로 먼저 2만큼 움직일 경우
pdx, pdy = [1, -1], [2, -2]

count = 0

for i in hdx:
    for j in hdy:
        temp_col = col + i
        temp_row = row + j

        if temp_col < 1 or temp_row < 1 or temp_col > 8 or temp_row > 8:
            continue

        count += 1

for i in pdx:
    for j in pdy:
        temp_col = col + i
        temp_row = row + j

        if temp_col < 1 or temp_row < 1 or temp_col > 8 or temp_row > 8:
            continue

        count += 1

print(count)

## 값은 제대로 출력되지만 중복되는 코드가 별로 보기 좋진 않은듯

# 답안 예시 -----------------------------------
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)