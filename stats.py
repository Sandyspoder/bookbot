def num_words_func(text):
    return len(text.split())

def num_char_func(text):
    listed = list(text.lower())
    dict = {}
    for char in listed:
        if char in dict:
            dict[char] += 1

        elif char not in dict:
            dict[char] = 1

        
    return dict 