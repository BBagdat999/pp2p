def divisible_by_3_and_4(n):
    for i in range(n + 1):
         if i % 3 == 0 and 1 % 4 == 0:
            yield i

n = 100
for num in divisible_by_3_and_4(n):
    print(num)