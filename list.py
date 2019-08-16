li=[]
even_li=[]
n=int(input("Enter the size of the list: "))
for i in range(0,n):
   numbers=int(input("Enter the numbers into the list: "))
   li.append(numbers)
   print (li)
def divide(li):
    
    for i in li:
        if(i%2==0):
            even_li.append(i)
divide(li)
print(even_li)

