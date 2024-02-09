def solve(numheads, numlegs):
    for chickens in range(1, numheads):
            for rabbits in range(1, numheads):
                  if(rabbits * 1 + chickens * 1 == numheads) and (chickens*2 + rabbits*4 == numlegs):  
                         print(f'number of rabbits = {rabbits} {'\n'}number of chickens = {chickens}')
                         return 0
    print('it is impossible to solve')


solve(int(input('enter a number of heads: ')), int(input('enter a number of legs: ')))
