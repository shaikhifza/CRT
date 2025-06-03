class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begining(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=Node(data) 
        if self.head is None: 
            self.head=new_node 
        else:
            temp=self.head
            while temp.next:  
                temp=temp.next 
            temp.next=new_node 
    def insert_position(self,pos,data):
        if pos==0:
            self.insert_begining(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def delete_begining(self):
        self.head=self.head.next
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def delete_position(self,pos,data):
        if pos==0:
            self.delete_begining(data)
        else:
            new_node=Node(data)
            temp=self.head
            for i in range(pos-1):
                if temp.next is None:
                    print("Position out of bound")
                    return
                temp=temp.next
            temp.next=temp.next.next
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
ll=LinkedList()
ll.insert_begining(1)
ll.insert_begining(2)
ll.insert_begining(3)
ll.insert_begining(3)
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_position(2,89)
ll.delete_begining()
ll.delete_end()
ll.delete_position(3,2)
ll.display()

'''#insert at begin
1
2,1
3,2,1
3,3,2,1
#insert at end
3,3,2,1,10,20,30,40
#insert at specific pos
3,3,89,2,1,10,20,30,40
#delete at begin
3,89,2,1,10,20,30,40
#delete at end
3,89,2,1,10,20,30
#delete at specific pos
3,89,2,10,20,30'''

