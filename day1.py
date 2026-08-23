##time complexity
#def binary_search(arr,target):
#    low=0
#    high=len(arr)-1
#    while low <= high:
#        mid=(low+high)//2
#        if arr[mid]==target:
#            return mid
#        elif arr[mid]<target:
#            low =mid+1
#        elif arr[mid]>target:
#            high=mid-1
#    return -1
#g=[1,45,67,89,2,560,234]
#p=int(input("enter the target"))
#g.sort()
#target=p
#result=binary_search(g,target)
#if result !=-1:
#    print(f"element {target} found at index{result}")
#else:
#    print(f"not found")
my_list=[]
user_input=input("enter the data with single space")
my_list=[(int(x),str(x)) for x  in user_input.split()]
print(my_list)