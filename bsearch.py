def bsearch(A,n,k):
    low=0;
    high=n-1;
    while(low<=high):
        mid=int((low+high)/2)
        if(A[mid]==k):
            return mid
        else:
            if(k>A[mid]):
                low=mid+1
            else:
                high=mid-1
    return -1
print("Enter elements in ascending order: ")
li=[int(x) for x in input().split()]
k=int(input("Enter element to be searched: "))
res=bsearch(li,len(li),k)
if(res==-1):
    print(k," is not found")
else:
    print(k," is found at position ",res+1)
