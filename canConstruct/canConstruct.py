def canConstruct(target, wordBank):
    if target is str and len(target) == 0: return True

    for word in wordBank:
        if target.startswith(word):
            suffix = remove_prefix(target, word)
            print("%s starts with %s and has suffix: %s" %
                  (target, word, suffix))
            if (canConstruct(suffix, wordBank)):
                return True

    return False


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


if "__name__" == "__main__":
    canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])  # True
    canConstruct("skateboard",
                 ["bo", "rd", "ate", "t", "ska", "sk", "boar"])  # False
