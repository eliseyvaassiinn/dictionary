import json
from pathlib import Path

FILE_NAME = Path("dictionary.json")


def load_dictionary():
    if not FILE_NAME.exists():
        return {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

            if isinstance(data, dict):
                return data

            print("Warning: dictionary file has an invalid format.")
            return {}

    except (json.JSONDecodeError, OSError):
        print("Warning: could not read dictionary file.")
        return {}


def save_dictionary(dictionary):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                dictionary,
                file,
                ensure_ascii=False,
                indent=4
            )
        return True

    except OSError:
        print("Error: could not save dictionary.")
        return False


def print_line():
    print("-" * 50)


def pause():
    input("\nPress Enter to continue...")


def add_word(dictionary):
    print("\nADD NEW WORD")
    print_line()

    english = input("English word: ").strip().lower()
    if not english:
        print("Word cannot be empty.")
        return

    if english in dictionary:
        print("This word already exists.")
        print(f"Current translation: {dictionary[english]}")

        choice = input("Replace translation? (y/n): ").strip().lower()

        if choice != "y":
            print("Operation cancelled.")
            return

    french = input("French translation: ").strip()

    if not french:
        print("Translation cannot be empty.")
        return

    dictionary[english] = french

    if save_dictionary(dictionary):
        print(f"\n'{english}' was successfully added!")


def search_word(dictionary):
    print("\nSEARCH WORD")
    print_line()

    query = input("Enter an English word or part of it: ").strip().lower()

    if not query:
        print("Search query cannot be empty.")
        return

    results = {
        english: french
        for english, french in dictionary.items()
        if query in english.lower()
    }

    if not results:
        print("No matching words found.")
        return

    print(f"\nFound {len(results)} result(s):")
    print_line()

    for english, french in sorted(results.items()):
        print(f"{english:<25} -> {french}")


def show_dictionary(dictionary):
    print("\nFULL DICTIONARY")
    print_line()

    if not dictionary:
        print("The dictionary is empty.")
        return

    words = sorted(dictionary.items())

    print(f"Total words: {len(words)}\n")

    for number, (english, french) in enumerate(words, start=1):
        print(f"{number:>3}. {english:<25} -> {french}")


def delete_word(dictionary):
    print("\nDELETE WORD")
    print_line()

    english = input("Enter the English word to delete: ").strip().lower()

    if english not in dictionary:
        print("Word not found.")
        return

    print(f"\nWord: {english}")
    print(f"Translation: {dictionary[english]}")

    confirmation = input("\nAre you sure you want to delete it? (y/n): ")
    if confirmation.strip().lower() != "y":
        print("Deletion cancelled.")
        return

    del dictionary[english]

    if save_dictionary(dictionary):
        print("Word successfully deleted.")


def edit_word(dictionary):
    print("\nEDIT TRANSLATION")
    print_line()

    english = input("Enter the English word: ").strip().lower()

    if english not in dictionary:
        print("Word not found.")
        return

    print(f"\nEnglish: {english}")
    print(f"Old translation: {dictionary[english]}")

    new_translation = input("New French translation: ").strip()

    if not new_translation:
        print("Translation cannot be empty.")
        return

    dictionary[english] = new_translation

    if save_dictionary(dictionary):
        print("Translation successfully updated.")


def show_statistics(dictionary):
    print("\nDICTIONARY STATISTICS")
    print_line()

    print(f"Total words: {len(dictionary)}")

    if dictionary:
        longest_word = max(dictionary, key=len)
        shortest_word = min(dictionary, key=len)

        print(f"Longest English word: {longest_word}")
        print(f"Shortest English word: {shortest_word}")


def main():
    dictionary = load_dictionary()

    while True:
        print("\n")
        print("=" * 50)
        print("       ENGLISH - FRENCH DICTIONARY")
        print("=" * 50)
        print(f"Words in dictionary: {len(dictionary)}")
        print_line()

        print("1. Add a new word")
        print("2. Search for a word")
        print("3. Show all words")
        print("4. Edit translation")
        print("5. Delete a word")
        print("6. Dictionary statistics")
        print("0. Exit")

        print_line()

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_word(dictionary)
            pause()

        elif choice == "2":
            search_word(dictionary)
            pause()

        elif choice == "3":
            show_dictionary(dictionary)
            pause()

        elif choice == "4":
            edit_word(dictionary)
            pause()

        elif choice == "5":
            delete_word(dictionary)
            pause()

        elif choice == "6":
            show_statistics(dictionary)
            pause()

        elif choice == "0":
            print("\nDictionary saved. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select an option from the menu.")
            pause()


if __name__ == "__main__":
    main()