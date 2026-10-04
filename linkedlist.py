'''
#its a manual linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.next=node3

head=node1
#for travesal
current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print(None)
'''
'''
class Node:
    def __init__(self,data):                        ##here it is a order of n complexity  we are traversing head but next code is order of 1 and we are using a tail pointer 
        self.data=data
        self.next=None
head=None
n=int(input("enter the number of nodes"))
for i in range(n):
    data=int(input("enter the data"))
    new_node=Node(data)
    if head is None:
        head=new_node
    else:
        current=head
        while current.next is not None:
            current=current.next
        current.next=new_node

current=head
while current is not None:
    print(current.data,end="->")
    current=current.next
print("None")
'''
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = None
tail = None
n = int(input("Enter the number of nodes: "))
for i in range(n):
    data = int(input("Enter the data: "))
    new_node = Node(data)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node
current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("None")
'''