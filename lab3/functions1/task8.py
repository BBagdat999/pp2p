def spy_game(nums):
    check = [0, 0, 7]
    i = 0

    for j in range(len(nums)):
        if check[i] == nums[j]:
            i += 1

    print(True if i == 3 else False)

spy_game(list(map(int, input().split())))