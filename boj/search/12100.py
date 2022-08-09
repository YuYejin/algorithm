from copy import deepcopy

N = int(input())
Board = [map(int, input().split()) for i in range(N)]


def convert(x):
    pass


def rotate90(Board, N):
    pass


def dfs(N, Board, count):
    ret = max([max(i) for i in Board])
    if count == 0:
        return ret
    for _ in range(4):
        X = [convert(x) in Board]
        if X != Board:
            ret = max(ret, dfs(N, X, count-1))
        Board = rotate90(Board, N)
    return ret


print(dfs(N, Board, 5))