def howSumMemoized(sum, arr, memo = None):
    if isinstance(memo, type(None)): memo = {}
    if sum in memo: return memo[sum]
    if sum == 0: return []
    if sum < 0: return None

    for item in arr:
        remainder = sum - item
        itemsForSum = howSumMemoized(remainder, arr, memo)
        if itemsForSum != None:
            itemsForSum.append(item)
            memo[sum] = itemsForSum
            return itemsForSum
    
    memo[sum] = None
    return None
