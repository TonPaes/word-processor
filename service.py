# service.py

def count_vowels(word: str) -> int:
    return sum(1 for char in word.lower() if char in 'aeiou')
