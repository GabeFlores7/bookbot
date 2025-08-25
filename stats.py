def get_num_words(text): 
    return len(text.split()) # return number of words in text

def count_chars(text):
    char_dict = {} # initialize char dictionary
    for char in text:
        char = char.lower() # prevent duplicates by converting all chars to lowercase
        if char in char_dict: # update dict value if char exists
            char_dict[char] += 1
        else:
            char_dict[char] = 1 # initialize dict value if char doesn't exist
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_char_dict(input_dict):
    dict_list = []
    for char in input_dict: 
        if char.isalpha():
            dict_list.append({"char":char, "num":input_dict[char]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list