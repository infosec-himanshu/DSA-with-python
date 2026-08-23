# FIFO = First In First Out
# Linear queue like a movie ticket row
'''
size = 10
queue = [0] * size
front = -1
rear = -1
while True:
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Display updated")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            item = int(input("Enter the item: "))
            if rear == size - 1:
                print("Queue is full, no more space")
            else:
                rear = rear + 1
                queue[rear] = item
                if front == -1:
                    front = 0
        case 2:
            if front == -1 or front > rear:
                print("Queue is empty")
            else:
                deleted = queue[front]
                front = front + 1
                print(f"Deleted item is: {deleted}")
        case 3:
            if front == -1 or front > rear:
                print("Queue is empty")
            else:
                print("Current Queue:")
                for i in range(front, rear + 1):
                    print(queue[i], end=" ")
                print()
        case 4:
            break
        case _:
            print("Enter a valid choice")

'''
'''
#circular queue
size = 10
queue = [0] * size
front = -1
rear = -1
while True:
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Display updated")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            item=int(input("enter the item to insert"))
            if (rear+1)%size==front:
                print("circular queue is full")
            else:
                if front==-1:
                    front=0
                    rear=0
                else:
                    rear=(rear+1)%size
                queue[rear]=item

           
        case 2:
             if front == -1:
                print("queue is empty")
             else:
            
                deleted = queue[front]                   
                queue[front] = 0                         
            
                if front == rear:
                    front = -1
                    rear = -1
                else:
                    front = (front + 1) % size           
                print(f"the item deleted is {deleted}")
        case 3:
            if front==-1:
                print("queue is empty")
            else:
                i=front
                while True:
                    print(queue[i],end=" ")
                    if i==rear:
                        break
                    i=(i+1)%size
        case 4:
            break
        case _:
            print("enter choice from 1 to 4")


                
                

            '''

#priority Queue:
'''
size=10
queue=[0]*size
priority=[0]*size
rear=-1

while True:
    print("\n1. Insertion")
    print("2. Deletion")
    print("3. Display updated")
    print("4. Exit")
    ch = int(input("Enter your choice: "))
    match ch:
        case 1:
            if  rear==size-1:
                print("queue is full")
            else:
                item=int(input("enter the item"))
                p=int(input("enter the priority of that element"))
                rear=rear+1
                queue[rear]=item
                priority[rear]=p
        case 2:
            if rear==-1:
                print("queue is empty")
            else:
                highest=0
                for i in range(1,rear+1):
                    if priority[i]>priority[highest]:
                        highest=i
                deleted=queue[highest]
                print(f"deleted item is:{queue[highest]} ")
                print(f"priority of element:{priority[highest]}")
                for i in range(highest,rear):
                    queue[i]=queue[i+1]
                    priority[i]=priority[i+1]
                rear=rear-1
        case 3:
            if rear==-1:
                print("queue is empty")
            else:
                for i in range(rear+1):
                    print(queue[i])

        case 4:
            break
        case _:
            print("enter a valid choice")
            

'''


