from pprint import pprint

def hamilton(G, size, pt = 0, path = []):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
    # loop or dead end, None is implicitly returned

def graph_constructor(node_holes, n = 10):
    def get_edges(node):
        ## Top left corner
        if (node == 0):
            return [node + 1, node + n]
        ## Top right corner
        if (node == n - 1):
            return [node - 1, node + n]
        ## Bottom left corner
        if (node == n * (n - 1)):
            return [node - n, node + 1]
        ## Bottom right corner
        if (node == n**2 - 1):
            return [node - 1, node - n]

        ## Left column
        if (node % n == 0):
            return [node - n, node + 1, node + n]
        ## Top row
        if (node < n):
            return [node - 1, node + n, node + 1]
        ## Right column
        if (node % n == n - 1):
            return [node - n, node - 1, node + n]
        ## Bottom column
        if (n**2 - n <= node and node < n**2):
            return [node - 1, node - n, node + 1]

        return [node - 1, node - n, node + 1, node + n]

    graph = { i: get_edges(i) for i in range(n**2) }
 
    def remove_edges(node):
        left = node - 1
        top = node - n
        right = node + 1
        bottom = node + n
        direction_nodes = [left, top, right, bottom]

        for direction_node in direction_nodes:
            direction_edges = graph.get(direction_node, [])
            if node in direction_edges:
                graph[direction_node].remove(node)

        del graph[node]

    for node_hole in node_holes:
        hole_index = (node_hole[0] * n) + node_hole[1]
        remove_edges(hole_index)

    return graph

node_holes = [[0,5], [1,2], [1,7], [6,3]] 
graph = graph_constructor(node_holes)
pprint(graph)
# path = hamilton(graph, 100 - len(node_holes))
# pprint(path)
