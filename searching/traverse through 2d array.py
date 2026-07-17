def count_element(arr, k):
    count = 0

    for i in arr:
        low, high = 0, len(i) - 1
        first = -1

        # find first occurrence
        while low <= high:
            mid = (low + high) // 2
            if i[mid] == k:
                first = mid
                high = mid - 1
            elif i[mid] > k:
                high = mid - 1
            else:
                low = mid + 1

        # if not found in this row, skip
        if first == -1:
            continue

        low, high = 0, len(i) - 1
        last = -1

        # find last occurrence
        while low <= high:
            mid = (low + high) // 2
            if i[mid] == k:
                last = mid
                low = mid + 1
            elif i[mid] > k:
                high = mid - 1
            else:
                low = mid + 1

        count += last - first + 1

    return count


# test
arr = [
    [10, 20, 20, 30],
    [20, 20, 40],
    [10, 20, 50]
]

print(count_element(arr, 20))








# IT HAS A TIME COMPLEXITY OF O(m log n) WHERE m IS THE NUMBER OF ROWS AND n IS THE NUMBER OF COLUMNS IN THE 2D ARRAY.