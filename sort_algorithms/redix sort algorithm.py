def counting_sort(arr, exp):
    n = len(arr)
    
    output = [0] * n        # output array
    count = [0] * 10        # digits 0–9

    # 🔹 Step 1: Count frequency
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # 🔹 Step 2: Prefix sum (cumulative)
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 🔥 Step 3: Build output (RIGHT → LEFT)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        
        position = count[digit] -1    # find correct index
        output[position] = arr[i]
        
        count[digit] -= 1             # 🔑 decrement

    # 🔹 Copy back to original array
    for i in range(n):
        arr[i] = output[i]
    
    print(output)


def radix_sort(arr):
    max_val = max(arr)

    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


# 🔥 Example run
arr = [170, 45, 75, 90, 802, 24, 2, 66, 66 , 66]
radix_sort(arr)
print(arr)