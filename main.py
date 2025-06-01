import sys
from stats import number_of_words, character_count, sort_by_count

def get_book_txt(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_txt = get_book_txt(path_to_file)
    word_count = number_of_words(book_txt)
    char_count = character_count(book_txt)
    char_list = sort_by_count(char_count)

    # print output
    print(f"Analyzing book found at {path_to_file}")
    print(f"Found {word_count} total words")
    for i in char_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    # print(char_list)

main()
