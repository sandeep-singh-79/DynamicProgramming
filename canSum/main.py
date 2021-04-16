from canSum import canSum
from canSumMemoized import canSumMemoized

if __name__ == "__main__":
    print("===========================================")
    print("Can Sum Memoized")
    print("===========================================")
    print(canSumMemoized(7, [2, 3]))
    print(canSumMemoized(7, [5, 3, 4, 7]))
    print(canSumMemoized(7, [2, 4])) # this case returns true after memoization when even one example is run before it.
    print(canSumMemoized(8, [2, 3, 5]))
    print(canSumMemoized(300, [7, 14]))
    print("===========================================")
    print("Can Sum Recursion")
    print("===========================================")
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))
