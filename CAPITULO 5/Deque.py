class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def insertIzquierda(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def insertDerecha(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def eliminarIzquierda(self):
        if self.isEmpty():
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return data

    def eliminarDerecha(self):
        if self.isEmpty():
            return None
        data = self.rear.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        return data

    def peekLeft(self):
        if self.isEmpty():
            return None
        return self.front.data

    def peekRight(self):
        if self.isEmpty():
            return None
        return self.rear.data

# Ejemplo de uso
deque = Deque()
word = "Welcome"
for letter in word:
    deque.insertDerecha(letter)

reverse = ''
while not deque.isEmpty():
    reverse += deque.eliminarDerecha()

print('The reverse of', word, 'is', reverse)
