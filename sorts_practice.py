def mergesort(arr, start, end):
    if start < end:
        # calculate mid like this only
        # not like (end-start)/2
        mid = start + (end - start) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        msort(arr, start, mid, end)


def msort(arr, start, mid, end):
    # second parameter is non inclusive
    # so increase it by 1 --> L from start to
    # mid+1, R from mid+1 to end+1
    # always put start and end indices when selecting sub arrays
    # because start and end change in each recursive call
    # if we dont give one index, it will select all of sub array
    L = arr[start:mid + 1]
    R = arr[(mid + 1):(end + 1)]
    i = 0
    j = 0
    k = start

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def call_quicksort(arr1):
    start = 0
    end = len(arr1) - 1
    quicksort(arr1, start, end)


def quicksort(arr1, start, end):
    if start < end:
        # we dont calculate mid, we sort array
        # around pivot. sort from end to beginning
        # keep doing for all eles
        pivot = partition(arr1, start, end)
        quicksort(arr1, start, pivot - 1)
        quicksort(arr1, pivot + 1, end)


def partition(arr1, start, end):
    pivot = arr1[end]
    lowerpointer = start - 1
    # get eles lesser than pivot
    # in arr[lowerpointer] pos
    # if arr[i] is less than pivot,
    # then we have to put it in arr[lowerpointer]
    # position. all eles greater than pivot
    # will be in pos not traversed by lowerpointer
    # ele at lowerpointer pos previously, which will be
    # swapped with ith ele lower than pivot,
    # will be pushed forward, and compared later
    # with lowerpointer and pivot.
    for i in range(start, end):
        if arr1[i] < pivot:
            lowerpointer += 1
            temp = arr1[i]
            arr1[i] = arr1[lowerpointer]
            arr1[lowerpointer] = temp

    # lowerpointer has traversed all array
    # and sorted based on lower than pivot.
    # now insert pivot just after lowerpointer
    # and send ele at this position, at which pivot
    # will be inserted, to end. return the end element
    # as pivot.
    lowerpointer += 1
    temp = arr1[lowerpointer]
    arr1[lowerpointer] = pivot
    arr1[end] = temp
    return lowerpointer

if __name__ == "__main__":
    arr = [5, 78, 21, 34, 12, 6, 90, 99, 22]
    # merge sort
    mergesort(arr, 0, len(arr) - 1)
    print(arr)

    arr1 = [89, 90, 2, 38, 32, 41, 99, 4, 0, 88, 15]
    call_quicksort(arr1)
    print(arr1)
