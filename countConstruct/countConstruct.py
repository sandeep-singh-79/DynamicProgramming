def countConstruct(target, wordBank):
    if target is str or len(target) == 0: return 1

    totalCount = 0

    for word in wordBank:
        if (target.startswith(word)):
            count = countConstruct(target[len(word):], wordBank)
            totalCount += count

    return totalCount
