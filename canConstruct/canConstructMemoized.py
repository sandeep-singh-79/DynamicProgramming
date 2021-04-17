def canConstructMemoized(targetStr, wordbank, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if targetStr in memo: return memo[targetStr]
    if targetStr is str or len(targetStr) == 0: return True

    for word in wordbank:
        if (targetStr.startswith(word)):
            suffix = targetStr[len(word):]
            if (canConstructMemoized(suffix, wordbank, memo)):
                memo[targetStr] = True
                return True
    
    memo[targetStr] = False
    return False
