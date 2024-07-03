// https://leetcode.com/problems/the-latest-time-to-catch-a-bus

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        curr = 0
        ans = -1

        for bus in buses:
            cap = 1
            while curr < len(passengers) and cap <= capacity and passengers[curr] <= bus:
                cap += 1
                curr += 1
            ans = bus if cap <= capacity else passengers[curr - 1]
        
        while ans in passengers:
            ans -= 1

        return ans