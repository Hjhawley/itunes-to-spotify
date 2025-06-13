import re

def clean_track(title: str) -> str:
    # Cleans a song title by removing special characters for improved matching.
    return re.sub(r'\(.*\)|[\'’]|[\/\-]', ' ', title).strip()

def clean_artist(artist_name: str) -> str:
    # Cleans up artist's name for improved matching.
    if artist_name == ("The The"): # annoying edge case
        return artist_name
    return artist_name.replace('The ', '').replace('&', 'and')