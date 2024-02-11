class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedPos = sorted([(s, p) for s, p in zip(speed, position)], key=itemgetter(1))
        # Reduction from sorting

        prevTime = float("-inf")
        fleets = 0

        # Realized that number of fleets == number of fleet leaders
        for i in range(len(speedPos) - 1, -1, -1):
            currTime = (target - speedPos[i][1]) / speedPos[i][0]
            # Check the condition that indicates a fleet leader
            if prevTime < currTime:
                # Incremented counter whenever we found a fleet leader
                prevTime = currTime
                fleets += 1
        return fleets

# Two types of cars:
    # Fleet leaders
    # Fleet followers

# Number of fleets is equal to the number of fleet leaders

"""
    Fleet leaders only exist if the time it takes car i to
    reach target exceeds the time it takes the previous fleet leader
    to reach target.
"""