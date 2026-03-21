class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n + 1)]

        for first, last, seats in bookings:
            diff[first - 1] += seats      
            if last < n:
                diff[last] -= seats       

        # Build answer via prefix sum
        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff[:n]