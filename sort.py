def search(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
my_list=[]
while True:
    print("enter the choice")
    print("\n1.insert data in list\n")
    print("2.find the data index\n")
    print("3.current list\n")
    print("4.exit\n")
    ch=int(input("\nenter your choice:"))

    match ch:
        case 1:
            val=input("enter integer value with a single space")
            newdata=[int(x) for x in val.split()]
            my_list+=newdata
        case 2:
            if not my_list:
                print("list is empty")
                continue
            my_list.sort()
            value=int(input("enter the target wants to search"))
            result=search(my_list,value)
            if result!=-1:
                print(f"target {value} is found at index{result}")
            else:
                print("not found")
        case 3:
            if not my_list:
                print("list is empty")
                continue
            print(my_list)
        case 4:
            break
        case _:
            print("enter a valid choice")
           



## we have to also study the bubble sort it is important