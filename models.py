#models.py

from typing import List
from pydantic import BaseModel

class VowelCountRequest(BaseModel):
    words: List[str]

class SortRequest(BaseModel):
    words: List[str]
    order: str