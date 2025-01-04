def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words_count = count_words(file_contents)
    char_occurence = count_char(file_contents)
    print("---Begin report for books/frankenstein.txt----") 
    print(f"\nThere are {words_count} words in the book") 
    print()
    for char in char_occurence:
        print(f"The char {char} shows up {char_occurence[char]} times")

    print("---End of report---") 
    


def count_words(text):
    words_list = text.split()
    return len(words_list) 






def count_char(text):
    text = text.lower() 
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    count_dict = {}
    for char in chars:
        count_dict[char] = text.count(char)

    return count_dict


if __name__ == "__main__":
    main()
