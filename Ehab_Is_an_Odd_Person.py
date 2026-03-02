n = int(input())
a = list(map(int , input().split()))
 
has_even = False
has_odd = False
 
 
for x in a:
    if x % 2 == 0:
        has_even = True
    else:
        has_odd = True
    # since odd can be get only id even + odd is added 
    if has_odd and has_even:
        break
# sort the araay since we can swap
if has_odd and has_even:
    a.sort()
 
print(" ".join(map(str, a)))
