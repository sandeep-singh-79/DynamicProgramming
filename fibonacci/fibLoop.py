def fibByLoop(n):
    if n <= 2: return 1
    first = 1
    second = 1
    for i in range(2,n):
        retval = first + second
        first = second
        second = retval
    return retval;
