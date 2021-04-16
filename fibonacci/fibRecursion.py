def fibByRecursion (n):
    if(n <= 2): return 1
    return fibByRecursion(n-1) + fibByRecursion(n-2)