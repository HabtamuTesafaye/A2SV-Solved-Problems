n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

first = 0
results = []
for second in range(m):
    while first < n and a[first] < b[second]:
        first += 1
    results.append(first)

print(' '.join(map(str, results)))
