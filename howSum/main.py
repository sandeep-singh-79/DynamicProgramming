from howSum import howSum
from howSumMemoized import howSumMemoized

if __name__ == "__main__":
    print("===========================================")
    print("How Sum Memoized")
    print("===========================================")
    print(howSumMemoized(7, [2, 3]))
    print(howSumMemoized(7, [5, 3, 4, 7]))
    print(howSumMemoized(7, [2, 4])) # this case returns true after memoization when even one example is run before it.
    print(howSumMemoized(8, [2, 3, 5]))
    print(howSumMemoized(300, [7, 14]))
    print("===========================================")
    print("How Sum Recursion")
    print("===========================================")
    print(howSum(7, [2, 3]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(7, [2, 4]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
