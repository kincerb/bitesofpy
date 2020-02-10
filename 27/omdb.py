import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""
    movie_dicts = []
    for file in files:
        movie_dicts.append(json.loads(file.read_text()))
    return movie_dicts


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    for movie in movies:
        if 'Comedy' in movie.get('Genre'):
            return movie.get('Title')


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    max_votes = 0
    most_votes_movie = None
    for movie in movies:
        movie_votes = int(movie.get('imdbVotes').replace(',', ''))
        if movie_votes > max_votes:
            most_votes_movie = movie
            max_votes = movie_votes
    return most_votes_movie.get('Title')


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    max_runtime = 0
    longest_movie = None
    for movie in movies:
        movie_runtime = int(movie.get('Runtime').split()[0])
        if movie_runtime > max_runtime:
            longest_movie = movie
            max_runtime = movie_runtime
    return longest_movie.get('Title')
