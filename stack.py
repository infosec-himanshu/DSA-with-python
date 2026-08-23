# stack using python inbuilt functions
'''
class stacks:
    def __init__(self):
        self.dher=[]
    def push(self,value):
        self.dher.append(value)
        print(f"pushed value:{value}")
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.dher.pop()
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.dher[-1]
    def is_empty(self):
        return len(self.dher)==0 
    def size(self):
        return len(self.dher)
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("\n current stack from TOP->BOTTOM")
            for item in reversed(self.dher):
                print(f"{item}")
s=stacks()
s.push(10)
s.push(50)
s.push(60)
s.display()
s.pop()
print(s.peek())
print(s.size())
s.display()
        '''


#stack using core DSA approach:


'''
stack=[0]*2
top=-1

#insertion 
top=top+1
stack[top]=10
top=top+1
stack[top]=20
print(stack)



#deletion
deleted=stack[top]
stack[top]=0
top=top-1
print(f"the deleted element is:{deleted}")
print("stack",stack[0:top-1])
'''


#full user driven code

stack=[0]*2
top=-1
while True:
    print("\n insertion ")
    print("\n deletion")
    print("\n display updated")
    print("\n exit")

    ch=int(input("enter your choice"))

    match ch:
        case 1:
            if top==len(stack)-1:
                print("stack is full")
                continue
            value=int(input("enter the value to insert"))
            top=top+1
            stack[top]=value
            
        case 2:
            if top==-1:
                print("your stack is empty")
                continue
            delete=stack[top]
            stack[top]=0
            top=top-1
            print(f"the deleted item is:{delete}")
            
        case 3:
            if top==-1:
                print("stack is empty")
                continue
            for i in range(0,top+1):
                print(stack[i])

        case 4:
            print("exiting.....")
            break
        case _:

            print("enter the choice from 1 to 4")


        


