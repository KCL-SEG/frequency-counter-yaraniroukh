"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items = list(map(str, items)) # convert all list elements to string
    for item in items:
        if not(item in frequencies):
            count = items.count(item)
            frequencies[item] = count
    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
print(frequencies([100, 'Hello', '100', '100', 100]))