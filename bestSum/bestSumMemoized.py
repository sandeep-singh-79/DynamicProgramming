def bestSumMemoized(sum, arr, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if sum in memo: return memo[sum]
    if sum == 0: return []
    if sum < 0: return None

    shortestCombination = None

    for item in arr:
        combination = bestSumMemoized((sum - item), arr, memo)
        if combination != None:
            combination.append(item)
            if (shortestCombination
                    == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    memo[sum] = shortestCombination
    return memo[sum]
