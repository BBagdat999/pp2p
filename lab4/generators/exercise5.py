def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())

print(f"Counting down from {n} to 0:")
for num in countdown(n):
    print(num)