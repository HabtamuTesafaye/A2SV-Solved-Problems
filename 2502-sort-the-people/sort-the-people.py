class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        for i in range(1, len(people)):
            key = people[i]
            j = i - 1

            # Compare by height (index 1) in descending order
            while j >= 0 and people[j][1] < key[1]:
                people[j + 1] = people[j]
                j -= 1
                
            people[j + 1] = key

        return [name for name, height in people]