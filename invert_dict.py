def invert_dict(dict1):
    """
    Inverts a dictionary, turning each of the list items into
    separate keys in the inverted dictionary.

    Args:
        dict1: A dictionary to be inverted.

    Returns:
        An inverted dictionary, with the keys and values swapped.
    """

    inverted_dict = {}
    for key, value in dict1.items():
        for item in value:
            inverted_dict.setdefault(item, []).append(key)
    return inverted_dict


# Sample input dictionary
dict1 = {
    'Stud1': ['CS1101', 'CS2402', 'CS2001'],
    'Stud2': ['CS2402', 'CS2001', 'CS1102']
}

# Invert the dictionary
inverted_dict = invert_dict(dict1)

# Print the original dictionary
print('Original dictionary:')
print(dict1)

# Print the inverted dictionary
print('Inverted dictionary:')
print(inverted_dict)
