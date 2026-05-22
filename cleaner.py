import string

class Cleanup:
    def clean(self, pathOfFile):
        """Reads a file, removes punctuation, converts to lowercase, and splits into words."""
        # Clean paths if user manually wrapped them in quotes
        nice_path = pathOfFile.strip("'\"")
        try:
            with open(nice_path, 'r', encoding='utf-8') as file:
                result= file.read().lower()
                # Remove punctuation safely
                result= result.translate(str.maketrans('', '', string.punctuation))
                return result.split()
        except FileNotFoundError:
            print(f"\n[Error] The file path '{nice_path}' is not present.")
            return None

    def count_words(self, list):
        if not list:
            return {}
        word_count = {}
        for word in list:
            word_count[word] = word_count.get(word, 0) + 1
        return word_count
