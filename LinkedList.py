class LinkedList():
    
    def __init__(self):
        self.head = None
    
    def add(self, value):
        self.value = value
        self.head = Nodo(self.value, next = self.head)
        
    def printList(self):
        
        Nodo = self.head
        while Nodo != None:
            print (Nodo.value, end= " - ")
            Nodo = Nodo.next

class Nodo():
        
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
            
def main ():
    
    linkedlist = LinkedList()
    
    for i in range(10):
        linkedlist.add(i+1)

    print('Secuencia de la lista enlazada')
    linkedlist.printList()
    print(0, end='')
    
    pass
    
if __name__ == "__main__":
    main()
