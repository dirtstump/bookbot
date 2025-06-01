def number_of_words(full_string):
    return len(full_string.split())

def character_count(full_string):
    char_count = {}
    for i in full_string.lower():
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def sort_by_count(char_dict):
    return_list = []
    for i in char_dict:
        return_list.append({"char": i, "num": char_dict[i]})
    return_list.sort(reverse=True, key=sort_on)
    return return_list

def sort_on(dict):
    return dict["num"]
