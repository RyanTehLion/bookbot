def main():
    book_path = "books/frankenstein.txt"

    with open(book_path) as f:
        file_contents = f.read()
        lowered_contents = file_contents.lower()
        words_split_string = lowered_contents.split()
        entire_count = char_count(words_split_string)
        ordered_results = sorted_list(entire_count)
        alphabet_results = alphabet_list(ordered_results)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(words_split_string)} words found in the document" "\n" "\n")
    for report in alphabet_results:
        print(f"The '{report[0]}' character was found {report[1]} times")
    print("--- End report ---")

def word_count(words_split_string):
    words = 0
    for i in words_split_string:
        words += 1
    return words

def char_count(words_split_string):
    letter_count_dict = {}
    for i in words_split_string:
        for char in i:
            if char in letter_count_dict:
                letter_count_dict[char] += 1
            else:
                letter_count_dict.setdefault(char, 1)

    return letter_count_dict

def sorted_list(entire_count):
    pairs_list = entire_count.items()
    Descending_list = sorted(pairs_list,key= lambda d : d[1], reverse=True)
    
    return Descending_list

def alphabet_list(ordered_results):
    letters_only = []
    for key in ordered_results:
        if key[0].isalpha():
            letters_only.append(key)

    return letters_only    



main()
