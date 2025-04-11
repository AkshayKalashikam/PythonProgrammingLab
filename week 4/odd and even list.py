def create_list(l1,n1):
    
    for i in range(n1):
        temp = int(input("enter numbers in list : "))
        l1.append(temp)
    print(l1)
    
def evensum(l1,n1):
    sum=0
    for i in range (n1):
        if(i%2==0):
            sum=sum+l1[i]
    return sum    

def oddsum(l1,n1):
    sum=0
    for i in range(n1):
        if(i%2== 1):
            sum=sum+l1[i]
    return sum
    
n1 = int(input("enter n1 :"))
n2 = int(input("enter n2 :"))
n3 = int(input("enter n3 :")) 

l1=[]
l2=[]
l3=[]
create_list(l1,n1)
create_list(l2,n2)
create_list(l3,n3)

evensum(l1,n1)
evensum(l2,n2)
evensum(l3,n3)
oddsum(l1,n1)
oddsum(l2,n2)
o1=oddsum(l1,n1)
print(o1)
o2=oddsum(l2,n2)
print(o2)
o3=oddsum(l3,n3)
print(o3)
e1=evensum(l1,n1)
print(e1)
e2=evensum(l2,n2)
print(e2)
e3=evensum(l3,n3)
print(e3)
required=(e1+e2+e3)*(o1+o2+o3)
print(required)
oddsum(l3,n3)
