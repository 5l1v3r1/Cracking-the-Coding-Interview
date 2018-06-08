# Given a directed graph, design an algorithm to  nd out whether there is a route be- tween two nodes
from collections import deque

def bfs(graph, start, end):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in graph[vertex] - set(path):
            if next == end:
                return path
            queue.append((next, path+[next]))

if __name__ == '__main__':
    g = {
        'a': set(['b', 'c', 'd']),
        'b': set(['a']),
        'c': set(['f']),
        'd': set(['a', 'c']),
        'f': set([]),
        'g': set([])
    }

    print('YES' if bfs(g, 'a', 'g') else 'NO')
    print('YES' if bfs(g, 'a', 'f') else 'NO')
