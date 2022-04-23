from __future__ import annotations
from collections import defaultdict


# https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None


class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0

    def __len__(self):
        return self._size

    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1

    def pop(self, node=None):
        if self._size == 0:
            return

        if not node:
            node = self._sentinel.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1

        return node


class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._node = dict()
        self._freq = defaultdict(DLinkedList)
        self._min_freq = 0

    def _update(self, node):
        freq = node.freq

        self._freq[freq].pop(node)
        if self._min_freq == freq and not self._freq[freq]:
            self._min_freq += 1

        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1

        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._min_freq].pop()
                del self._node[node.key]
                self._size -= 1

            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._min_freq = 1
            self._size += 1


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = self.max_capacity = capacity
        self.counter_to_key = defaultdict(dict)
        self.key_to_counter = defaultdict(int)
        self.min_use_count = 0

    def get(self, key: int) -> int:
        if not self.max_capacity or key not in self.key_to_counter:
            return -1
        return self._update_key_value_pair(key=key, value=None, get=True)

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_counter:
            self._update_key_value_pair(key, value)
        else:
            self._add_new_key_value_pair(key, value)

    def _update_key_value_pair(self, key, value, get=False):
        use_count = self.key_to_counter[key]
        self.key_to_counter[key] += 1
        if get:
            value = self.counter_to_key[use_count][key]
        del self.counter_to_key[use_count][key]
        self.counter_to_key[use_count+1][key] = value
        if self.min_use_count ==\
                use_count and not self.counter_to_key[use_count]:
            self.min_use_count += 1
        return value

    def _add_new_key_value_pair(self, key, value):
        if not self.max_capacity:
            return

        if not self.capacity:
            first_key_for_least_frequestly_used =\
                next(iter(self.counter_to_key[self.min_use_count].keys()))
            del self.counter_to_key[self.min_use_count][
                first_key_for_least_frequestly_used]
            del self.key_to_counter[first_key_for_least_frequestly_used]
            self.capacity = 1

        self.capacity -= 1
        self.key_to_counter[key] = 1
        self.counter_to_key[1][key] = value
        self.min_use_count = 1
