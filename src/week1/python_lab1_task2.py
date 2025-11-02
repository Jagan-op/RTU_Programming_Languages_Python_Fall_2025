"""
Task 2 – Greeting Function with String Manipulation
--------------------------------------------------
Write a function `greet_user(name)` that:
- removes extra spaces with .strip()
- capitalizes the first letter with .capitalize()
- returns "Hello, <Name>! Welcome to Python!"
Ask user for their name and print result.
"""

def greet_user(name):
    """Return a greeting message after cleaning and capitalizing the name."""
    cleaned = name.strip().capitalize()
    return f"Hello, {cleaned}! Welcome to Python!"

if __name__ == "__main__":
    user_name = input("What's your name? ")
    # Optional: handle empty input gracefully
    if user_name.strip() == "":
        print("Hello! Welcome to Python!")
    else:
        print(greet_user(user_name))
