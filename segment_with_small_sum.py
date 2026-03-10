n,s = map(int, input().split())
a = list(map(int, input().split()))
 
left = 0
max_len = 0
current_sum = 0
 
for right in range(n):
    current_sum += a[right]
    while current_sum > s:
        current_sum -= a[left]
        left += 1
 
    max_len = max(max_len, right - left + 1)
 
print(max_len)
