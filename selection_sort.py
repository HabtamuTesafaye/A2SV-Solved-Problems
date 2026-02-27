class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            #assum the current postion is the minimum
            minnum_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minnum_index]:
                    minnum_index = j
            
            # swap with the new minimum element foumd
            arr[i],arr[minnum_index] = arr[minnum_index], arr[i]
            
        return arr
            
