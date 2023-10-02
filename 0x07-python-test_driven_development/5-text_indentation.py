#!/usr/bin/python3

"""Prints a text with 2 new lines after each of these characters: ., ? and :"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input string.

    Raises:
        TypeError: If text is not a string.
    """

    if type(text) != str:
        raise TypeError("text must be a string")

    for char in ".:?":
        text = text.replace(char, char + "\n\n")

    for line in text.split("\n"):
        print(line.strip())
