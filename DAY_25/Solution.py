class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def InsertAtBeginning(self,data):
        newnode=node(data)
        if(self.head==None):
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
            
    def printList(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.next

n=int(input("Enter the number of nodes you want to insert in the beginning :"))
l=LinkedList()
for i in range(n):
    a=int(input("Enter the data :"))
    l.InsertAtBeginning(a)

print("Linked List :",end=" ")
l.printList()
