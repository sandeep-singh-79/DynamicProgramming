def allConstruct(targetStr, wordBank):
    if len(targetStr) == 0: return list()

    totalCombinations = []

    for word in wordBank:
        if targetStr.startswith(word):
            suffixcombination = allConstruct(targetStr[len(word):], wordBank)
            targetCombination = suffixcombination + [word]
            totalCombinations.extend(targetCombination)
    
    return totalCombinations
