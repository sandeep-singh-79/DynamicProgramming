def canSumMemoized(sum, arr, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if sum in memo: return memo[sum]
    if sum == 0: return True
    if sum < 0: return False

    for i in arr:
        remainder = sum - i
        if canSumMemoized(remainder, arr, memo) == True:
            memo[sum] = True
            return True

    memo[sum] = False
    return False
