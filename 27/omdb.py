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
            return movie


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    votes = 0
    most_votes = None
    for movie in movies:
        if int(movie.get('imdbVotes')) > votes:
            most_votes = movie
    return most_votes


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    max_runtime = 0
    longest_movie = None
    for movie in movies:
        if int(movie.get('Runtime').split()[0]) > max_runtime:
            longest_movie = movie
    return longest_movie
