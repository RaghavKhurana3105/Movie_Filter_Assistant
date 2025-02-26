# About

A movie filtering assistant that can filter movies from a database / file through inputs on a CLI, talking filters
such as movie actors, release year, total revenue + other miscellaneous filters that return desired list of movies.

# Content of the files:

## imdb.py
This is the "main" file that you will run via the CLI to see the resulting output to the CLI.

## data folder
The imdb_movies.csv file serves as the primary data source for the Command-Line Interface (CLI) application, enabling users to parse and retrieve movie information based on specified filters. Users can refine their search using the following criteria:

- **Genre:** Filter movies by their genre(s).
- **Actors:** Select films featuring specific actors.
- **Release Year:** Choose movies released in a particular year.
- **Total Revenue:** Filter films based on their box office earnings.

Additionally, the CLI allows users to sort the filtered results in ascending or descending order based on the above parameters. Users can also specify the number of movies to display in the output list, tailoring the results to their preferences.

### Example inputs in CLI
```sh
python imdb.py
python imdb.py --actors "Jennifer Lawrence"
python imdb.py --genres "Fantasy"
python imdb.py --years 2022
python imdb.py --actors "Daniel Radcliffe" "Emma Watson" --genres "Fantasy"
```


