const countConstruct = (targetStr, wordBank) => {
    if (targetStr.length === 0) return 1

    let totalCount = 0

    for (word of wordBank) {
        if (targetStr.indexOf(word) === 0) {
            const count = countConstruct(targetStr.slice(word.length), wordBank)
            totalCount += count
        }
    }

    return totalCount
}

const countConstructMemoized = (targetStr, wordBank, memo = {}) => {
    if (targetStr in memo) return memo[targetStr]
    if (targetStr.length === 0) return 1

    let totalCount = 0

    for (word of wordBank) {
        if (targetStr.indexOf(word) === 0) {
            const count = countConstructMemoized(targetStr.slice(word.length), wordBank, memo)
            totalCount += count
        }
    }

    memo[targetStr] = totalCount
    return totalCount
}

console.log(countConstructMemoized("purple", ["purp", "p", "ur", "le", "purpl"])) // 2
console.log(countConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // 1
console.log(countConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // 0
console.log(countConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // 4
console.log(countConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // 0
console.log(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) // 2
console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // 1
console.log(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // 0
console.log(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // 4
console.log(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // 0