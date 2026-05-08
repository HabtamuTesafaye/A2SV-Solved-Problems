class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        mx = max(nums)

        # smallest prime factor sieve
        spf = list(range(mx + 1))
        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = set()
            while x > 1:
                p = spf[x]
                factors.add(p)
                while x % p == 0:
                    x //= p
            return factors

        def is_prime(x):
            return x > 1 and spf[x] == x

        # map prime factor -> indices divisible by it
        factor_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            for p in get_factors(val):
                factor_to_indices[p].append(i)

        q = deque([(0, 0)])  # index, distance
        visited = [False] * n
        visited[0] = True
        used_prime = set()

        while q:
            i, dist = q.popleft()

            if i == n - 1:
                return dist

            # adjacent moves
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, dist + 1))

            # teleport
            val = nums[i]
            if is_prime(val) and val not in used_prime:
                used_prime.add(val)
                for nxt in factor_to_indices[val]:
                    if not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt, dist + 1))

        return -1