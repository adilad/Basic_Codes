a=[89, 12, 5, 6, 78, 1112, 200, 1000, 10, 90]
b=[5, 89, 12, 6, 78, 1112, 200, 1000, 10, 90]

def selection(a):
    for k in range(0,len(a)):
        min=a[k]
        index=k
        for i in range(k,len(a)):
            if a[i]<=min:
                min=a[i]
                index=i
            else:
                pass

        a[k],a[index]=a[index],a[k]

    return min,index,a


print(selection(a))

