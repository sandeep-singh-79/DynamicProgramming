from countConstruct import countConstruct
from countConstructMemoized import countConstructMemoized

if __name__ == "__main__":
    print(countConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(countConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(countConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(countConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False
    print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # True
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # False