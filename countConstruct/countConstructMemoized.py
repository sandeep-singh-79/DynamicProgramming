def countConstructMemoized(targetStr, wordbank, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if targetStr in memo: return memo[targetStr]
    if targetStr is str or len(targetStr) == 0: return 1

    totalCount = 0

    for word in wordbank:
        if (targetStr.startswith(word)):
            count = countConstructMemoized(targetStr[len(word):], wordbank, memo)
            totalCount += count
    
    memo[targetStr] = totalCount
    return totalCount
