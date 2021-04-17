from bestSumRecursion import bestSum
from bestSumMemoized import bestSumMemoized

if __name__ == "__main__":
    print("===========================================")
    print("Best Sum Memoized")
    print("===========================================")
    print(bestSumMemoized(7, [2, 3, 5])) # [5, 2]
    print(bestSumMemoized(7, [5, 3, 4, 7])) # [7]
    print(bestSumMemoized(8, [1, 4, 5]))  # [4, 4]
    print(bestSumMemoized(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
    print("===========================================")
    print("Best Sum Plain Recursion")
    print("===========================================")
    print(bestSum(7, [2, 3, 5]))
    print(bestSum(7, [5, 3, 4, 7]))
    print(bestSum(8, [1, 4, 5]))
    print(bestSum(100, [1, 2, 5, 25]))
