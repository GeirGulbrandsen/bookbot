from stats import count_words

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    return ""

def main():
    book_text = get_book_text('books/frankenstein.txt')
    word_count = count_words(book_text)
    print(f'Found {word_count} total words')
 
main()