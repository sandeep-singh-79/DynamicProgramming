from countConstruct import countConstruct
from countConstructMemoized import countConstructMemoized

if __name__ == "__main__":
    print(countConstructMemoized("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
    print(countConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(countConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(countConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(countConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False
    print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) # 2
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # 0
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # 4
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # 0