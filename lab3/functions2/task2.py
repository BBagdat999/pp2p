from dictionaries_of_movies import movies

def list_above_5_5():
    sublist = []
    for movie in movies:
        if movie['imdb'] > 5.5:
            sublist.append(movie['name'])

    return sublist

print(list_above_5_5())