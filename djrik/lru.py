class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.prev = prev
        self.val = val
        self.next = next

    """Inserts a new node as this node's next node"""

    def insert_after(self, val):
        current_next = self.next
        self.next = ListNode(val, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Inserts a new node as this node's previous node"""

    def insert_before(self, val):
        current_prev = self.prev
        self.prev = ListNode(val, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Deletes this node from the List"""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Doubly-linked List class"""


class List:
    def __init__(self, node=None):
        self.head = node
        self.tail = node.next if node else None

    """Adds the given value as the new head of the List"""

    def add_to_head(self, val):
        if not self.head:
            self.head = ListNode(val, None, self.tail)
        elif not self.tail:
            self.tail = self.head
            self.head = ListNode(val, None, self.tail)
            self.tail.prev = self.head
        else:
            self.head = ListNode(val, None, self.head)
            self.head.next.prev = self.head

    """Removes the head of the List and returns its value"""

    def shift(self):
        if not self.head:
            if not self.tail:
                return None
            return self.remove_from_tail()
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            return current_head.val

    """Adds the given value as the new tail of the List"""

    def add_to_tail(self, val):
        if not self.tail:
            self.tail = ListNode(val, self.head, None)
        elif not self.head:
            self.head = self.tail
            self.tail = ListNode(val, self.head, None)
            self.head.next = self.tail
        else:
            self.tail = ListNode(val, self.tail, None)
            self.tail.prev.next = self.tail

    """Removes the tail of the List and returns its value"""

    def remove_from_tail(self):
        if not self.tail:
            if not self.head:
                return None
            return self.shift()
        else:
            current_tail = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return current_tail.val

    """Moves the given node to the head of the List"""

    def move_to_front(self, node):
        value = node.val
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
        self.add_to_head(value)

    """Moves the given node to the tail of the List"""

    def move_to_end(self, node):
        value = node.val
        if node is self.head:
            self.shift()
        else:
            node.delete()
        self.add_to_tail(value)
