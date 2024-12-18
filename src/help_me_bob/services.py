# src/help_me_bob/services.py
import pandas as pd
import random
from pathlib import Path
#from .models import Verse

def load_csv():
    current_dir = Path(__file__).parent
    data_file = current_dir / 'data' / 'clear.csv'
    
    if not data_file.exists():
        raise FileNotFoundError(f"Could not find data file at {data_file}")
    
    return pd.read_csv(data_file)

def get_random_lyrics(df, year=None):
    if year is not None:
        available_years = sorted(df['release_year'].unique())
        
        if year not in available_years:
            closest_year = min(available_years, key=lambda x: abs(x - year))
            filtered_df = df[df['release_year'] == closest_year]
        else:
            filtered_df = df[df['release_year'] == year]
    else:
        filtered_df = df
        
    selected_song = filtered_df.sample(n=1).iloc[0]
    
    # Split into lines
    lines = [line.strip() for line in selected_song['lyrics'].split('\n') if line.strip()]
    
    # Select a random starting point
    start_index = random.randint(0, max(0, len(lines) - 4))
    
    # Get up to 4 consecutive lines
    selected_lines = lines[start_index:start_index + 4]
    
    # Join the lines with newlines
    selected_text = '\n'.join(selected_lines)
    
    # When using pydantic
    #return Verse(verse=selected_text)
    
    return selected_text