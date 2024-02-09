def filter_prime(numbers): # list of ints
    for x in range(len(numbers)):
        for div in range(2, numbers[x]): 
            if  numbers[x] % div == 0:
                numbers[x] = 0
    return [x for x in numbers if x != 0] 

print(*filter_prime(list(map(int, input().split()))))