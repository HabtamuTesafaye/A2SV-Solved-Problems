class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {res: i for i, res in enumerate(list1)}
        sums = defaultdict(list)
        
        for j, res in enumerate(list2):
            if res in index_map:
                sums[index_map[res] + j].append(res)
                
        # Return the list associated with the smallest key (index sum)
        return sums[min(sums.keys())]