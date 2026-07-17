def minimum(arr):
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(len(arr) - 1):
        farthest = max(farthest, i + arr[i])  # Update the farthest reachable index

        if i == current_end:  # If we have reached the end of the current jump
            jumps += 1  # Increment the jump count
            current_end = farthest  # Move to the farthest reachable index

            if current_end >= len(arr) - 1:  # If we can reach or exceed the last index, break out of the loop
                break

    return jumps
# Example usage:
arr = [1,3,5,8,0,9,2,6,7,6,8,9]






