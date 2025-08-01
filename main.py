from stats import count_words, count_characters, sort_characters_dict
import sys


def get_book_text(filepath):
    contents = None
    try:
        with open(filepath) as f:
            contents = f.read()
    except OSError as e:
        print(f"error with opening file: {e}")
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_contents = get_book_text(book_path)

    if book_contents is None:
        return

    words_count = count_words(book_contents)
    characters_count = count_characters(book_contents)
    sorted_characters = sort_characters_dict(characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()
