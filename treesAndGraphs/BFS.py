from collections import deque

def BFS(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            queue.extendleft(graph[vertex] - visited)
    return visited

def BFS_paths(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path
            queue.append((next, path + [next]))

if __name__ == '__main__':
    g = {
        'A': {'B', 'C', 'D'},
        'B': {'C', 'A', 'F'},
        'C': {'B', 'F', 'G'},
        'D': {'G', 'B'},
        'F': {'A'},
        'G': {'F'}
    }

    # print(BFS(g, 'A'))
    print(list(BFS_paths(g, 'A', 'C')))
