from collections import deque


def assign_good_and_evil(graph):
    labels = {}

    for start in graph.nodes:
        if start in labels:
            continue
        # BFS to label this connected component
        labels[start] = 'good'
        queue = deque([start])

        while queue:
            node = queue.popleft()
            for neighbor in graph.neighbors(node):
                if neighbor not in labels:
                    # Assign opposite label
                    labels[neighbor] = 'evil' if labels[node] == 'good' else 'good'
                    queue.append(neighbor)
                elif labels[neighbor] == labels[node]:
                    # Same label on both ends of an edge → not bipartite
                    return None

    return labels

