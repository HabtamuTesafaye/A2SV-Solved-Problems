n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = []
first, second = 0, 0

while first < n and second < m:
    if a[first] < b[second]:
        result.append(a[first])
        first += 1
    else:
        result.append(b[second])
        second += 1

while first < n:
    result.append(a[first])
    first += 1

while second < m:
    result.append(b[second])
    second += 1

print(' '.join(map(str, result)))
