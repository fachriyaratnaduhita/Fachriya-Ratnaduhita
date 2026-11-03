glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one by one.',
    'dictionary': 'A collection of key-value pairs.',
    'key': 'The first item in a dictionary key-value pair.',
    'value': 'An item associated with a key in a dictionary.',
    'boolean': 'An expression that evaluates to True or False.',
    'tuple': 'An immutable list.',
    'slice': 'A specific group of items in a list.',
}

for word, meaning in glossary.items():
    print(f"\n{word.title()}:\n\t{meaning}")