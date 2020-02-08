from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = namedtuple('Game', 'title link')


def get_games():
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    return [game for game in _get_games_iter(FEED_URL)]


def _get_games_iter(url):
    parser = feedparser.parse(url)
    for entry in parser.get('entries', []):
        yield Game(entry.get('title'), entry.get('link'))
