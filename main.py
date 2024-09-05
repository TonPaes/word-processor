from fastapi import FastAPI, HTTPException
from service import count_vowels
from models import VowelCountRequest, SortRequest

app = FastAPI()

@app.post("/vowel_count")
async def vowel_count(request: VowelCountRequest):
    word_counts = {word: count_vowels(word) for word in request.words}
    return word_counts

@app.post("/sort")
async def sort_words(request: SortRequest):
    if request.order not in {"asc", "desc"}:
        raise HTTPException(status_code=400, detail="Invalid order parameter")
    sorted_words = sorted(request.words, reverse=request.order == "desc")
    return sorted_words