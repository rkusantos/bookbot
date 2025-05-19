import sys
from stats import get_book_text, get_number_text_sorted

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    get_book_text(sys.argv[1])
    sorted_dict = get_number_text_sorted(sys.argv[1])
    for k, v in sorted(sorted_dict.items()):
        if k.isalpha():
            print(f"{k}: {v}")
main()
