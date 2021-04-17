from fibLoop import fibByLoop
from fibRecursion import fibByRecursion
import fibDPTabulation
from fibonacciMemo import fibByRecursionMemo

if __name__ == "__main__":
    position = 50
    print("Fibonacci number at position %d: %d" % (position, fibByLoop(position)))
    print("Fibonacci number at position %d: %d" % (position, fibByRecursionMemo(position)))
    print("Fibonacci number at position %d: %d" % (position, fibDPTabulation.fibDPTabulation(position)))
    print("Fibonacci number at position %d: %d" % (position, fibDPTabulation.fibDPTab(position)))
    print("Fibonacci number at position %d: %d" % (position, fibByRecursion(position)))