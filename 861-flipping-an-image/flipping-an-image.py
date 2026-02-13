class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
            for i in range(len(image)):
                # reverse row and invert at the same time
                image[i] = [1 - x for x in image[i][::-1]]
            return image