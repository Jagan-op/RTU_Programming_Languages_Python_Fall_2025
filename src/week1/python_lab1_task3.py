"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    length = len(text)
    words = text.split()
    word_count = len(words)
    has_python = "python" in text.lower()
    return (length, word_count, has_python)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    length, word_count, has_python = analyze_sentence(sentence)
    print(f"Characters: {length}")
    print(f"Words: {word_count}")
    print(f"Contains 'Python': {'Yes' if has_python else 'No'}")
