def cluster(graph, weights, level):

    visited = {} 
 
    def bfs(start, component_id):
        queue = [start]
        visited[start] = component_id
        head = 0
        while head < len(queue):
            node = queue[head]
            head += 1
            for neighbor in graph.neighbors(node):
                if neighbor not in visited and weights(node, neighbor) >= level:
                    visited[neighbor] = component_id
                    queue.append(neighbor)
 
    component_id = 0
    for node in graph.nodes():
        if node not in visited:
            bfs(node, component_id)
            component_id += 1
 
    components = {}
    for node, cid in visited.items():
        components.setdefault(cid, set()).add(node)
 
    return frozenset(frozenset(nodes) for nodes in components.values())
 
