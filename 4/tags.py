import os
import re

from collections import Counter
import urllib.request

# prep
tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    matches = get_tags(content)
    return Counter(matches).most_common(n)


def get_tags(xml_string):
    return re.findall(r'<category>(\w+\s*?\w*?)</category>', content)
