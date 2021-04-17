def bestSumMemoized(sum, arr, memo=None):
    if isinstance(memo, type(None)): memo = dict()
    if sum in memo: return memo[sum]
    if sum == 0: return []
    if sum < 0: return None

    shortestCombination = None

    for item in arr:
        remainder = sum - item
        remaindercombination = bestSumMemoized(remainder, arr, memo)
        if remaindercombination != None:
            combination = remaindercombination.copy()
            combination.append(item)
            if (shortestCombination == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[sum] = shortestCombination
    return shortestCombination
