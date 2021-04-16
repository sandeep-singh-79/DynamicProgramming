const canSum = (sum, arr) => {
    if (sum === 0) return true
    if (sum < 0) return false

    for (let i of arr) {
        const remainder = sum - i
        if (canSum(remainder, arr) === true) return true
    }

    return false
}

const canSumMemoized = (sum, arr, memo={}) => {
    if(sum in memo) return memo[sum]
    if (sum === 0) return true
    if (sum < 0) return false

    for (let i of arr) {
        const remainder = sum - i
        if (canSum(remainder, arr, memo) === true){
            memo[sum] = true
            return true
        }
    }

    memo[sum] = false
    return false
}

console.log("==========================")
console.log("Can Sum for provided inputs with DP")
console.log("==========================")
console.log(canSumMemoized(7, [2, 3])) // true
console.log(canSumMemoized(7, [5, 3, 4, 7])) // true
console.log(canSumMemoized(7, [2, 4])) // false
console.log(canSumMemoized(8, [2, 3, 5])) // true
console.log(canSumMemoized(300, [7, 14])) // false
console.log("==========================")
console.log("Can Sum for provided inputs with recursion")
console.log("==========================")
console.log(canSum(7, [2, 3])) // true
console.log(canSum(7, [5, 3, 4, 7])) // true
console.log(canSum(7, [2, 4])) // false
console.log(canSum(8, [2, 3, 5])) // true
console.log(canSum(300, [7, 14])) // false