# Dictionary of movies
movies = [
        {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
        {"name": "Hitman", "imdb": 6.3, "category": "Action"},
        {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
        {"name": "The Help", "imdb": 8.0, "category": "Drama"},
        {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
        {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
        {"name": "Love", "imdb": 6.0, "category": "Romance"},
        {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
        {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
        {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
        {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
        {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
        {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
        {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
        {"name": "We Two", "imdb": 7.2, "category": "Romance"}
    ]
#Exercise1----------------------------------------------------
def above_5_5(movie):
    if movie["imdb"] > 5.5:
        return True

movie_name = input("Enter the name of the movie: ")
found_movie = None
for movie in movies:
    if movie["name"] == movie_name:
        found_movie = movie
        break

if above_5_5(found_movie):
    print("TRUE, The IMDB score of",movie_name,"is above 5.5.")
else:
    print("FALSE, The IMDB score of",movie_name,"is not above 5.5.")
#Exercise2----------------------------------------------------
def above_5_5_movies(movies):
    return [movie for movie in movies if above_5_5(movie)]

print(above_5_5_movies(movies))
#Exercise3----------------------------------------------------
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

category = input("Enter the category of the movie: ")
print(movies_by_category(movies,category))
#Exercise4----------------------------------------------------
def average_imdb_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

print(average_imdb_score(movies))
#Exercise5----------------------------------------------------
def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)

category = input("Enter category of movie ")
print(average_imdb_score_by_category(movies,category))