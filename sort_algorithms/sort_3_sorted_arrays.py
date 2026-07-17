class Solution:
    def merge(self, arr1, arr2, arr3):
        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        result = []

        # Merge all three
        while i < n1 and j < n2 and k < n3:
            if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                result.append(arr1[i])
                i += 1
            elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr3[k])
                k += 1

        # Merge remaining two arrays
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        while j < n2 and k < n3:
            if arr2[j] <= arr3[k]:
                result.append(arr2[j])
                j += 1
            else:
                result.append(arr3[k])
                k += 1

        while i < n1 and k < n3:
            if arr1[i] <= arr3[k]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr3[k])
                k += 1

        # Add leftovers
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        result.extend(arr3[k:])

        return result


    def val_weight(self, val , weight , capacity):
        # putted = 0 
        total = 0
        total_weight = 0

        # items = sorted([(val[i]/weight[i] , val[i] ,weight[i] ) for c] , reverse=True)
        items = sorted([(v / w, v, w) for v, w in zip(val, weight)], reverse=True)
        


        print(items)



# flow of the execution -> first compare the 3 arryas  -> compare all 2 arrays with their comparisons -> after that add all the remaining elements 



Solution().val_weight([10, 5, 15, 7, 6, 18, 3] , [2, 3, 5, 7, 1, 4, 1] , 15)

