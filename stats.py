def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_counts(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=sort_on, reverse=True)
    return char_list