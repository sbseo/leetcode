from collections import defaultdict
from collections import deque

def topological_sort(vertices, edges):
    sortedOrder, queue = [], deque()
    adj_list, adj_degree = defaultdict(list), defaultdict(int)

    for v1, v2 in edges: 
        if not adj_degree[v1]: adj_degree[v1] = 0
        adj_list[v1].append(v2)
        adj_degree[v2] += 1 
    
    # repeat 1-2
    count = 0
    while count < vertices:
        # 1. find vertex where indegree = 0
        for v, indegree in adj_degree.items():
            if indegree == 0:
                queue.append(v)
        
        # 2. remove indgree
        while queue: 
            source = queue.popleft()
            adj_degree.pop(source)
            sortedOrder.append(source)
            for child in adj_list[source]:
                adj_degree[child] -= 1
        count += 1

    return sortedOrder

def main():
    print("Topological sort: " +
            str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
            str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
            str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()
