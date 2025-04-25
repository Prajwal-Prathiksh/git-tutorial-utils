"""
This module contains string manipulation functions.
"""


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == reverse_string(s)


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string."""
    return sum(1 for char in s if char.lower() in "aeiou")


def count_consonants(s: str) -> int:
    """Count the number of consonants in a string."""
    return sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")


def count_words(s: str) -> int:
    """Count the number of words in a string."""
    return len(s.split())


# Create a new class CustomString that inherits from str and has memeber functions which call the above functions
class CustomString(str):
    pass


if __name__ == "__main__":
    # Test the functions
    test_string = (
        "Hello world, this is a dummy string to test the string manipulation functions."
    )
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reverse_string(test_string)}")
    print(f"Is palindrome: {is_palindrome(test_string)}")
    print(f"Number of vowels: {count_vowels(test_string)}")
    print(f"Number of consonants: {count_consonants(test_string)}")
    print(f"Number of words: {count_words(test_string)}")
    print("\n")

    # Test the CustomString class
    custom_str = CustomString(
        "Hi there, this is a test string to check the CustomString class."
    )
    # TODO: Print the results of the member functions
