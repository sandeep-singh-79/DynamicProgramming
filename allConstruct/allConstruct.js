const allConstruct = (targetStr, wordBank) => {
    if (targetStr === '') return [[]]

    let finalCombinations = []

    for(let word of wordBank) {
        if (targetStr.indexOf(word) === 0){
            const suffix = targetStr.slice(word.length)
            const suffixWays = allConstruct(suffix, wordBank)
            const targetWays = suffixWays.map(way => [word, ...way])
            finalCombinations.push(...targetWays)
        }
    }

    return finalCombinations
}

const allConstructMemoized = (targetStr, wordBank, memo = {}) => {
    if (targetStr in memo) return memo[targetStr]
    if (targetStr === '') return [[]]

    let finalCombinations = []

    for(let word of wordBank) {
        if (targetStr.indexOf(word) === 0){
            const suffix = targetStr.slice(word.length)
            const suffixWays = allConstructMemoized(suffix, wordBank, memo)
            const targetWays = suffixWays.map(way => [word, ...way])
            finalCombinations.push(...targetWays)
        }
    }

    memo[targetStr] = finalCombinations
    return finalCombinations
}

console.log("----------------------------------")
console.log('all construct memoized')
console.log("----------------------------------")
console.log(allConstructMemoized("purple", ["purp", "p", "ur", "le", "purpl"])) // 2
console.log(allConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // 1
console.log(allConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // 0
console.log(allConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // 4
console.log(allConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // 0
console.log("----------------------------------")
console.log('all construct plain recursion')
console.log("----------------------------------")
console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])) // 2
console.log(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  // 1
console.log(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  // 0
console.log(allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) // 4
console.log(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) // 0