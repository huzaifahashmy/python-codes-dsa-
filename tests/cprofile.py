import cProfile

def solve():
    arr = [i for i in range(100000)]
    return sum(arr)

cProfile.run("solve()")