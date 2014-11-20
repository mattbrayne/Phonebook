Phonebook v0.1
==============

A simple text-based Python phonebook that uses DBM
This program runs in IDLE. (Python3.4)
--------------------------------------------------
This is my first Python project, so any feedback
or criticism is fully appreciated :)
Bug reports are most welcome!
--------------------------------------------------
##################################################
--------------------------------------------------
FUNCTIONS:
--------------------------------------------------
1) Add contact.
   Allows the user to add a contact to the 
   database, asks for name and number as input.
   
2) Delete contact.
   Allows the user to delete a contact from the
   database, asks for a name and looks up the 
   exact string value, so make sure the name is
   spelled correctly.
   
3) Search by Letter.
   Prompts the user for a letter as input and
   prints all contacts that start with that
   letter. If no contacts are found, user will
   be notified.
   
4) View all contacts.
   Prints entire database of contacts in an
   organised manner.
   
5) Exit Program.
   Terminates program.
   
   
--------------------------------------------------
CURRENT BUGS:
--------------------------------------------------

1) exit_program() function behaving strangely.
Something to do with the 'try' loops layering over
themselves, causing the exit_program() function to
be called multiple times as the program unwraps
itself. I'm concerned that this will become a
huge architectural problem in later versions :(

2) no error handling system for add_contact when 
the user inputs a non-alphabetic character for the
name of a contact (will get around to implementing
this eventually)


--------------------------------------------------
FUTURE FEATURES:
--------------------------------------------------

1) Improved search and delete functionality, 
including fuzzy string searching that will suggest 
similar names to you if you misspell the name of a
contact. (Will need to research fuzzy string 
matching first)

2) 'Search by number' feature.

3) GUI [Will need to learn TkInter first :) ]
