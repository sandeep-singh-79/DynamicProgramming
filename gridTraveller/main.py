from gridTravellerRecursion import gridTraveller
from gridTravellerRecursionMemo import gridTravellerMemo

if __name__ == "__main__":
    print("===========================================")
    print("Grid Traveller Memoized")
    print("===========================================")
    print("A person can travel a grid of 1,1 in " +
          str(gridTravellerMemo(1, 1)) + " ways")
    print("A person can travel a grid of 2,3 in " +
          str(gridTravellerMemo(2, 3)) + " ways")
    print("A person can travel a grid of 3,2 in " +
          str(gridTravellerMemo(3, 2)) + " ways")
    print("A person can travel a grid of 3,3 in " +
          str(gridTravellerMemo(3, 3)) + " ways")
    print("A person can travel a grid of 18,18 in " +
          str(gridTravellerMemo(18, 18)) + " ways")
    print("===========================================")
    print("Grid Traveller Plain Recursion")
    print("===========================================")
    print("A person can travel a grid of 1,1 in " + str(gridTraveller(1, 1)) +
          " ways")
    print("A person can travel a grid of 2,3 in " + str(gridTraveller(2, 3)) +
          " ways")
    print("A person can travel a grid of 3,2 in " + str(gridTraveller(3, 2)) +
          " ways")
    print("A person can travel a grid of 3,3 in " + str(gridTraveller(3, 3)) +
          " ways")
    print("A person can travel a grid of 18,18 in " +
          str(gridTraveller(18, 18)) + " ways")
