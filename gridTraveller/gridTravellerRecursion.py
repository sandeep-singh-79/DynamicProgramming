def gridTraveller(m, n):
    if (m == 0 or n == 0): return 0
    if (m == 1 and n == 1): return 1
    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)
