import cleaner
import searcher
import checker

def main():
   
        
        doc1="essay-1.txt"
        doc2="essay-2.txt"   
               
        cleaner_instance = cleaner.Cleanup()
        doc1_list = cleaner_instance.clean(doc1)
        doc2_list = cleaner_instance.clean(doc2)
            
        doc1_set = set(doc1_list)
        doc2_set = set(doc2_list)
        
        common_words = doc1_set.intersection(doc2_set)
        unique_words = doc1_set.union(doc2_set)

        no_of_common_words = len(common_words)
        no_of_unique_words = len(unique_words)

        doc1_dict = cleaner_instance.count_words(doc1_list)
        doc2_dict = cleaner_instance.count_words(doc2_list)
        
        # Menu Loop
        while True :
            print("="*100)
            print(" WELCOME TO THE FORTUNATE PLAGIARISM CHECKER ")
            print("="*100)
            print("="*60)
            print(" MAIN MENU ")
            print("="*60)
            print("1. Look out for a word")
            print("2. Get plagiarism results")
            print("3. Close program ")
            
            try:
                option = int(input("Choose an option (1-3): "))
            except ValueError:
                print("Please enter numbers only.")
                continue

            if option== 1:
                searcher_instance = searcher.Search_word()
                searcher_instance.get_word(doc1_list, doc2_list, doc1_dict, doc2_dict)
                            
            elif option == 2:
               print(" List Of Common words ")
               print(f"{list(common_words)[:15]}...\n")
                
               for word in common_words:
                    doc1_appearance = doc1_dict.get(word, 0)
                    doc2_appearance = doc2_dict.get(word, 0)
                    print(f"'{word}' appeared {doc1_appearance} times in essay1, {doc2_appearance} times in essay2")
               print()
                
               checker_instance = checker.Checker()
               checker_instance.plagiarism_calculation(no_of_common_words, no_of_unique_words)
                
            elif option == 3:
                print("\nClosing Now\n Take care.")
                break
            else:
                print("Incorrect choice (1, 2, or 3)")

if __name__ == "__main__":
    main()
