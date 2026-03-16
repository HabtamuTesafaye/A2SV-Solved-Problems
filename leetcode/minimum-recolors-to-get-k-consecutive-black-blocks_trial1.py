class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Count W's in the first window
        white_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_count = white_count + 1

        # Step 2: Save this as the minimum
        min_ops = white_count

        # Slide the window across the rest of the string
        for i in range(k, len(blocks)):
            # Add incoming character, remove outgoing character
            if blocks[i] == 'W':
                white_count += 1
            if blocks[i - k] == 'W':
                white_count -= 1
            
            min_ops = min(min_ops, white_count)

        return min_ops