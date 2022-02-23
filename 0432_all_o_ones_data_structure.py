from __future__ import annotations
from collections import defaultdict


class Node:
    def __init__(self):
        self.key_set = set([])
        self.prev, self.next = None, None

    def add_key(self, key):
        self.key_set.add(key)

    def remove_key(self, key):
        self.key_set.remove(key)

    def get_any_key(self):
        if self.key_set:
            result = self.key_set.pop()
            self.add_key(result)
            return result
        else:
            return None

    def count(self):
        return len(self.key_set)

    def is_empty(self):
        return len(self.key_set) == 0


class DoubleLinkedList():
    def __init__(self):
        self.head_node, self.tail_node = Node(), Node()
        self.head_node.next, self.tail_node.prev =\
            self.tail_node, self.head_node
        return

    def insert_after(self, x):
        node, temp = Node(), x.next
        x.next, node.prev = node, x
        node.next, temp.prev = temp, node
        return node

    def insert_before(self, x):
        return self.insert_after(x.prev)

    def remove(self, x):
        prev_node = x.prev
        prev_node.next, x.next.prev = x.next, prev_node
        return

    def get_head(self):
        return self.head_node.next

    def get_tail(self):
        return self.tail_node.prev

    def get_sentinel_head(self):
        return self.head_node

    def get_sentinel_tail(self):
        return self.tail_node


class AllOne:
    def __init__(self):
        self.dll, self.key_counter = DoubleLinkedList(), defaultdict(int)
        self.node_freq = {0: self.dll.get_sentinel_head()}

    def _rmv_key_prev_freq_node(self, prev_freq, key):
        node = self.node_freq[prev_freq]
        node.remove_key(key)
        if node.is_empty():
            self.dll.remove(node)
            self.node_freq.pop(prev_freq)
        return

    def inc(self, key: str) -> None:
        self.key_counter[key] += 1
        cur_freq, prev_freq =\
            self.key_counter[key], self.key_counter[key]-1
        if cur_freq not in self.node_freq:
            self.node_freq[cur_freq] =\
                self.dll.insert_after(self.node_freq[prev_freq])
        self.node_freq[cur_freq].add_key(key)
        if prev_freq > 0:
            self._rmv_key_prev_freq_node(prev_freq, key)

    def dec(self, key: str) -> None:
        if key in self.key_counter:
            self.key_counter[key] -= 1
            cur_freq, prev_freq =\
                self.key_counter[key], self.key_counter[key]+1
            if self.key_counter[key] == 0:
                self.key_counter.pop(key)
            if cur_freq != 0:
                if cur_freq not in self.node_freq:
                    self.node_freq[cur_freq] =\
                        self.dll.insert_before(self.node_freq[prev_freq])
                self.node_freq[cur_freq].add_key(key)
            self._rmv_key_prev_freq_node(prev_freq, key)

    def getMaxKey(self) -> str:
        if self.dll.get_tail().count() > 0:
            return self.dll.get_tail().get_any_key()
        else:
            return ""

    def getMinKey(self) -> str:
        if self.dll.get_tail().count() > 0:
            return self.dll.get_head().get_any_key()
        else:
            return ""
