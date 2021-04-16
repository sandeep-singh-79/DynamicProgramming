import fibLoop
import fibonacciMemo
import fibRecursion

if __name__ == "__main__":
    print("Fibonacci number at location 10: " + str(fibLoop.fibByLoop(10)))
    print("Fibonacci number at location 10: " + str(fibRecursion.fibByRecursion(10)))
    print("Fibonacci number at location 10: " + str(fibonacciMemo.fibByRecursionMemo(10)))