import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, left = None, right = None):
        self.left = left
        self.right = right
        self.val = key
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def tree_from_heap(heap, idx = 0):
    if idx >= len(heap):
        return None
    elif idx > (len(heap) - 2) // 2:
        return Node(heap[idx])
    else:
        return Node(heap[idx], tree_from_heap(heap, 2*idx+1), tree_from_heap(heap, 2*idx+2))

def dfs_iterative(start_node):
    order = []
    stack = [start_node]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        order.append(node.id)
    return order

def draw_tree_dfs(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    order = dfs_iterative(root)

    colors = [('green', 1-(order.index(node[0]))/len(order)) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs_iterative(start_node):
    order = []
    queue = [start_node]
    while queue:
        order.append(queue[0].id)
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return order

def draw_tree_bfs(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    order = bfs_iterative(root)

    colors = [('blue', 1-(order.index(node[0]))/len(order)) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

heap = [12, 5, 6, 11, 13, 7, 14, 3, 8, 10, 12, 9]
heapq.heapify(heap)
root = tree_from_heap(heap)
draw_tree_dfs(root)
draw_tree_bfs(root)

