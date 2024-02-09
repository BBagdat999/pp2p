def histogram(li):
    [print('*'*i, sep='\n') for i in li]
    
histogram(list(map(int, input().split())))