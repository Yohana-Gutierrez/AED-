class Link(object):
    def __init__(self, data):
        self.data = data
        self.next_link = None

class LinkedList(object):
    def __init__(self):
        self.first_link = None

    def insert(self, data):
        new_link = Link(data)
        new_link.next_link = self.first_link
        self.first_link = new_link

    def getFirst(self):
        return self.first_link

    def __iter__(self):
        next_link = self.getFirst()
        while next_link is not None:
            yield next_link.data
            next_link = next_link.next_link

    def traverse(self, func=print):
        for item in self:
            func(item)

    def __str__(self):
        result = "["
        first = True
        for item in self:
            if not first:
                result += " > "
            result += str(item)
            first = False
        return result + "]"

    def __len__(self):
        return sum(1 for _ in self)

# Crear una lista enlazada
my_list = LinkedList()

# Agregar elementos a la lista
my_list.insert("Anny")
my_list.insert("Cristina")
my_list.insert("Carla")

# Imprimir la representación de la lista
print("Lista enlazada de nombres:", my_list)

# Recorrer la lista y saludar a cada persona
def saludar(nombre):
    print(f"Hola, {nombre}!")

print("Saludos a las personas en la lista:")
my_list.traverse(saludar)



