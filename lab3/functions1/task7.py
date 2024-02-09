def has_33(ls):  # list of ints
    for i in range(len(ls) - 1):
        if ls[i] == ls[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#print(has_33(list(map(int, input().split()))))