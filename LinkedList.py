class LinkedList():
    
    def __init__(self):
        #Variable en el costructor con valor None
        self.head = None
    
    #Metodo para agregar elementos a la lista
    def add(self, value):
        self.value = value
        self.head = Nodo(self.value, next = self.head)
        
    #Metodo para imprimir la lista
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
    
if __name__ == "__main__":
    main()
