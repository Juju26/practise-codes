def inserti(arr):
    for i in range(1,len(arr)):
        j=i-1
        ne=arr[i]
        print('ne :',ne,end=' ')
        while j>=0 and arr[j]>ne:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=ne
        print(arr)
    print("sorted :",arr)
arr=[23,24,2,3,1,56,32,70,0,-1]
inserti(arr)
arr.sort()