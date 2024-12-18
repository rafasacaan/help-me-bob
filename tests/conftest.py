# tests/conftest.py
import pytest
import pandas as pd

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing"""
    return pd.DataFrame({
        'release_year': [1999, 2000, 2001],
        'album': ['Album1', 'Album2', 'Album3'],
        'title': ['Song1', 'Song2', 'Song3'],
        'lyrics': [
            'Verse 1\nLine 2\n\nVerse 2\nLine 2',
            'Test verse 1\nLine 2\n\nTest verse 2\nLine 2',
            'Sample verse 1\nLine 2\n\nSample verse 2\nLine 2'
        ]
    })

# tests/test_models.py
import pytest
from help_me_bob.models import Verse
from pydantic import ValidationError

def test_valid_verse():
    verse = "This is a valid verse\nWith multiple lines"
    verse_obj = Verse(verse=verse)
    assert verse_obj.verse == verse.strip()

def test_empty_verse():
    with pytest.raises(ValidationError):
        Verse(verse="")

def test_whitespace_verse():
    with pytest.raises(ValidationError):
        Verse(verse="   \n   ")

def test_too_short_verse():
    with pytest.raises(ValidationError):
        Verse(verse="too short")

# tests/test_services.py
import pytest
from help_me_bob.services import get_random_lyrics

def test_get_random_lyrics_no_year(sample_df):
    result = get_random_lyrics(sample_df)
    assert isinstance(result, Verse)
    assert len(result.verse) > 0

def test_get_random_lyrics_with_year(sample_df):
    result = get_random_lyrics(sample_df, year=1999)
    assert isinstance(result, Verse)
    assert len(result.verse) > 0

def test_get_random_lyrics_closest_year(sample_df):
    # Test with a year that doesn't exist
    result = get_random_lyrics(sample_df, year=1998)
    assert isinstance(result, Verse)
    assert len(result.verse) > 0

# pyproject.toml additions for pytest configuration
"""
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
"""