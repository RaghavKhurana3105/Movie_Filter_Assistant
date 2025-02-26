# About

A movie filtering assistant that can filter movies from a database / file through inputs on a CLI, talking filters
such as movie actors, release year, total revenue + other miscellaneous filters that return desired list of movies.

# Content of the files:

## imdb.py

### Key Features:

**Data Reading and Enrichment:** The script reads movie data from a specified CSV file and enriches it by extracting additional information, such as the release year and a list of actors for each movie.

**Filtering Options: Users can filter movies based on:**

- **Genre:** Filter movies by their genre(s).
- **Actors:** Select films featuring specific actors.
- **Release Year:** Choose movies released in a particular year.
- **Total Revenue:** Filter films based on their box office earnings.

**Sorting and Limiting Results:** The script allows sorting the filtered list by various attributes, such as score or year, in ascending or descending order. Additionally, users can specify the number of top results to display.

**Command-Line Arguments:** The script utilizes the argparse module to handle command-line arguments, enabling users to specify their filtering and sorting preferences directly from the terminal.

## data folder
The imdb_movies.csv file serves as the primary data source for the Command-Line Interface (CLI) application, enabling users to parse and retrieve movie information based on specified filters. Users can refine their search using the following criteria:

Additionally, the CLI allows users to sort the filtered results in ascending or descending order based on the above parameters. Users can also specify the number of movies to display in the output list, tailoring the results to their preferences.

# Example inputs in CLI
```sh
python imdb.py
python imdb.py --actors "Salman Khan"
python imdb.py --genres "Comedy"
python imdb.py --years 2012
python imdb.py --actors "Daniel Radcliffe" "Emma Watson" --genres "Fantasy"
```


