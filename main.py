from stats import get_num_words, count_chars, sorted_char_dict
import sys

def main():

    if len(sys.argv) < 2: # If no pathway to book was provided, return error
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    user_in = sys.argv[1] # user input book pathway
    text = get_book_text(user_in) # store string in text
    num_words = get_num_words(text) # get number of words in text
    char_dict_list = sorted_char_dict(count_chars(text)) # list of dictionaries containing chars and instances
    print_report(user_in, num_words, char_dict_list) # print instances of chars in order


def get_book_text(filepath):
    with open(filepath) as f: # open input filepath
        file_contents = f.read() # store file as string
    return file_contents


def print_report(book_path, num_words, char_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_dict_list:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")




main()