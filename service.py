# service.py

def count_vowels(word: str) -> int:
    """
    Count the number of vowels in a given word.

    Args:
    word (str): The word to count vowels in.

    Returns:
    int: The number of vowels in the word.
    """
    return sum(1 for char in word.lower() if char in 'aeiou')