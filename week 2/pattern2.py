n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j<=i):
            print(i,end=" ")
    print()    
