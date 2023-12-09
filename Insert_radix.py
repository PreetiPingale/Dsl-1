def insertionSort(smarks):

 for i in range(0,len(smarks)-1):

 for j in range(i+1,0,-1):

 if smarks[j] < smarks[j-1]:

 smarks[j], smarks[j-1]=smarks[j-1], smarks[j]

def shellSort(smarks):

 gap=len(smarks)//2

 while gap > 0:

 for i in range(gap,len(smarks)):

 current=smarks[i]

 j=i

 while j >= gap and current < smarks[j-gap]:

 smarks[j]=smarks[j-gap]

 j=j-gap

 smarks[j]=current

 gap=gap//2

smarks=[]

n=int(input("Enter no. of students: "))

print("Enter marks of students: ")

for i in range(n):

 m=float(input())

 smarks.append(m)

print("\n1.Insertion sort \n2. Shell Sort \n Enter your choice :")

ch=int(input())

if(ch==1):

 insertionSort(smarks)

elif(ch==2):

 shellSort(smarks)

else:

 print("Invalid choice")

print("Marks in ascending order: ")

print(smarks)
print("Top 5 marks: ")

for i in range(n-1,n-6,-1):

 print(smarks[i])
