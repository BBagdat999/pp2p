from dictionaries_of_movies import movies

def average_score_by_category(category_name):
    totalScores = 0
    countOfMovies = 0
    for movie in movies:
        if movie['category'] == category_name:
            totalScores += movie['imdb']
            countOfMovies += 1

    return totalScores / countOfMovies

print(average_score_by_category(input()))
