from dictionaries_of_movies import movies

def filterByCategories(category_name):
    for movie in movies:
        if movie['category'] == category_name:
            print(movie['name'])
        
filterByCategories(input())