def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                te=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=te
    print(arr)

def gbubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)

arr=[23,24,2,3,1,56,32,70,0,-1,20,26,47,89]
#bubble(arr)
gbubble(arr)