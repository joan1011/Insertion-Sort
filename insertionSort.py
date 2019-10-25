def insertionSort(array):
# Looping through an array to calculate the length and iterate from 1 to len array
# i is assigned to j so that j can be decremented and compare with value of i and sorted
    for i in range(1,len(array)):
        j = i
# using a while loop 
        while j>0 and array[j] < array[j-1]:
            swap(j,j-1,array)
            j -=1
    return array
    
def swap(i, j, array):
    array[i],array[j] = array[j],array[i]
    
insertionSort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]),
