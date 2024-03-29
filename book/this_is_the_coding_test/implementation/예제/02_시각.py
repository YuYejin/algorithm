# 입출력 예시 --------------------------------------
## 입력
# 5
## 출력
# 11475

# 풀이 과정 --------------------------------------
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되는 모든 경우의 수를 구하는 문제이다.
# N이 1이면, 1시 59분 59초 (0 <= N <= 23)
#
# 초 단위: 03초 / 13초 / 23초 / 30초 ~ 39초 / 43초 / 53초
# 분 단위: 03분 / 13분 / 23분 / 30분 ~ 39분 / 43분 / 53분
# 시 단위: 3시 / 13시 ...
#
# 59초 -> 15번
# 1분 59초 -> 15 + 15번
# 2분 59초 -> 15 + 15 + 15번
# 3분 59초 -> 15 + 15 + 15 + 60번
# 4분 59초 -> 15 + 15 + 15 + 60 + 15번
# 5분 59초 -> 15 + 15 + 15 + 60 + 15 + 15번
# 59분 59초 -> 15번은 60번, (60-15)번은 15번
# 1시 59분 59초 -> 59분 59초의 두 배
# 2시 59분 59초 -> 59분 59초의 세 배
# 3시 59분 59초
# -> N이 0~2이면 (N+1)*(15*60+(60-15)*15))
# -> N이 3~12이면 N*(15*60+(60-15)*15))+3600
# -> N이 13~22이면 (N-1)*(15*60+(60-15)*15))+3600*2
# -> N이 23이면 (N-2)*(15*60+(60-15)*15))+3600*3
# 만약 3시면 3600번

# 내 풀이 --------------------------------------
N = int(input())

import time
start_time = time.time() # 측정 시작

if N <= 2:
    print((N + 1) * (15 * 60 + (60 - 15) * 15))
elif N <= 12:
    print(N*(15*60+(60-15)*15)+3600)
elif N <= 22:
    print((N-1)*(15*60+(60-15)*15)+3600*2)
else:
    print((N-2)*(15*60+(60-15)*15)+3600*3)

end_time = time.time()  # 측정 종료
print("time :", end_time - start_time)  # 수행 시간 출력

## 출력값은 제대로 나오지만 풀이 과정을 계산하는 게 너무 오래 걸림...

# 답안 예시 --------------------------------------
h = int(input())

import time
start_time = time.time() # 측정 시작

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

end_time = time.time()  # 측정 종료
print("time :", end_time - start_time)  # 수행 시간 출력

print(count)