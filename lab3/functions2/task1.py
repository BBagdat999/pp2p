from dictionaries_of_movies import movies

def check_to_above_5_5(movie_name):
    for movie in movies:
        if movie_name == movie['name'] and movie['imdb'] > 5.5:
            return True
    return False

print(check_to_above_5_5(input()))