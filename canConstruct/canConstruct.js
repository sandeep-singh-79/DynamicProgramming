const canConstruct = (targetStr, wordBank) => {
    if (targetStr.length === 0) return true

    for (word of wordBank)
        if(targetStr.indexOf(word) === 0) 
            if(canConstruct(targetStr.slice(word.length), wordBank) === true)
                return true

    return false
}

const canConstructMemoized = (targetStr, wordBank, memo={}) => {
    if(targetStr in memo) return memo[targetStr]
    if (targetStr.length === 0) return true

    for (word of wordBank)
        if(targetStr.indexOf(word) === 0)
            if(canConstructMemoized(targetStr.slice(word.length), wordBank, memo) === true){
                memo[targetStr] = true
                return true
            }
        }
    
    memo[targetStr] = false
    return false
}

console.log(canConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // True
console.log(canConstructMemoized("skateboard",
                 ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // False
console.log(canConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // True
console.log(canConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // False
console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // True
console.log(canConstruct("skateboard",
                 ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // False
console.log(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // True
console.log(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // False