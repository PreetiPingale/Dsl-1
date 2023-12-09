arr=[0,0,0,0,0,0,0,0,0]
n=0
key=0
c=1
while c==1:
    
    
    flag=0
    print ("Enter no. of students ")
    n=int(input())
    
    print ("enter roll no. of Student ")
    for i in range(n):
        arr[i]=int(input())
        
    print("Enter key") 
    key=int(input())
    
    
    print ("1. Linear search")
    print("2. Binary Search")
    ch=int(input("Enter your choice "))
    if ch==1:
        for i in range (n):
           if arr[i]==key:
             flag=1
             print ("Key found at ",i+1)
        if flag==0:
           print ("key not found")
    elif ch==2:    
        lb=0
        ub=n-1
    
        while lb<=ub:
            mid=int((lb+ub)/2)
            if arr[mid]==key:
              flag=1
              print ("Key found at",mid+1)
             
            elif key<arr[mid]:
               ub=mid-1
            else:
               lb=mid+1
        if flag==0:
           print ("key not found")
    c=int(input("Do you want to continue 0/1"))
