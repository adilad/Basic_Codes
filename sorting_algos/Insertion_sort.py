a=[89, 12, 5, 6, 78, 1112, 200, 1000, 10, 90,90600660,343,1,445,56]

def insert_sort(a):

    k=1
    while(k<=len(a)-1):

        for i in range(k,0,-1):

            if a[i]<a[i-1]:
                a[i],a[i-1]=a[i-1],a[i]
            else:
                i=i+1
        k=k+1

    return a

