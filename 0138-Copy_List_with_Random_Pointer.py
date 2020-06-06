from __future__ import annotations


class Node:
    def __init__(self, x: int, next: 'Node'=None, random: 'Node'=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        # copy nodes
        node = head
        while node:
            copy = node.next
            node.next = Node(node.val)
            node.next.next = copy
            node = copy

        # copy random pointers
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next

        # separate two parts
        second = node = head.next
        while node.next:
            head.next = node.next
            head = head.next
            node.next = head.next
            node = node.next

        head.next = None

        return second


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return

        node, copy = head, {}

        # copy nodes
        while node:
            copy[node] = Node(node.val)
            node = node.next
        node = head

        # copy random pointers
        while node:
            if node.random:
                copy[node].random = copy[node.random]
            if node.next:
                copy[node].next = copy[node.next]
            node = node.next

        return copy[head]


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy = dict()
        m = n = head

        while m:
            copy[m] = Node(m.val)
            m = m.next

        while n:
            copy[n].next = copy.get(n.next)
            copy[n].random = copy.get(n.random)
            n = n.next

        return copy.get(head)


from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        It can be done in one pass because he's using defaultdict,
        so he's just able to update the values as he gets to them
        without a key error. The reason for dic[None] = None is
        so he can do things like return dic[head] when operating
        on an empty list, meaning head == None. This also allows him
        to not check that each node has a random pointer because
        if random is None then it just gets assigned accordingly.
        """
        copy = defaultdict(lambda: Node(0))
        copy[None] = None
        node = head

        while node:
            copy[node].val = node.val
            copy[node].next = copy[node.next]
            copy[node].random = copy[node.random]
            node = node.next

        return copy[head]


"""
simple or statements:
The statement x or y returns x if x evaluates to True, otherwise it returns y (even if both are False), let us look at a few examples:
1 or 2 returns 1, because 1 evaluates to True
0 or 1 returns 1
0 or '' returns ''

simple and statements:
The statement x and y returns x if x evaluates to False, otherwise it returns y (even if both are True), let us look at a few examples:
1 and 2 returns 2
1 and 0 returns 0
0 and 2 returns 0
So we can see that intuitively the above statements are evaluated in a "short circuit" manner, i.e. the statement is evaluated from left to right and whichever variable determines the value of the boolean expression first is returned.

Now let us have a look at some complicated examples with the above intuition:
Continuous or statements
The variable which first evaluates to True is returned else the last variable is returned.
Examples:
1 or 2 or 3 or 4 returns 1
'' or {} or [] or 4 returns 4
'' or {} or [] returns []
Continuous and statements
The variable which first evaluates to False is returned else the last variable is returned
Examples:
1 and 2 and 3 returns 3
1 and '' and 4 returns ''
0 and '' and 4 returns 0

More complex statements:
What if compound statements mixed with and and or are used?
In such cases we have to remember that and has a higher precedence than or and the order of evaluation of the expression is always from left to right, and lastly remember the 'short circuit' intuition.
Let us have a look at some statements:
1 and 2 or 4 returns 2, why?
1 and 2 or 4 is evaluated as (1 and 2) or (4), (1 and 2) evaluates to True, so the or statement returns 1 and 2 which further returns 2
Infact the ternary condition x if condition else y can be rewritten as
condition and x or y ! (prove it to yourself) , although it is not recommended for readability purposes.
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Insert each node's copy right after it with .val
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next

        # Separate the copied list from the original,
        # (re)setting every .next
        node = head
        copy = headCopy = head and head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next

        return headCopy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # create new nodes
        node = head
        while node:
            # modify 'random' field instead of the 'next' field
            # in the copied list
            node.random = Node(node.val, node.random, None)
            node = node.next

        # populate random field of the new node
        node = head
        while node:
            node.random.random = node.random.next.random\
                                 if node.random.next else None
            node = node.next

        # restore original list and build new list
        headCopy = head.random if head else None
        node = head
        while node:
            node.random.next = node.next.random\
                               if node.next else None
            node.random = node.random.next
            node = node.next

        return headCopy


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        a nice thing for "modify 'random' field instead of the 'next'
        field in the copied list" is that the original list's next
        structure is never changed, so you can write a helper generator
        to visit the original list with a nice for loop encapsulating
        the while loop and making the loop bodies a little simpler:
        """
        def nodes():
            node = head
            while node:
                yield node
                node = node.next

        # create new nodes
        for node in nodes():
            node.random = Node(node.val, node.random, None)

        # populate random field of the new node
        for node in nodes():
            node.random.random = node.random.next and\
                                 node.random.next.random

        # restore original list and build new list
        headCopy = head and head.random
        for node in nodes():
            node.random.next = node.next and node.next.random
            node.random = node.random.next

        # return headCopy
        print(headCopy)
