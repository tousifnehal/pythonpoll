invalid_symbols = ['/', '\\', '?', '%', '*', ':', '"', '<', '>', '|', '.', '(', ')', '[', ']', '{', '}']

def contains_invalid_symbol(name):
    for symbol in invalid_symbols:
        if symbol in name:
            return True
    return False