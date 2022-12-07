# 나의 풀이 ---------------------------------------------------------
def solution(arr):
    answer = []

    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            if answer[-1] != i:
                answer.append(i)

    return answer

# 다른 사람 풀이 ---------------------------------------------------------
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a