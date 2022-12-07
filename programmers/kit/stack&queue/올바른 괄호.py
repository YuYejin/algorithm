# 나의 풀이 ---------------------------------------------------------
def solution(s):
    answer = True
    lst = []

    for i in s:
        if i == '(':
            lst.append(i)
        else:
            if lst == []:
                answer = False
                break
            else:
                lst.pop()

    if lst != []:
        answer = False

    return answer

# 다른 사람 풀이 ---------------------------------------------------------
def is_pair(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x  # 삼항연산자 두 번 사용 - w가 (이면 x가 1증가, w가 )이면 1감소, 그것도 아니라면 x
    return x==0