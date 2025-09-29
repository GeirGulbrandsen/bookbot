from stats import count_chars, count_words, sort_char_counts
import sys

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    return ""

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
    path = sys.argv[1]

    book_text = get_book_text(path)
    word_count = count_words(book_text)
    print(f'Found {word_count} total words')
    char_dict = count_chars(book_text)
    stats = sort_char_counts(char_dict)
 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for item in stats:
        if item["char"].isalpha():  # Only print alphabetic characters
            print(f"{item['char']}: {item['num']}")
main()