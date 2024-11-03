import heapq

def add_edge(adjacency_list, u, v, wt):
    adjacency_list[u].append((v, wt))
    adjacency_list[v].append((u, wt))

def dijkstra(adjacency_list, N, source):
    priority_queue = []
    distances = [float('inf')] * N
    heapq.heappush(priority_queue, (0, source))
    distances[source] = 0

    while priority_queue:
        _, u = heapq.heappop(priority_queue)

        for v, weight in adjacency_list[u]:
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
                heapq.heappush(priority_queue, (distances[v], v))

    print("Vertex   Distance from the source")
    for i in range(N):
        i_chr = chr(i+65)
        print(f"{i_chr:<9}{distances[i]}")

graph = {
    'A': {'B': 5,  'C': 10},
    'B': {'A': 5,  'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3,  'C': 2, 'E': 4},
    'E': {'D': 4}
}
N = len(graph)
adjacency_list = [[] for _ in range(N)]

for v in graph.keys():
    v_ord = ord(v)-65
    for u in graph[v].keys():
        u_ord = ord(u)-65
        add_edge(adjacency_list, v_ord, u_ord, graph[v][u])

dijkstra(adjacency_list, N, 0)
