# Given a directed graph, design an algorithm to  nd out whether there is a route be- tween two nodes

def DFS(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def recursiveDFS(graph, start, visited=None):
    if visited == None:
        visited = set()

    visited.add(start)

    for vertex in graph[start] - visited:
        recursiveDFS(graph, vertex, visited)

    return visited

def DFSPaths_rec(graph, start, goal, path=None):
    if path is None:
        path = []

    if start == goal:
        yield path

    for next in graph[start] - set(path):
        yield from DFSPaths_rec(graph, next, goal, path + [start])

def DFSPaths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path
            stack.append((next, path + [next]))

if __name__ == '__main__':
    g = {
        'A': {'B', 'C', 'D'},
        'B': {'C', 'A', 'F'},
        'C': {'B', 'F', 'G'},
        'D': {'G', 'B'},
        'F': {'A'},
        'G': {'F'}
    }

    print(DFS(g, 'A'))
    print(recursiveDFS(g, 'A'))
    print(list(DFSPaths_rec(g, 'A', 'C')))
    print(list(DFSPaths(g, 'A', 'C')))
