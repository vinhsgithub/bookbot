def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    print_report(book_path, num_words, char_count)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_chars(text):
    lowered_text = text.lower()
    unique_chars = set(lowered_text)
    char_count = {}
    for char in unique_chars:
        char_count[char] = lowered_text.count(char)
    return char_count

def print_report(book_path, num_words, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for key in char_count:
        if key.isalpha():
            print(f"The '{key}'character was found {char_count[key]} times")
    print("--- End of report ---")

main()