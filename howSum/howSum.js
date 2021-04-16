const howSum = (sum, arr) => {
    if(sum === 0) return []
    if(sum < 0) return null

    for(let num of arr) {
        const remainder = sum - num
        let itemsForSum = howSum(remainder, arr)
        if(itemsForSum !== null) {
            return [...itemsForSum, num]
        }
    }

    return null;
}

const howSumMemoized = (sum, arr, memo = {}) => {
    if(sum in memo) return memo[sum]
    if(sum === 0) return []
    if(sum < 0) return null

    for(let num of arr) {
        const itemsForSum = howSumMemoized((sum - num), arr, memo)
        if(itemsForSum !== null) {
            memo[sum] = [...itemsForSum, num]
            return memo[sum]
        }
    }

    memo[sum] = null
    return null;
}

console.log("========================")
console.log("How Sum Memoization")
console.log("========================")
console.log(howSumMemoized(7, [2, 3])) // [3, 2, 2]
console.log(howSumMemoized(7, [5, 3, 4, 7])) // [4, 3]
console.log(howSumMemoized(7, [2, 4])) // null
console.log(howSumMemoized(8, [2, 3, 5])) // [2, 2, 2, 2]
console.log(howSumMemoized(8, [3, 5, 2])) // [2, 3, 3]
console.log(howSumMemoized(300, [7, 14])) // null
console.log("========================")
console.log("How Sum plain recursion")
console.log("========================")
console.log(howSum(7, [2, 3])) // [3, 2, 2]
console.log(howSum(7, [5, 3, 4, 7])) // [4, 3]
console.log(howSum(7, [2, 4])) // null
console.log(howSum(8, [2, 3, 5])) // [2, 2, 2, 2]
console.log(howSum(8, [3, 5, 2])) // [2, 3, 3]
console.log(howSum(300, [7, 14]))