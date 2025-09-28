from stats import count_chars, count_words, sort_char_counts

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    return ""

def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = count_words(book_text)
    print(f'Found {word_count} total words')
    char_dict = count_chars(book_text)
    stats = sort_char_counts(char_dict)
 
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")
    for item in stats:
        if item["char"].isalpha():  # Only print alphabetic characters
            print(f"{item['char']}: {item['num']}")
main()