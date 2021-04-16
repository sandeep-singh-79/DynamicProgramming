def howSum(sum, arr):
    if sum == 0: return []
    if sum < 0: return None

    for item in arr:
        remainder = sum - item
        itemsForSum = howSum(remainder, arr)
        if itemsForSum != None:
            itemsForSum.append(item)
            return itemsForSum
    
    return None
