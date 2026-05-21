def biggest_descendent(graph, root, value):
    biggest = {}
 
    def dfs(node):
        # Start with the node's own value
        best = value[node]
        for neighbor in graph.neighbors(node):
            dfs(neighbor)
            if biggest[neighbor] > best:
                best = biggest[neighbor]
        biggest[node] = best
 
    dfs(root)
    return biggest
 
