n,m=map(int,input("Enter the size of matrix: ").split(" "))
print("Enter elements")
arr=[]
for i in range(n):
    val=[]
    for j in range(m):
         val.append(int(input())) 
    arr.append(val) 
print("The upper triangular matrix is as follows: ")
for i in range(n):
    for j in range(m):
        if(i<=j):
            print(arr[i][j],end="\t")
        else:
            print(0,end="\t")
    print()
