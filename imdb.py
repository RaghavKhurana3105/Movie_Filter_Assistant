import os.path as path
import csv
import argparse
import sys

SCORE_TTL = "Score"
YEAR_TTL = "Year"
TITLE_TTL = "Title"
ACTORS_TTL = "Actors"


def read(filepath: str) -> list[dict]:
    """
    Returns a list of movies and its information from a fie from an inputted file path, 
    each movie is represented as a dictionary containing information,
    about that specific movie.

    Args:
        Filepath (String): Filepath of csv file

    Returns:
        list[dict]:List of dictionaries, each dictionary represents a 
        movie from the inputted file from the filepath

    """
    movies = []
    with open(filepath, mode='r' , newline='', encoding='utf-8') as movie_csv:
        movie_reader = csv.DictReader(movie_csv)
            
        for row in movie_reader:
            movies.append(row)

    return movies


def enrich_data(movies: list[dict]) -> list[dict]:
    """
    Adds two new fields to each entry of a movie, one for release year and 
    one for list of actors in the movie

    Args:
        movies (list[dict]): Original list of dictionaries containing the movies

    Returns:
        list[dict] : List of dictionaries, where each dictionary is an 
        updated movie entry with an added fields for release year and list of 
        actors in that movie
    """
    add_year(movies)
    add_actor(movies)

    return movies    


def print_movies(data: list[dict]):
    
    print(f'{"Score":<10s} {"Year":<8s} {"Title":<33s} {"Actors":<50s}')
    for movie in data:
        actors = ", ".join(movie["actors"])
        title = movie["names"]

        # limit movie title string to a length of 33 characters according to project description
        if (len(movie["names"]) > 33): 
            title = (movie["names"][:30] + "...")
        else:
            title

        # limit actors string to a length of 50 characters according to project description
        if (len(actors) > 50): 
            actors = (actors[:47] + "...")
        
        

        print(f'{float(movie["score"]):<10.1f} {movie["year"]:<8d} {title:<33s} {actors:<50s}')
    


def add_year(movies: list[dict]) -> list[dict]:
    """
    Adds a new field to each entry of a movie, that represents the 
    year the movie was released.

    Args:
        movies (list[dict]): Original list of dictionaries containing the movies

    Returns:
        list[dict] : List of dictionaries, where each dictionary is an 
        updated movie entry with an added field for the 
        release year of the movie
    """
    for movie in movies:
        year= movie["date_x"][6:10]
        movie["year"] = int(year)
    
    return movies
    


def add_actor(movies: list[dict]) -> list[dict]:
    """
    Adds a  new field to each entry of a movie, that represents all the 
    actors in that specific movie.

    Args:
        movies (list[dict]): Original list of dictionaries containing the movies

    Returns:
        list[dict] : List of dictionaries, where each dictionary is an 
        updated movie entry with an added field for the actors casted 
        in that specific movie
    """

    for movie in movies:
        actors_roles = movie["crew"].split(", ")
        actors = actors_roles[::2]
        movie["actors"] = actors
    
    return movies


def get_filtered_movies(
    movies: list[dict],
    actors: list[str] = None,
    genres: list[str] = None,
    years: list[int] = None,
    top: int = 0,
    sort_by: str = None,
    ascending: bool = False,
) -> list[dict]:
    
    """Takes in the data list and filters the movies based on the
    given parameters

    Args:
        movies (list[dict]): List of all the movies
        actors (list[str]): List of Actors that needs to be in the movies
        genres (list[str]): List of Genres to include in the filter
        years (list[int]): List of years movies were released in
        top (int): How many movies to return
        sort_by (str): What key to sort by, default 'score'
        asc (bool): Sort ascending (e.g. the lowest score is returned first)

    Returns:
        list[dict]: The filtered list of movies
    """
    filtered_movie_list = []

    # Filter by Actors -------------------------

    if actors == None:
        filtered_movie_list = movies
    else:
        for movie in movies:
            if all (actor in movie["actors"] for actor in actors):
                filtered_movie_list.append(movie)

    # ------------------------------------------

    # Filter by Genres -------------------------

    genre_movie_list = []

    if genres == None:
        pass
    else:
        for movie in filtered_movie_list:
            for genre in genres:
                if (genre in movie["genre"]) and (movie not in genre_movie_list):
                    genre_movie_list.append(movie)
    
        filtered_movie_list = genre_movie_list
    # ------------------------------------------

    # Filter by Year(s) -------------------------

    year_movie_list = []

    if years == None:
        pass
    else:
        for movie in filtered_movie_list:
            for year in years:
                if (year == movie["year"]) and (movie not in year_movie_list):
                    year_movie_list.append(movie)
    
        filtered_movie_list = year_movie_list
    
    # ------------------------------------------

    # Sort movies by key + ascending/descending order 

    if sort_by == None:
        pass
    else:
        filtered_movie_list.sort(key=lambda movie: movie[sort_by],reverse=(not ascending))
           
    # -----------------------------------------

    # Number of movies to return ---------------

    if top <= 0 :
        pass
    else:
        filtered_movie_list = filtered_movie_list[0:top]

    # ------------------------------------------

    return filtered_movie_list

def main():
    # path.join() is agnostic to operating system (Windows Vs Linux)
    data = read(path.join("data", "imdb_movies.csv"))

    # -------------------------------------
    # Command line input parser
    # -------------------------------------
    arg_parser = argparse.ArgumentParser(
        prog="Movie filtering and sorting system",
        description="Apply filters and sort your desired list of movies!",
    )
    
    arg_parser.add_argument(
    "--actors", nargs="*",type=str, help="Names of the actors whose movies you would like to see in your list of movies"
    )

    arg_parser.add_argument(
    "--genres", nargs="*", type=str, help="Genres of movies you would like to see in your list of movies"
    )

    arg_parser.add_argument(
    "--years", nargs="*", type=int, default=0, help="Release year(s) of movies you would like to see in your list of movies"
    )

    arg_parser.add_argument(
    "--top",type=int, help="Number of movies you would like to see in you filtered list"
    )

    arg_parser.add_argument(
    "--sort",type=str, help="Sort the desired list by this key"
    )

    arg_parser.add_argument(
    "--ascending",action="store_true", help="If given, return the desired list in ascending order by sort key"
    )

    # -------------------------------------
    args = arg_parser.parse_args()
    # -------------------------------------

    # Add the additional fields to the raw data
    movies = enrich_data(data)

    # Run the filter function
    movies = get_filtered_movies(
        movies,
        args.actors,
        args.genres,
        args.years,
        args.top,
        args.sort,
        args.ascending,
    )
    # And finally print a nice table
    print_movies(movies)


if __name__ == "__main__":
    main()
