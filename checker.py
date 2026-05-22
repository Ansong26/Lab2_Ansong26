class Checker:
    def plagiarism_calculation(self, no_of_common_words, no_of_unique_words):
        if no_of_common_words == 0:
            plagiarism_value = 0.0
        else:
            plagiarism_value = (no_of_common_words / no_of_unique_words) * 100
        
        print("="*60)
        print(" PLAGIARISM DETECTION ")
        print("="*60)
        print(f"Plagiarism level: {plagiarism_value:.2f} %")  
        
        if plagiarism_value >= 50:
            print("\nThere is plagiarism registered\n")
        else:
            print("\nNo plagiarism registered\n")
