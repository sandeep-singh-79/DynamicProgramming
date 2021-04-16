def canSum(sum, arr):
    if sum == 0: return True
    if sum < 0: return False

    for i in arr:
        if canSum((sum - i), arr) == True: return True

    return False
