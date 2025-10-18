#!/usr/bin/env python3
"""
dsa_library.py

A complete Python code file that demonstrates major DSA concepts:
- Basic data structures (Stack, Queue, LinkedList)
- Trees (Binary Search Tree, Traversals)
- Graphs (Adjacency List, BFS, DFS, Dijkstra)
- Sorting algorithms (Quick, Merge, Bubble)
- Searching algorithms (Linear, Binary)
- Dynamic Programming examples (Fibonacci, Knapsack)

Run:
    python dsa_library.py
"""

from __future__ import annotations
import heapq
from collections import deque
import math
import random

# -------------------------------------------------------------------
# 1️⃣ BASIC DATA STRUCTURES
# -------------------------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return f"Stack({self.items})"


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return f"Queue({list(self.items)})"


class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(cur.data)
            cur = cur.next
        return vals

# -------------------------------------------------------------------
# 2️⃣ TREE (Binary Search Tree)
# -------------------------------------------------------------------

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

class BST:
    def __init__(self):
        self.root: TreeNode | None = None

    def insert(self, key):
        def _insert(root, key):
            if not root:
                return TreeNode(key)
            if key < root.key:
                root.left = _insert(root.left, key)
            elif key > root.key:
                root.right = _insert(root.right, key)
            return root
        self.root = _insert(self.root, key)

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.key] + _inorder(node.right) if node else []
        return _inorder(self.root)

    def search(self, key):
        cur = self.root
        while cur:
            if cur.key == key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

# -------------------------------------------------------------------
# 3️⃣ GRAPH (Adjacency List + BFS/DFS + Dijkstra)
# -------------------------------------------------------------------

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, w=1):
        self.adj.setdefault(u, []).append((v, w))
        self.adj.setdefault(v, []).append((u, w))  # undirected

    def bfs(self, start):
        visited = set([start])
        q = deque([start])
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nbr, _ in self.adj.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)
                    q.append(nbr)
        return order

    def dfs(self, start):
        visited = set()
        order = []
        def _dfs(u):
            visited.add(u)
            order.append(u)
            for v, _ in self.adj.get(u, []):
                if v not in visited:
                    _dfs(v)
        _dfs(start)
        return order

    def dijkstra(self, start):
        dist = {node: math.inf for node in self.adj}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in self.adj[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        return dist

# -------------------------------------------------------------------
# 4️⃣ SORTING ALGORITHMS
# -------------------------------------------------------------------

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# -------------------------------------------------------------------
# 5️⃣ SEARCHING ALGORITHMS
# -------------------------------------------------------------------

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# -------------------------------------------------------------------
# 6️⃣ DYNAMIC PROGRAMMING
# -------------------------------------------------------------------

def fibonacci(n, memo=None):
    memo = memo or {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacity]

# -------------------------------------------------------------------
# 7️⃣ DEMONSTRATION
# -------------------------------------------------------------------

def demo():
    print("\n=== STACK & QUEUE ===")
    s = Stack()
    for i in range(5):
        s.push(i)
    print("Stack:", s)
    print("Pop:", s.pop())

    q = Queue()
    for c in "ABCDE":
        q.enqueue(c)
    print("Queue:", q)
    print("Dequeue:", q.dequeue())

    print("\n=== LINKED LIST ===")
    ll = LinkedList()
    for v in [10, 20, 30]:
        ll.append(v)
    print("LinkedList:", ll.display())

    print("\n=== BINARY SEARCH TREE ===")
    bst = BST()
    for num in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(num)
    print("BST Inorder:", bst.inorder())
    print("Search 7:", bst.search(7))

    print("\n=== GRAPH ===")
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    print("BFS:", g.bfs("A"))
    print("DFS:", g.dfs("A"))
    print("Dijkstra from A:", g.dijkstra("A"))

    print("\n=== SORTING ===")
    arr = [random.randint(1, 50) for _ in range(10)]
    print("Original:", arr)
    print("Bubble:", bubble_sort(arr.copy()))
    print("Quick:", quick_sort(arr.copy()))
    print("Merge:", merge_sort(arr.copy()))

    print("\n=== SEARCHING ===")
    arr2 = sorted(arr)
    print("Sorted array:", arr2)
    print("Linear search for", arr2[3], ":", linear_search(arr2, arr2[3]))
    print("Binary search for", arr2[3], ":", binary_search(arr2, arr2[3]))

    print("\n=== DYNAMIC PROGRAMMING ===")
    print("Fibonacci(10):", fibonacci(10))
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    cap = 5
    print("Knapsack:", knapsack(w, v, cap))


if __name__ == "__main__":
    demo()
