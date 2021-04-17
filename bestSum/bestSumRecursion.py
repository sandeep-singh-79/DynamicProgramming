def bestSum(sum, arr):
    if sum == 0: return []
    if sum < 0: return None

    shortestCombination = None

    for item in arr:
        remainder = sum - item
        combination = bestSum(remainder, arr)
        if combination != None:
            combination.append(item)
            if (shortestCombination == None) or (len(combination) < len(shortestCombination)):
                shortestCombination = combination

    return shortestCombination
