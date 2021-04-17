const bestSum = (sum, arr) => {
    if (sum === 0) return []
    if (sum < 0) return null

    let shortestCombination = null

    for (let item of arr) {
        const remainder = sum - item;
        const remainderCombination = bestSum(remainder, arr)
        if (remainderCombination !== null){
            const combination = [...remainderCombination, item]
            if (shortestCombination === null || (combination.length < shortestCombination.length)) {
                shortestCombination = combination
            }
        }
    }

    return shortestCombination
}

const bestSumMemoized = (sum, arr, memo={}) => {
    if (sum in memo) return memo[sum]
    if (sum === 0) return []
    if (sum < 0) return null

    let shortestCombination = null

    for (let item of arr) {
        const remainder = sum - item;
        const remainderCombination = bestSumMemoized(remainder, arr, memo)
        if (remainderCombination !== null){
            const combination = [...remainderCombination, item]
            if (shortestCombination === null || (combination.length < shortestCombination.length)) {
                shortestCombination = combination
            }
        }
    }

    memo[sum] = shortestCombination
    return shortestCombination
}

console.log(bestSumMemoized(7, [5,3,4,7])) // [7]
console.log(bestSumMemoized(7, [2,3,5])) // [3,5]
console.log(bestSumMemoized(8, [1,4,5])) // [4,4]
console.log(bestSumMemoized(100, [1,2,5,25])) // [25, 25, 25, 25]
console.log(bestSum(7, [5,3,4,7])) // [7]
console.log(bestSum(7, [2,3,5])) // [3,5]
console.log(bestSum(8, [1,4,5])) // [4,4]
console.log(bestSum(100, [1,2,5,25])) // [25, 25, 25, 25]