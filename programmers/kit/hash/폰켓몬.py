# 나의 풀이 ---------------------------------------------------------
def solution(nums):
    n = len(nums) // 2 #뽑는개수
    lst = set(nums) #중복제거

    if len(lst) >= n:
        answer = n
    else:
        answer = len(lst)

    return answer

# 다른 사람 풀이 ---------------------------------------------------------
def solution(ls):
    return min(len(ls)/2, len(set(ls)))