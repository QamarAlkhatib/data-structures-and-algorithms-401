from collections import Counter

def repeated_word(string):
    
    string = string.replace(',','')
    string = string.lower()
    if len(string) == 0:
        return None

    convert_to_list = list(string.split(" "))
    count_words = Counter(convert_to_list)
    print(count_words)
    for i in convert_to_list:
        if count_words[i] > 1:
            return i