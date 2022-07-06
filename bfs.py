# Поиск в глубину

graph = {
    '0': {'1'},
    '1': {'2'},
    '2': {'3', '4'},
    '3': {'1', '0'},
    '4': {'2'}
}

def bfs(graph, start, visited = []): #  в функции необходимо сам граф, вершина в которой находимся, и список посещенных вершин
    visited.append(start)
    queue = []
    queue.append(start)
    while queue:
        s = queue.pop(0)
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited

print(bfs(graph, '2'))




