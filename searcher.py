class Search_word:
    def get_word(self, list1, list2, dict1, dict2):
        searched_word= input("Searched for a word: ").strip().lower()
        doc1appearance = dict1.get(searched_word, 0)
        doc2appearance = dict2.get(searched_word, 0)
        print("\n" + "-"*40)
        print(f"Word searched for: '{searched_word}'")
        print(f"'{searched_word}' appeared {doc1appearance} times in essay one.")
        print(f"'{searched_word}' appeared {doc2appearance} times in essay two.")
        print("-"*40)
        # Returns True only if found in both documents per assignment rules
        if searched_word in list1 and searched_word in list2:
            print("Word appeared in both essays")
            return True
        else:
            print("word not appeared in both essays")
            return False
