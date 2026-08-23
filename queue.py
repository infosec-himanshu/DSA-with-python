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
'''

size = 10

Queue = [0] * size

f = -1
r = -1

while True:

    print("\n\n1. Insertion from rear end")
    print("2. Insertion from front end")
    print("3. Deletion from front end")
    print("4. Deletion from rear end")
    print("5. Print")
    print("6. Exit")

    ch = int(input("Enter the choice: "))

    match ch:

        case 1:
            if f == 0 and r == size - 1:
                print("Deque is full")

            else:
                if r == size - 1:
                    for i in range(f, r + 1):
                        Queue[i - 1] = Queue[i]

                    f = f - 1

                else:
                    r = r + 1

                item = int(input("Enter the element: "))
                Queue[r] = item

                if f == -1:
                    f = 0

        case 2:
            if f == 0 and r == size - 1:
                print("Deque is full")

            else:
                if f == 0:
                    for i in range(r, f - 1, -1):
                        Queue[i + 1] = Queue[i]

                    r = r + 1

                elif f == -1:
                    f = 0
                    r = 0

                else:
                    f = f - 1

                item = int(input("Enter the element: "))
                Queue[f] = item

        case 3:
            if f == -1 and r == -1:
                print("Deque is empty")

            else:
                print("Item deleted is:", Queue[f])

                if f == r:
                    f = -1
                    r = -1

                else:
                    f = f + 1

        case 4:
            if f == -1 and r == -1:
                print("Deque is empty")

            else:
                print("Item deleted is:", Queue[r])

                if f == r:
                    f = -1
                    r = -1

                else:
                    r = r - 1

        case 5:
            if f == -1:
                print("Deque is empty")

            else:
                print("Deque elements are:")

                for i in range(f, r + 1):
                    print(Queue[i], end="\t")

                print()

        case 6:
            break

        case _:
            print("Please enter a valid choice from 1 to 6")


            
    




'''