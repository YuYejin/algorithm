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

print(bfs(graph, 'A')) # bfs 방식으로 탐색됨

# 일반적인 BFS 시간 복잡도
# 노드 수 : V
# 간선 수 : E
# 시간 복잡도 : O(V + E)