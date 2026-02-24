from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Hash table for O(1) validity checks
        bank_map = {gene: True for gene in bank}

        if endGene not in bank_map:
            return -1

        queue = deque([(startGene, 0)])
        visited = {startGene: True} 

        while queue:
            gene, mutations = queue.popleft()

            if gene == endGene:
                return mutations

            for i in range(len(gene)):
                for char in "ACGT":
                    if char == gene[i]:
                        continue

                    mutated = gene[:i] + char + gene[i+1:]

                    if mutated in bank_map and mutated not in visited:
                        visited[mutated] = True
                        queue.append((mutated, mutations + 1))

        return -1