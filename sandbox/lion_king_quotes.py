"""Module to print memorable quotes from The Lion King.

This script defines a fixed list of famous quotes and prints each quote to
standard output when executed. It serves as a simple example of iterating
through a list of strings and displaying each entry.

Attributes
----------
quotes : list[str]
    Memorable quotes from The Lion King that are printed sequentially.
"""

quotes = [
    "Hakuna Matata - it means no worries!",
    "Remember who you are.",
    "The past can hurt. But the way I see it, you can either run from it or learn from it.",
    "I laugh in the face of danger because I have mastered stealth.",
]

for quote in quotes:
    print(quote)
