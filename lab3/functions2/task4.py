from dictionaries_of_movies import movies

def average_score_by_list_of_movies(list_of_movies):
    count_of_movies = 0
    total_score = 0
    for name_of_movies in list_of_movies:
        for movie in movies:
            if movie['name'] == name_of_movies:
                total_score += movie['imdb']
                count_of_movies += 1
            
    return total_score / count_of_movies

print(average_score_by_list_of_movies(['Exam', 'We Two']))

'''
movies :
    Hitman, Usual Suspects, Dark Knight, The Choice
'''
