n=int(input("Enter the number of fibonacci numbers to generate: "))
def fibonacci(n):
    a=0
    b=1
    count=0
    if n == 0:
        print("Invalid number")
    elif n == 1:
        print(a)
    elif n == 2:
        print(b)
    else:
            while count < n:
                print(a,end=',')
                sum=a+b
                a=b
                b=sum
                count+=1

print(fibonacci(n))
