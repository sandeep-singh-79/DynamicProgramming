def fibByRecursionMemo(n, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if(n in memo): return memo[n]
    if(n <= 2): return 1
    memo[n] = fibByRecursionMemo(n-1, memo) + fibByRecursionMemo(n-2, memo)
    return memo[n]
