def is_planar(graph):
    #Test whether a given graph is planar or not using Kuratowski's and Wagner's theorem.
    #Returns True if the graph is planar, False otherwise.
    for subgraph in get_subgraphs(graph):
        if is_k5_subdivision(subgraph) or is_k33_subdivision(subgraph):
            return False
    return True

def get_subgraphs(graph):
    #Generate all subgraphs of the given graph.
    subgraphs = []
    n = len(graph)
    for i in range(1, 2**n):
        subgraph = []
        for j in range(n):
            if i & (1 << j):
                subgraph.append(graph[j])
        subgraphs.append(subgraph)
    return subgraphs

def is_k5_subdivision(graph):
    #Test whether the given graph is a subdivision of \(K_5\).
    edges = set()
    for u, v in graph:
        if (u, v) in edges or (v, u) in edges:
            return False
        edges.add((u, v))
        edges.add((v, u))
    n = len(edges)
    if n < 10:
        return False
    adj = [[] for _ in range(5)]
    count = 0
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        count += 1
        if count == n:
            break
    for i in range(5):
        if len(adj[i]) != 4:
            return False
    visited = [False] * 5
    visited[0] = True
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return all(visited)

def is_k33_subdivision(graph):
    #Test whether the given graph is a subdivision of \(K_{3,3}\).
    edges = set()
    for u, v in graph:
        if (u, v) in edges or (v, u) in edges:
            return False
        edges.add((u, v))
        edges.add((v, u))
    n = len(edges)
    if n < 6:
        return False
    adj = [[] for _ in range(6)]
    count = 0
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        count += 1
        if count == n:
            break
    for i in range(3):
        if len(adj[i]) != 3:
            return False
    for i in range(3, 6):
        if len(adj[i]) != 3:
            return False
    return True
