## 목차
+ 그래프 기본 탐색 알고리즘
  + 너비 우선 탐색(BFS)
  + 깊이 우선 탐색(DFS)

---

## 그래프 기본 탐색 알고리즘
### BFS와 DFS란?
+ 대표적인 그래프 탐색 알고리즘
  + 너비 우선 탐색(BFS): 정점들과 같은 레벨에 있는 노드들(형제 노드들)을 먼저 탐색하는 방식
  + 깊이 우선 탐색(DFS): 정점의 자식들을 먼저 탐색하는 방식
![image](https://user-images.githubusercontent.com/98029695/183276017-2a30aa2c-10f2-490b-8417-1b3433fc6751.png)

### 너비 우선 탐색(BFS)
+ 파이썬으로 그래프를 표현하는 방법
  + 파이썬에서 제공하는 딕셔너리와 리스트 자료구조를 활용!
```python
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
print(graph) # {'A':['B', 'C'], 'B':['A', 'D'], ...}
```
```python
# BFS 알고리즘 구현 - need_vist 큐와 visited 큐 생성
def bfs(graph, start_node):
  visited = list()
  need_visit = list()

  need_visit.append(start_node)

  while need_visit:
    node = need_visit.pop(0)
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])

  return visited

print(bfs(graph, 'A')) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
```

### 깊이 우선 탐색(DFS)
```python
graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']
```
```python
# DFS 알고리즘 구현 - need_visit 스택과 visited 큐 생성
def dfs(graph, start_node):
  visited, need_visit = list(), list()
  need_visit.append(start_node)

  while need_visit:
    node = need_visit.pop()
    if node not in visited:
      visited.append(node)
      need_visit.extend(graph[node])

  return visited

print(dfs(graph, 'A')) # ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']
```
