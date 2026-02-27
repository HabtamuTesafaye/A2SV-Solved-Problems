n, k = map(int, input().split())
a = list(map(int, input().split()))
 
# Sort the array so we can find the k-th smallest element easily
a.sort()
 
answer = -1
 
# When k == 0: choose a number smaller than the minimum element so that 0 elements are <= x
if k == 0:
    if a[0] > 1:
        answer = a[0] - 1
    else:
        answer = -1
 
# When k == n: choose the maximum element so that all elements are <= x
elif k == n:
    answer = a[n - 1]
 
# When 0 < k < n: choose x such that a[k-1] <= x < a[k]
else:
    if a[k - 1] != a[k]:
        answer = a[k] - 1
    else:
        answer = -1
 
print(answer)
