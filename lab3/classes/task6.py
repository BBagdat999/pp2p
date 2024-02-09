li = list(map(int, input().split()))
print(list(filter(lambda x: all(map(lambda s: x % s, range(2, x))), li)))