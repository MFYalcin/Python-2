ECOR1042S Summer 2022 README for Milestone 3 Objective Project Version 1.0... 19/08/2022

The project can be reached at:
Voice: (+1)438-523-9319
Website: ...
Student Number: 101233944
Email:muhammetyalcin@cmail.carleton.ca

Description:
------------
- The project contains various modules that are implemented through the related part of the function calls in the given project Milestones...
- It subsequently provides a user with an interface and selection of commands, to load a datafile, 
which can either have a book added to it and removed from it. Books that have been inputted to shell, in this case accordingly, contain books of titles, 
rates, authors, publishers or categories, sort books by title, rate, publisher or author, last but not least text-based user interface and calling the data analysis functions are executed as it is going to be mentioned below.

- The project of T1A1_P5_data_analyzer is made up of multiple files:
      T1A1_P1_load_data.py                          A python script
      T1A1_P2_add_remove_search_dataset.py          A python script
      T1A1_P3_sorting_fun.py                        A python script
      T1A1_P4_booksUI.py                            A python script

      
                              
	
	

- Please verify the correct files related to their implemented locations. 
- The functions called add/remove that have been done, might execute a temporary dictionary as opposed to get datas from given datafile.





Installation:
-------------
The version of Python 3.10.6 or later must be installed in order to make it work and not to get any errors.
External modules might be loaded in the beginning for desired calls in the python scripts.

Usage:
------
> python T1A1_P4_booksUI.py      

When prompted, enter any of strings, float points or integers with proper style according to given T1A1_P5_load_data, otherwise there is no error control -- if you type invalid value, the program ends.

The available commands are(in order): 
L)oad data
A)dd book
R)emove book
G)et books
   T)itle R)ate A)uthor P)ublisher C)ategory
GCT) Get all Categories for book Title
S)ort books
   T)itle R)ate P)ublisher A)uthor
Q)uit

- The upper letters seen in this command allows users to get a list of related functions and in some commands, once executed with an upper letter, there comes other multiple options to execute as desired.

Credits:
--------
Muhammet Yalcin : Worked on README.md file and how to properly demonstrate the function to make it run easier for users and consequently the writer of(in order):
T1A1_P1_{book_category_dictionary}.py
T1A1_P1_main_{book_category_dictionary}.py
T1A1_P2_fun.py -> ((Function 1: add_book ) and (Function 2: remove_book))
T1A1_P2_test.py -> ((Test Function 1: add_book) and (Test Function 2: remove_book))
T1A1_P3_sorting.py -> (Function 1: sort_books_title) and (Function 4: sort_books_ascending_rate)
T1A1_P3_sorting_test.py
T1A1_P4_UI_{case1}
README.md



Soliman Elkhouli : Worked on T1A1_report.pdf file and worked on how to properly demonstrate functions to work easier for users and consequently the writer of(in order):
T1A1P1{book_author_dictionary}.py
T1A1_P1main{book_author_dictionary}.py
T1A1_P2_fun.py -> ((Function 6: get_books_by_author ) and (Function 7: get_books_by_publisher) and (Function 8: get_all_categories_for_book_title))
T1A1_P2_test.py -> ((Function 6: get_books_by_author ) and (Function 7: get_books_by_publisher) and (Function 8: get_all_categories_for_book_title))
T1A1_P3_sorting.py -> (Function 3: sort_books_author) 
T1A1_P3_sorting_test.py
T1A1_P4UI{case4}
README.md





Tsu Hsun Chen : Worked on T1A1_P5_load_data and did release the software accordingly and packaged the code together and consequently the writer of(in order):
T1A1P1{book_publisher_dictionary}.py
T1A1_P1main{book_publisher_dictionary}.py
T1A1_P1_load_data.py
T1A1_P2_fun.py -> ((Function 4): get_books_by_rating) and (Function 5): get_books_by_title)
T1A1_P2_test.py -> ((Test Function 4: get_books_by_title) and (Test Function 5: get_books_by_rating))
T1A1_P2_add_remove_search_dataset.py
T1A1_P3_sorting.py -> (sort_books_publisher)
(2)T1A1_P3_sorting_test.py
T1A1_P3_sorting_fun.py
T1A1_P4UI{case2}
T1A1_P4_booksUI.py
T1A1_P5_load_data.py
T1A1_data_analyzer.zip
README.md






Licence:
--------
[Github](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features customizing-your-repository/about-readmes)
[Markdowntutorial](https://www.markdowntutorial.com/lesson/1/)
[MakeREADME](https://www.makeareadme.com/)
[MarkDownGuide](https://www.markdownguide.org/getting-started/)
[HowToWriteAREADME](https://www.wikihow.com/Write-a-Read-Me)