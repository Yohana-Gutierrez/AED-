class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def remove(self):
        if not self.head:
            return None
        removed_data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                prev = current
                current = current.next
            prev.next = current.next
            self.head = prev.next
        return removed_data

    def peek(self):
        if not self.head:
            return None
        return self.head.data

class Stack(LinkedList):
    def push(self, data):
        self.insert(data)

    def pop(self):
        return self.remove()

class Queue(LinkedList):
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head.next
            self.head.next = new_node
            self.head = new_node

    def remove(self):
        return super().remove()  # Reuse the remove method from LinkedList

# Ejemplo de uso
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:")
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Pop:", stack.pop())

queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)

print("\nQueue:")
print("Peek:", queue.peek())
print("Remove:", queue.remove())
print("Remove:", queue.remove())
