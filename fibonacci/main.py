from fibLoop import fibByLoop
from fibRecursion import fibByRecursion
from fibDPTabulation import fibDPTabulation
from fibonacciMemo import fibByRecursionMemo

if __name__ == "__main__":
    position = 0
    print("Fibonacci number at position %d: %d" % (position, fibByLoop(position)))
    print("Fibonacci number at position %d: %d" % (position, fibByRecursionMemo(position)))
    print("Fibonacci number at position %d: %d" % (position, fibDPTabulation(position)))
    print("Fibonacci number at position %d: %d" % (position, fibByRecursion(position)))