# from pydantic import BaseModel, Field, field_validator
# from typing import Optional

# class Verse(BaseModel):
#     """
#     Pydantic model for validating verse output.
#     """
#     verse: str = Field(
#         ...,
#         min_length=1,
#         description="A single verse from a song"
#     )

#     @field_validator('verse')
#     def validate_verse(cls, v):
#         """Ensure verse is not empty and is a valid string"""
#         if not v.strip():
#             raise ValueError('Verse cannot be empty or just whitespace')
#         if len(v.strip()) < 10:  # You can adjust this minimum length
#             raise ValueError('Verse seems too short to be valid')
#         return v.strip()

#     class ConfigDict:
#         """Configuration for the model"""
#         json_schema_extra = {
#             "example": {
#                 "verse": "This is an example verse\nWith multiple lines\nOf lyrics"
#             }
#         }

# def validate_verse_output(verse: str) -> str:
#     """
#     Validate the output of get_random_lyrics function.
    
#     Parameters:
#     verse (str): The verse to validate
    
#     Returns:
#     str: The validated verse
    
#     Raises:
#     ValidationError: If validation fails
#     """
#     validated = Verse(verse=verse)
#     return validated.verse