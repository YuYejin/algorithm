def check(N, C):
    for i in range(N): # 인원 수만큼 사탕 개수 입력
        if C[i] % 2 == 1: # 사탕 개수가 홀수 개
            C[i] += 1 # 사탕 보충
    return len(set(C)) == 1 # set(): 리스트 중복 삭제 -> len(set(C)) == 1 모든 수가 같음


def teacher(N, C):
    tmp_lst = [0 for i in range(N)]
    for idx in range(N):
        if C[idx] % 2: # 사탕 개수가 홀수 개
            C[idx] += 1
        C[idx] //= 2
        tmp_lst[(idx+1) % N] = C[idx] # 오른쪽에 줄 값

    for idx in range(N):
        C[idx] += tmp_lst[idx]

    return C



for i in range(int(input())): # 테스트 케이스 수
    N, C = int(input()), list(map(int, input().split())) # 인원, 사탕 개수 리스트
    cnt = 0 # 순환 카운트
    while not check(N, C): # 모든 수가 같은지 체크하는 함수
        cnt += 1
        C = teacher(N, C) # 선생님의 역할 나타내는 함수
    print(cnt)
