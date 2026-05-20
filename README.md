README.md
JUSTCHECK Plagiarism Checker
Project Title

JUSTCHECK – Plagiarism Checker System

Project Description

JUSTCHECK is a Python-based plagiarism detection system designed to compare two text documents and identify similarities between them.

The application preprocesses text files, removes punctuation, converts all text to lowercase, counts word frequencies, searches for specific words, and calculates a plagiarism percentage based on common and unique words.

This project demonstrates:

File handling
Object-Oriented Programming (OOP)
Dictionaries and sets
Error handling
User interaction using menus
Data preprocessing
Modular programming using multiple Python files
Objectives of the Program

The main objectives of this project are:

To compare two text documents.
To identify common words between documents.
To calculate a plagiarism percentage.
To allow users to search for specific words.
To provide meaningful feedback and error handling.
To implement Python concepts in a real-world application.
Modules Used in the Project

The program is divided into four Python files/modules:

Module/File	Purpose
main.py	Controls the whole program and menu system
filter.py	Preprocesses documents
word_search.py	Searches for words in both documents
checker_plagiarism.py	Calculates plagiarism percentage
Program Structure Overview
                    +------------------+
                    |    main.py       |
                    +------------------+
                              |
      -------------------------------------------------
      |                     |                         |
      v                     v                         v
+-------------+    +----------------+      +----------------------+
| filter.py   |    | word_search.py |      | checker_plagiarism.py|
+-------------+    +----------------+      +----------------------+
Detailed Explanation of Each File
1. main.py
Purpose

This is the main controller of the application.
It:

Loads documents
Displays the menu
Calls functions from other modules
Handles user interaction
Imported Modules
import filter
import word_search
import checker_plagiarism

These imports allow the program to use classes and methods from other files.

Main Functionalities
1. Display Welcome Screen
print("="*100)
print("WELCOME TO THE JUSTCHECK PLAGIARISM CHECKER")

This creates a professional user interface.

2. Load Documents
document1="essay-1.txt"
document2="essay-2.txt"

The program uses two text documents for comparison.

3. Preprocess Documents
preprocess_instance = filter.Preprocess()
document1_list = preprocess_instance.process(document1)

This sends the documents to the preprocessing module.

4. Error Handling
if document1_list is None or document2_list is None:

If files cannot be found, the program:

Displays an error message
Prevents crashing
Allows the user to try again

This improves reliability and usability.

5. Convert Lists into Sets
document1_set = set(document1_list)
document2_set = set(document2_list)

Sets are used because:

They remove duplicates
They help find common and unique words efficiently
6. Find Common and Unique Words
common_words = document1_set.intersection(document2_set)
unique_words = document1_set.union(document2_set)
intersection() finds matching words
union() finds all unique words
7. Create Frequency Dictionaries
document1_dict = preprocess_instance.get_word_count(document1_list)

This counts how many times each word appears.

Example:

{
   "python": 4,
   "programming": 2
}
8. Menu System

The menu allows users to:

Search for a word
Run plagiarism check
Exit program
9. Input Validation
try:
    choice = int(input())
except ValueError:

This prevents invalid input such as letters instead of numbers.

10. Plagiarism Check
check_instance.plagiarism_status(common_wordscount, unique_wordscount)

This calculates the similarity percentage.

2. filter.py
Purpose

This module preprocesses the documents before analysis.

Class: Preprocess
class Preprocess:

This class contains methods related to document cleaning and word counting.

Method 1: process()
Purpose

Reads a file and cleans the text.

Operations Performed
a) Open File
with open(clean_path, 'r', encoding='utf-8')

Reads the text file safely.

b) Convert to Lowercase
text = file.read().lower()

This ensures:

"Python"
"python"

are treated as the same word.

c) Remove Punctuation
text.translate(str.maketrans('', '', string.punctuation))

Removes:

commas
periods
exclamation marks
symbols

Example:

"Hello!" → "hello"
d) Split into Words
return text.split()

Converts the text into a list of words.

Example:

["this", "is", "python"]
Error Handling
except FileNotFoundError:

If the file does not exist:

an error message is displayed
the program continues safely
Method 2: get_word_count()
Purpose

Counts the frequency of each word.

Example

Input:

["python", "code", "python"]

Output:

{
  "python": 2,
  "code": 1
}
3. word_search.py
Purpose

Allows the user to search for a word in both documents.

Class: Search_word
class Search_word:
Method: find_word()
Purpose

Searches for a word entered by the user.

Step 1: Get User Input
word_entered = input()
Step 2: Convert to Lowercase
.strip().lower()

This ensures accurate matching.

Step 3: Count Appearances
appearanceInOne = dict1.get(word_entered, 0)

The .get() method:

avoids crashes
returns 0 if word is absent
Step 4: Display Results

Example output:

'python' found 3 times in document one.
Step 5: Return Boolean Value
return True

Returns:

True if found in both documents
False otherwise

This follows assignment requirements.

4. checker_plagiarism.py
Purpose

Calculates plagiarism percentage.

Class: checker
class checker:
Method: plagiarism_status()
Formula Used

The plagiarism percentage is calculated using:

Plagiarism Percentage=(
Unique Words
Common Words
	​

)×100

Explanation
Common words = words appearing in both documents
Unique words = total distinct words across both documents
Example

If:

Common words = 50
Unique words = 100

Then:

Plagiarism = 50%
Plagiarism Decision
if plagiarism_count >= 50:

If plagiarism is 50% or higher:

plagiarism is detected

Otherwise:

no plagiarism is detected
Features Implemented
Core Features

✔ Document comparison
✔ Word frequency analysis
✔ Plagiarism percentage calculation
✔ Word search functionality
✔ Menu-driven interface
✔ Modular programming
✔ Object-Oriented Programming
✔ Error handling
✔ Input validation
✔ User-friendly outputs

Python Concepts Demonstrated
Concept	Example
Classes & Objects	Preprocess(), checker()
File Handling	open()
Dictionaries	Word frequency counts
Sets	Common and unique words
Loops	Menu repetition
Conditionals	Menu choices
Exception Handling	try-except
String Manipulation	Lowercase conversion
Modular Programming	Multiple Python files
Error Handling Implemented

The program includes strong validation and error handling.

1. File Not Found Handling
except FileNotFoundError:

Prevents crashes when invalid file paths are used.

2. Invalid Input Handling
except ValueError:

Prevents crashes if users enter letters instead of numbers.

3. Safe Dictionary Access
dict.get(word, 0)

Avoids key errors.

How the Whole Program Works
Step-by-Step Execution Flow
Step 1

Program starts from:

main()
Step 2

Documents are loaded.

Step 3

Documents are cleaned and preprocessed.

Step 4

Word frequencies are calculated.

Step 5

User chooses an option from the menu.

Step 6

Depending on the option:

search functionality runs
OR
plagiarism check runs
Step 7

Results are displayed clearly.

Step 8

Program continues until user exits.

Sample Program Execution
============================================================
WELCOME TO THE JUSTCHECK PLAGIARISM CHECKER
============================================================

1. Search for a word
2. Run a plagiarism check and see common words
3. Exit Program

Enter your choice: 2
Advantages of the System
Easy to use
Fast comparison
Organized modular structure
Good error handling
Reusable code
Efficient word matching using sets
Limitations of the System
Only works with text files
Checks exact word similarity only
Does not detect paraphrasing
Uses basic plagiarism calculation
Possible Future Improvements
Add GUI interface
Support PDF and DOCX files
Use advanced plagiarism algorithms
Add percentage similarity graphs
Store plagiarism history
Compare multiple documents simultaneously
Conclusion

The JUSTCHECK Plagiarism Checker successfully demonstrates the use of Python programming concepts to build a functional plagiarism detection system.

The project effectively combines:

file processing,
data structures,
modular programming,
object-oriented programming,
and error handling

to produce a reliable and user-friendly application.

The system fulfills all assignment requirements and demonstrates strong software development practices.

Authors

Developed by:
[Student Name]

Course:
Programming Fundamentals / Python Programming

File Requirements

Ensure the following files are in the same folder:

main.py
filter.py
word_search.py
checker_plagiarism.py
essay-1.txt
essay-2.txt
README.md
How to Run the Program
Step 1

Open terminal or command prompt.

Step 2

Navigate to project folder.

Step 3

Run:

python main.py
End of READMEREADME.md
JUSTCHECK Plagiarism Checker
Project Title

JUSTCHECK – Plagiarism Checker System

Project Description

JUSTCHECK is a Python-based plagiarism detection system designed to compare two text documents and identify similarities between them.

The application preprocesses text files, removes punctuation, converts all text to lowercase, counts word frequencies, searches for specific words, and calculates a plagiarism percentage based on common and unique words.

This project demonstrates:

File handling
Object-Oriented Programming (OOP)
Dictionaries and sets
Error handling
User interaction using menus
Data preprocessing
Modular programming using multiple Python files
Objectives of the Program

The main objectives of this project are:

To compare two text documents.
To identify common words between documents.
To calculate a plagiarism percentage.
To allow users to search for specific words.
To provide meaningful feedback and error handling.
To implement Python concepts in a real-world application.
Modules Used in the Project

The program is divided into four Python files/modules:

Module/File	Purpose
main.py	Controls the whole program and menu system
filter.py	Preprocesses documents
word_search.py	Searches for words in both documents
checker_plagiarism.py	Calculates plagiarism percentage
Program Structure Overview
                    +------------------+
                    |    main.py       |
                    +------------------+
                              |
      -------------------------------------------------
      |                     |                         |
      v                     v                         v
+-------------+    +----------------+      +----------------------+
| filter.py   |    | word_search.py |      | checker_plagiarism.py|
+-------------+    +----------------+      +----------------------+
Detailed Explanation of Each File
1. main.py
Purpose

This is the main controller of the application.
It:

Loads documents
Displays the menu
Calls functions from other modules
Handles user interaction
Imported Modules
import filter
import word_search
import checker_plagiarism

These imports allow the program to use classes and methods from other files.

Main Functionalities
1. Display Welcome Screen
print("="*100)
print("WELCOME TO THE JUSTCHECK PLAGIARISM CHECKER")

This creates a professional user interface.

2. Load Documents
document1="essay-1.txt"
document2="essay-2.txt"

The program uses two text documents for comparison.

3. Preprocess Documents
preprocess_instance = filter.Preprocess()
document1_list = preprocess_instance.process(document1)

This sends the documents to the preprocessing module.

4. Error Handling
if document1_list is None or document2_list is None:

If files cannot be found, the program:

Displays an error message
Prevents crashing
Allows the user to try again

This improves reliability and usability.

5. Convert Lists into Sets
document1_set = set(document1_list)
document2_set = set(document2_list)

Sets are used because:

They remove duplicates
They help find common and unique words efficiently
6. Find Common and Unique Words
common_words = document1_set.intersection(document2_set)
unique_words = document1_set.union(document2_set)
intersection() finds matching words
union() finds all unique words
7. Create Frequency Dictionaries
document1_dict = preprocess_instance.get_word_count(document1_list)

This counts how many times each word appears.

Example:

{
   "python": 4,
   "programming": 2
}
8. Menu System

The menu allows users to:

Search for a word
Run plagiarism check
Exit program
9. Input Validation
try:
    choice = int(input())
except ValueError:

This prevents invalid input such as letters instead of numbers.

10. Plagiarism Check
check_instance.plagiarism_status(common_wordscount, unique_wordscount)

This calculates the similarity percentage.

2. filter.py
Purpose

This module preprocesses the documents before analysis.

Class: Preprocess
class Preprocess:

This class contains methods related to document cleaning and word counting.

Method 1: process()
Purpose

Reads a file and cleans the text.

Operations Performed
a) Open File
with open(clean_path, 'r', encoding='utf-8')

Reads the text file safely.

b) Convert to Lowercase
text = file.read().lower()

This ensures:

"Python"
"python"

are treated as the same word.

c) Remove Punctuation
text.translate(str.maketrans('', '', string.punctuation))

Removes:

commas
periods
exclamation marks
symbols

Example:

"Hello!" → "hello"
d) Split into Words
return text.split()

Converts the text into a list of words.

Example:

["this", "is", "python"]
Error Handling
except FileNotFoundError:

If the file does not exist:

an error message is displayed
the program continues safely
Method 2: get_word_count()
Purpose

Counts the frequency of each word.

Example

Input:

["python", "code", "python"]

Output:

{
  "python": 2,
  "code": 1
}
3. word_search.py
Purpose

Allows the user to search for a word in both documents.

Class: Search_word
class Search_word:
Method: find_word()
Purpose

Searches for a word entered by the user.

Step 1: Get User Input
word_entered = input()
Step 2: Convert to Lowercase
.strip().lower()

This ensures accurate matching.

Step 3: Count Appearances
appearanceInOne = dict1.get(word_entered, 0)

The .get() method:

avoids crashes
returns 0 if word is absent
Step 4: Display Results

Example output:

'python' found 3 times in document one.
Step 5: Return Boolean Value
return True

Returns:

True if found in both documents
False otherwise

This follows assignment requirements.

4. checker_plagiarism.py
Purpose

Calculates plagiarism percentage.

Class: checker
class checker:
Method: plagiarism_status()
Formula Used

The plagiarism percentage is calculated using:

Plagiarism Percentage=(
Unique Words
Common Words
	​

)×100

Explanation
Common words = words appearing in both documents
Unique words = total distinct words across both documents
Example

If:

Common words = 50
Unique words = 100

Then:

Plagiarism = 50%
Plagiarism Decision
if plagiarism_count >= 50:

If plagiarism is 50% or higher:

plagiarism is detected

Otherwise:

no plagiarism is detected
Features Implemented
Core Features

✔ Document comparison
✔ Word frequency analysis
✔ Plagiarism percentage calculation
✔ Word search functionality
✔ Menu-driven interface
✔ Modular programming
✔ Object-Oriented Programming
✔ Error handling
✔ Input validation
✔ User-friendly outputs

Python Concepts Demonstrated
Concept	Example
Classes & Objects	Preprocess(), checker()
File Handling	open()
Dictionaries	Word frequency counts
Sets	Common and unique words
Loops	Menu repetition
Conditionals	Menu choices
Exception Handling	try-except
String Manipulation	Lowercase conversion
Modular Programming	Multiple Python files
Error Handling Implemented

The program includes strong validation and error handling.

1. File Not Found Handling
except FileNotFoundError:

Prevents crashes when invalid file paths are used.

2. Invalid Input Handling
except ValueError:

Prevents crashes if users enter letters instead of numbers.

3. Safe Dictionary Access
dict.get(word, 0)

Avoids key errors.

How the Whole Program Works
Step-by-Step Execution Flow
Step 1

Program starts from:

main()
Step 2

Documents are loaded.

Step 3

Documents are cleaned and preprocessed.

Step 4

Word frequencies are calculated.

Step 5

User chooses an option from the menu.

Step 6

Depending on the option:

search functionality runs
OR
plagiarism check runs
Step 7

Results are displayed clearly.

Step 8

Program continues until user exits.

Sample Program Execution
============================================================
WELCOME TO THE JUSTCHECK PLAGIARISM CHECKER
============================================================

1. Search for a word
2. Run a plagiarism check and see common words
3. Exit Program

Enter your choice: 2
Advantages of the System
Easy to use
Fast comparison
Organized modular structure
Good error handling
Reusable code
Efficient word matching using sets
Limitations of the System
Only works with text files
Checks exact word similarity only
Does not detect paraphrasing
Uses basic plagiarism calculation
Possible Future Improvements
Add GUI interface
Support PDF and DOCX files
Use advanced plagiarism algorithms
Add percentage similarity graphs
Store plagiarism history
Compare multiple documents simultaneously
Conclusion

The JUSTCHECK Plagiarism Checker successfully demonstrates the use of Python programming concepts to build a functional plagiarism detection system.

The project effectively combines:

file processing,
data structures,
modular programming,
object-oriented programming,
and error handling

to produce a reliable and user-friendly application.

The system fulfills all assignment requirements and demonstrates strong software development practices.

Authors

Developed by:
[Student Name]

Course:
Programming Fundamentals / Python Programming

File Requirements

Ensure the following files are in the same folder:

main.py
filter.py
word_search.py
checker_plagiarism.py
essay-1.txt
essay-2.txt
README.md
How to Run the Program
Step 1

Open terminal or command prompt.

Step 2

Navigate to project folder.

Step 3

Run:

python main.py
End of README
