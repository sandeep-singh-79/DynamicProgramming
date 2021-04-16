def gridTravellerMemo(m, n, memo=None):
    if isinstance(memo, type(None)): memo = {}
    if ((m, n) in memo or (n, m) in memo): return memo[(m, n)]
    if (m == 0 or n == 0): return 0
    if (m == 1 and n == 1): return 1

    memo[(m, n)] = gridTravellerMemo(m - 1, n, memo) + gridTravellerMemo(m, n - 1, memo)
    memo[(n, m)] = memo[(m, n)]
    return memo[(m, n)]
