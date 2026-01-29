import sys

n = int(input())

phoneBook = {}
for _ in range(n):
    name, phone = input().split()
    phoneBook[name] = phone

for query in sys.stdin:
    query = query.strip()
    
    if query in phoneBook:
        print(f"{query}={phoneBook[query]}")
    else:
        print("Not found")
