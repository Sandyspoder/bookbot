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

def sort_char_dict(dict):

    def sort_on(items):
        return items["num"]

    char_list = []
    for i in dict:
        if i.isalpha():
            char_list.append({"char":i, "num":dict[i]})
        

    char_list.sort(reverse=True, key=sort_on)
        
    return char_list 