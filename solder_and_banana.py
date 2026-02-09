k,n,w = map(int, input().split())

total_pay = 0

for i in range(1, w + 1):
    total_pay += k * i

if total_pay > n:
    print(total_pay - n)
else:
    print(0)
