def merge(arr, l, m, r): 
    # code here
    # print(arr)
    L  = arr[:m]
    R = arr[m:]
    
    i = j = k = 0 
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k +=1
            
    
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1
    
            
            
def mergeSort(arr, l, r):
    #code here
    if l >= r:
        return
    m = l + (r-l)//2
    mergeSort(arr, l, m)
    mergeSort(arr, m+1, r)
    merge(arr,l,m,r)

def mergeSortNew(arr):
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSortNew(L)

        # Sorting the second half
        mergeSortNew(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    
arr = [6334, 4098, 7968, 4523, 277, 6956, 4560, 2062, 5705, 5743, 879, 5626, 9961, 491, 2995, 741, 4827]
# mergeSort(arr, 0, len(arr))
mergeSortNew(arr)
print(arr)
