#Quick Sort
#Worse case O(n^2)  average case O(nlogn)

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([8,3,7,2,9,4,5,11,1]))


#Merge Sort
#Worse case, avg case, best case are all O(nlogn)
"""This is the standard implementation for merge sort which I will be 
applying to both prefa and prefa and counting their inverts"""
def merge_sort(Arr: list) -> list:
    if len(Arr) > 1: 
        m = len(Arr) // 2
        leftArr, rightArr = Arr[:m], Arr[m:]
        
        #recursion
        merge_sort(leftArr)
        merge_sort(rightArr)

        #merge left and right
        i, j = 0, 0
        k = 0
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                Arr[k] = leftArr[i]
                i += 1
            else:
                Arr[k] = rightArr[j]
                #each time there is an invert I add the pair of values as a tuple
                j += 1
            k += 1
        
        while i < len(leftArr):
            Arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            Arr[k] = rightArr[j]
            j += 1
            k += 1

        return Arr