def canConstruct(target, wordBank):
    if target is str or len(target) == 0: return True

    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            if (canConstruct(suffix, wordBank):
                return True

    return False
