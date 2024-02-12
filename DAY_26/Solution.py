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

    def DeleteAtLast(self):
        current_node=self.head
        if(current_node.next==None):
            self.head=None
        else:
            while(current_node.next!=None):
                if(current_node.next.next==None):
                    current_node.next=None
                else:
                    current_node=current_node.next
            
            
    def printList(self):
        current_node=self.head
        while(current_node):
            print(current_node.data,end=" ")
            current_node=current_node.next

l=LinkedList()
l.InsertAtBeginning(1)
l.InsertAtBeginning(2)
l.InsertAtBeginning(3)
l.InsertAtBeginning(4)
l.InsertAtBeginning(5)


print("Linked List :",end=" ")
l.printList()


l.DeleteAtLast()
l.DeleteAtLast()
l.DeleteAtLast()
l.DeleteAtLast()

print("\nLinked List :",end=" ")
l.printList()




