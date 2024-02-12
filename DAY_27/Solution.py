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
            
    def count(self):
        county=0
        current_node=self.head
        while(current_node):
            county+=1
            current_node=current_node.next
        return county


l=LinkedList()
l.InsertAtBeginning(1)
l.InsertAtBeginning(2)
l.InsertAtBeginning(3)
l.InsertAtBeginning(4)
l.InsertAtBeginning(5)

c=l.count()
print("Number of nodes in the linkedlist :",c)
