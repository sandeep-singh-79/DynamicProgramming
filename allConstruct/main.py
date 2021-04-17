from allConstruct import allConstruct

if __name__ == "__main__":
    print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False