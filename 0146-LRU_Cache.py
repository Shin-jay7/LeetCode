from __future__ import annotations


# https://www.youtube.com/watch?v=7v_mUfpg46E&t=716s
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic: return -1

        n = self.dic[key]
        self._remove(n)
        self._add(n)

        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        else:
            if self.capacity:
                self.capacity -= 1
            else:
                n = self.head.next
                del self.dic[n.key]
                self._remove(n)

        node = Node(key, value)
        self.dic[key] = node
        self._add(node)

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.next, self.prev = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.prev[b] = b, a

    def delete(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.prev[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)

        return val

    def put(self, key, value):
        if key in self.cache: self.delete(key)
        self.append(key, value)


from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache: del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
