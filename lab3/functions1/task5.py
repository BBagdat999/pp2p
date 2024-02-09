from itertools import permutations

def permutation(string):
    # for x in permutations(string):
    #     print("".join(x))
    return (''.join(x) for x in permutations(string))

print(*list(permutation(input())))