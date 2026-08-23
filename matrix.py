'''
r=int(input("enter the no of rows"))
c=int(input("enter the no of columns"))
a=[]
print("enter the elements")
for i in range(r):
    row=[]
    for j in range(c):
        val=int(input(f"enter the element of [{i}[{j}]]"))
        row.append(val)
    a.append(row)
for i in range(r):
    for j in range(c):
        print(a[i][j],end=" ")
    print()
for i in range(r):
    for j in range(c):
        print(f"index [{i}][{j}]={a[i][j]}, address={id(a[i][j])},inhexadecimal={hex(id(a[i][j]))}")
     '''
#deletion from any index

a=[10,20,30,40,50]
'''
def deletion(arr,index):
    for i in range(0,len(arr)-1):
        arr[i]=arr[i+1]

    return arr[:-1]
'''
'''
#insertion from beggining
def insertion(arr):
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=1
    return arr
print(insertion(a))
'''


