class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = []
        for i in range(1, n + 1):
            circle.append(i)

        current_index = 0

        while len(circle) > 1:
            # the kth person to be remvoed
            current_index = (current_index + k- 1) % len(circle)
            circle.pop(current_index)

        return  circle[0]