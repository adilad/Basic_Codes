s=[110,7,8,9,1,56,13,14,324]

def quick_sort(a,low,high):
    
    i=low-1
    pivot=a[high]
    
    for j in range(low,high):
        if a[j]<=pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
        else:
            pass
    a[i+1],a[high]=a[high],a[i+1]    
    return i+1
    
def sort(a,low,high):
    if low<high:
        pi=quick_sort(a,low,high)
    
    quick_sort(a,low,pi-1)
    quick_sort(a,pi+1,high)

    return a 

print(sort(s,0,len(s)-1))


PSEDUO code 

1) The aim is that we need to take a pivot element and then sort around that
2) i=low,pivot=a[high]
3) loop j=low,high (this has to be low)
    if a[j]<=pivot:
        exchange i=i+1 and j 
4) in the end exahnge the pivot node and i+1 
