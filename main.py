def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")

    sorted_dict = dict(sorted(chars_dict.items(), key=get_value, reverse=True))
    for key in sorted_dict.keys():
        if str(key).isalpha():
            print(f"The {key} character was found {sorted_dict[key]} times")

    print(chars_dict)

def get_value(item):
    return item[1]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()