"""
Main app
"""
from fastapi import FastAPI, HTTPException
from service import count_vowels
from models import VowelCountRequest, SortRequest


app = FastAPI()

@app.get("/")
async def heroku_test():
    return {"howdi!"}

@app.post("/vowel_count")
async def vowel_count(request: VowelCountRequest):
    """
    Count the number of vowels in a given word.

    Args:
    word (str): The word to count vowels in.

    Returns:
    int: The number of vowels in the a given word.
    """
    word_counts = {word: count_vowels(word) for word in request.words}
    return word_counts

@app.post("/sort")
async def sort_words(request: SortRequest):
    """
    Sort list of words

    Args:
    List of words to count.

    Returns:
    list of words in specified words.
    """
    if request.order not in {"asc", "desc"}:
        raise HTTPException(status_code=400, detail="Invalid order parameter")
    sorted_words = sorted(request.words, reverse=request.order == "desc")
    return sorted_words
