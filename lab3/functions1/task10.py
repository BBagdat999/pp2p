def filter_unique(initial_list):
    newlist = []
    for x in initial_list:
        if x not in newlist:
            newlist.append(x)
    print(newlist) 
    
filter_unique(list(map(str, input().split()))) 