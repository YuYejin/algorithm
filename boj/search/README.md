## 목차
+ [1012번 - 유기농 배추](#1012번---유기농-배추)
+ [16768번 - Mooyo Mooyo](#16768번---mooyo-mooyo)

---

## 1012번 - 유기농 배추
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.

한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

![image](https://user-images.githubusercontent.com/98029695/183277425-3cd41ee5-e1b6-42b9-81de-6b7462b732c2.png)

---

### 입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.

### 출력
각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

### 예제 입력1
```python
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
```

### 예제 출력1
```python
5
1
```
</details>

---

+ **Flood Fill 알고리즘**의 대표적인 문제
+ Flood Fill 알고리즘이란?
  + 주어진 시작점으로부터 연결된 영역들을 찾는 알고리즘
  + 다차원 배열의 어떤 칸과 연결된 영역을 찾는 알고리즘
  + 보통 DFS 알고리즘을 이용하여 재귀 함수를 통해 구현하거나, BFS 알고리즘을 이용하여 Queue로 구현한다.

### (1) input을 넣는 과정
```python
T = int(input())
B = [] # 배추

def process():
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1

for _ in range(T):
    process()
```
+ BFS와 DFS를 사용할 때 상하좌우를 살펴봐야 하므로, 배열의 인덱스를 넘지 않도록 가상의 0을 채워준다.
+ 이때 0은 배추가 없으므로 BFS와 DFS 탐색 조건에 어긋나게 되어 알아서 제외된다.
+ 실수로 'B\[X+1]\[Y+1] = 1' 라고 입력하지 않도록 주의하자.

### (2) 체크 배열과 정답 변수
```python
T = int(input())
B, ck = [], []

def process():
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)
    

for _ in range(T):
    process()
```
+ Flood Fill의 핵심은 배열의 어떤 부분이 채워져 있는지 알 수 없기 때문에 전체 탐색을 진행하고, 탐색한 부분을 다시 탐색하지 않는 것이다.
+ 탐색한 부분은 탐색했다고 표시해주기 위해 ck를 만들어 주었다.
+ ck\[i]\[j]가 1로 채워져 있다면 즉, 이미 방문했다면 continue로 넘어가주고, 아닌 경우에만 dfs(i, j)로 그 지점에서 순회를 돌아준다.
+ 순회를 시작한다는 것은 아직 체크가 되지 않은 배열의 순회를 시작하겠다는 의미이다. 이 말은 새로운 그룹을 하나 찾았다는 의미가 된다.
+ 우리의 출력 정보 즉, 정답인 ans 변수를 이중 for문 상단과 하단에 작성해주고, for문이 끝났을 때 ans가 출력되게 한다.
+ 이제 dfs 함수를 작성하면 된다.

### (3) dfs 함수
```python
T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i] # 다음으로 순회를 돌 점
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M+2)] for _ in range(N+2)]
    ck = [[0 for i in range(M+2)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)
    

for _ in range(T):
    process()
```
+ 처음 지점에 'ck\[x]\[y] = 1'로 체크를 해주고, for문으로 네 방향을 확인한다.
+ 이때 다음에 갈 방향이 0이거나, 이미 갔던 곳이라면 가지 않는다.
+ global B, ck를 덧붙여 전역변수를 사용한다고 선언한다.

### (4) 런타임 에러 수정
```python
import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        dfs(xx, yy)

def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)]
    ck = [[0 for i in range(50+2)] for _ in range(50+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            dfs(i, j)
            ans += 1
    print(ans)

for _ in range(T):
    process()
```
+ (3)까지 작성 후 제출을 해보면 런타임 에러가 발생하는 것을 확인할 수 있다.
+ DFS를 사용할 때는 가끔 재귀함수 깊이가 너무 깊어질 경우 런타임 에러가 발생할 수 있는데, 재귀함수의 깊이를 제한하는 함수를 작성해주면 이 문제를 해결할 수 있다.
+ 'sys.setrecursionlimit(10000)'를 통해 재귀함수 깊이를 제한해주자.

## 16768번 - Mooyo Mooyo
<details>
<summary>문제 및 입출력 펼쳐보기</summary>

### 문제
With plenty of free time on their hands (or rather, hooves), the cows on Farmer John's farm often pass the time by playing video games. One of their favorites is based on a popular human video game called Puyo Puyo; the cow version is of course called Mooyo Mooyo.

The game of Mooyo Mooyo is played on a tall narrow grid N cells tall (1 ≤ N ≤ 100) and 10 cells wide. Here is an example with N = 6:
```python
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```
Each cell is either empty (indicated by a 0), or a haybale in one of nine different colors (indicated by characters 1..9). Gravity causes haybales to fall downward, so there is never a 0 cell below a haybale.

Two cells belong to the same connected region if they are directly adjacent either horizontally or vertically, and they have the same nonzero color. Any time a connected region exists with at least K cells, its haybales all disappear, turning into zeros. If multiple such connected regions exist at the same time, they all disappear simultaneously. Afterwards, gravity might cause haybales to fall downward to fill some of the resulting cells that became zeros. In the resulting configuration, there may again be connected regions of size at least K cells. If so, they also disappear (simultaneously, if there are multiple such regions), then gravity pulls the remaining cells downward, and the process repeats until no connected regions of size at least K exist.

Given the state of a Mooyo Mooyo board, please output a final picture of the board after these operations have occurred.

---

### 입력
The first line of input contains N and K (1 ≤ K ≤ 10N). The remaining N lines specify the initial state of the board.

### 출력
Please output N lines, describing a picture of the final board state.

### 예제 입력1
```python
6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223
```

### 예제 출력1
```python
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
```
</details>

---

+ 문제를 간략히 설명하자면 최대 100*100 크기의 map이 존재하고, 이 map에서 어떠한 특정 같은 수는 한 그룹이다. 이 그룹에 속한 수가 K개를 넘어가면 삭제되고 나머지가 아래로 내려온다. 이 과정을 반복했을 때 마지막에 남는 상태가 어떠한지 출력으로 나타내면 된다.
+ 이 문제는 **Flood Fill 알고리즘**을 기초지식으로 요구하고 있고, **Flood Fill 알고리즘으로 처리한 것을 이후에 어떻게 다시 처리할 것인지**도 이야기하고 있다. 마지막으로 **2차원 배열에서 배열 내부에 있는 요소들을 어떻게 잘 이동시킬 수 있는가**에 대한 것도 묻고 있다.
+ 따라서 BFS 혹은 DFS로 그룹의 개수를 찾고 이를 반환하는 함수, 그 그룹에 속한 수가 K개가 넘었을 때 그룹을 삭제하는 함수, 요소를 내려오게 하는 함수를 반복문으로 변화가 발생하지 않을 때까지 돌려주면 될 것이다.

### (1) input을 넣는 과정
```python
# import sys
# sys. setrecursionlimit(10000)

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)] # [['0', '0', ..., '0'], ['0', '0', ... '0'], ...]

while True:
    exist = True
    
    if exist: # 바뀌는 게 없을 때 반복문을 빠져 나온다.
        break

for i in M:
    print(''.join(i))
```
+ 바뀌는 것이 있을 때까지 반복하기 위해 while문을 작성한다.
+ 이제 우리가 해야할 것은 단 두 가지이다. dfs를 돌리고, dfs가 맞으면 다시 dfs를 돌려서없애는 것이다.

### (2) 체크 배열과 결과 변수
```python
# import sys
# sys. setrecursionlimit(10000)

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)

def dfs(x, y):
  pass
  
def dfs2(x, y):
  pass
  
def down():
  pass

while True:
    exist = False
    ck = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            if res >= K:
                dfs2(i, j) # 지우기
                exist = True
    if not exist:
        break
    down() # 내리기

for i in M:
    print(''.join(i))
```
+ 반복문 내부를 작성한 결과 dfs, dfs2, down 총 3개의 함수를 짜야한다는 것을 알 수 있다.

### (3) dfs, dfs2, down 함수
```python
# import sys
# sys. setrecursionlimit(10000)

def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]

N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


def dfs2(x, y, val):
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)


def down():
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N-len(tmp)):
            M[j][i] = '0'
        for j in range(N-len(tmp), N):
            M[j][i] = tmp[j - (N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ck[i][j]:
                continue
            res = dfs(i, j) # 개수 세기
            if res >= K:
                dfs2(i, j, M[i][j]) # 지우기
                exist = True
    if not exist:
        break
    down() # 내리기

for i in M:
    print(''.join(i))
```
