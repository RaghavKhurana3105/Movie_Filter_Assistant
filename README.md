# About

A movie filtering assistant that can filter movies from a database / file through inputs on a CLI, talking filters
such as movie actors, release year, total revenue + other miscellaneous filters that return desired list of movies.

# Content of the files:

## imdb.py
This is the "main" file that you will run to see the resulting output to the terminal.

### Example inputs in CLI
```sh
python imdb.py
python imdb.py --actors "Jennifer Lawrence"
python imdb.py --genres "Fantasy"
python imdb.py --years 2022
python imdb.py --actors "Daniel Radcliffe" "Emma Watson" --genres "Fantasy"
```

## data
Contains a `imdb_movies.csv` file that contains all the data that the CLI Interface can parse and return depending on the filters added by the user. The user can apply the following filters: 

- Genre of films
- Actors of the films
- Release year of movies

Moreover, the user can sort the filtered lists in ascending/ descending order using the above parameters and also set a desired number of movies which must be returned in the output list.

