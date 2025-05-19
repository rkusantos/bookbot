from collections import Counter

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        count_of_words = len(file_contents.lower().split())
        

        print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {filepath}
        ----------- Word Count ----------
        Found {count_of_words} total words
        --------- Character Count -------
        """)

def get_number_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        word_list = file_contents.lower()
        character_list = list(word_list)
        character_count = Counter(character_list)

        print(character_count)

def get_number_text_sorted(filepath):

    with open(filepath) as f:
        file_contents = f.read()
        word_list = file_contents.lower()
        character_list = list(word_list)
        character_count = Counter(character_list)

        return character_count
