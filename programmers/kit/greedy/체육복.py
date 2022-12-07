# 나의 풀이 ---------------------------------------------------------
## 테스트케이스 전부 통과하지 못함 (84/100)
def solution(n, lost, reserve):
    answer = 0
    count = 0
    lost.sort()
    reserve.sort()

    for i in lost:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            print(lost, reserve)

    for i in lost:
        if i - 1 in reserve:
            count += 1
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            count += 1
            reserve.remove(i + 1)

    answer = n - len(lost) + count
    return answer

# 다른 사람 풀이 ---------------------------------------------------------
def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n - len(set_lost)