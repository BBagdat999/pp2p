def generate_squares(N):
    for i in range(N):
        yield i ** 2

N = int(input("Enter N: "))
squares_generator = generate_squares(N)

for square in squares_generator:
    print(square)