from canConstruct import canConstruct
from canConstructMemoized import canConstructMemoized

if __name__ == "__main__":
    print(canConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(canConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False