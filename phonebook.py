### PYTHON PHONEBOOK v0.1 ###

###### MAIN FUNCTIONS ######

def add_contact(name, number):
    #adds contact to database
    db['{}'.format(name)] = '{}'.format(str(number))
    print('{} was successfully added to contacts!'.format(name))

def del_contact(name):
    #deletes contact from database
    del db[name.lower()]
    print('{} was successfully deleted from contacts!'.format(name))

def search(letter):
    #iterates through database and searches for db key beginning with 'letter'
    d = {}
    count = 0
    b = bytearray(letter,'utf-8')
    b = letter.encode('utf-8')   #this is a formality for working with dbm
    for key in db:               #module. letter needs to be converted to bytes
        if key.lower().startswith(b):
            d[key.decode('utf-8')] = db[key.decode('utf-8')] #if it finds something starting with 'letter'
            count +=1        #it adds the entry to a new database for printing
    
    if count > 0: #checks if any matches pop up
        for key in d:
            print('{}'.format(key),' ' * (20 - len(key)),'{}'.format(d[key].decode('utf-8')))
    else:         #if no matches, tells the user there are none
        print('No contacts under listing \'{}\'.'.format(letter.upper()))
            
def view_all():
    #iterates through entire dictionary and prints each contact
    #with correct spacing
    for key in db:
        print('{}'.format(key.decode('utf-8')),' ' * (20 - len(key)),'{}'.format(db[key].decode('utf-8')))

def exit_program():
    print('Closing database.')
    db.close()
    sys.exit()


###### PROGRAM FLOW ######

def main_loop():
    #main control function. Navigates to all other functions.
    print('\n'*50)
    print('='*14)
    print('Phonebook v0.1')
    print('  MAIN MENU')
    print('='*14)
    print('\n')
    print('Select your action:')
    print('-------------------')
    print('1) Add Contact.')
    print('2) Delete Contact.')
    print('3) Search Contact by letter.')
    print('4) View all Contacts.')
    print('5) Exit Program.')
    
    while True:
        choice = input('Enter a valid number:')
        try:
            if int(choice) == 1:
                add_loop()
            elif int(choice) == 2:
                del_loop()
            elif int(choice) == 3:
                search_loop()
            elif int(choice) == 4:
                view_all_loop()
            elif int(choice) == 5:
                sys.exit()
        except SystemExit:
            exit_program()
        except ValueError:
            print('Please make sure to enter a valid integer.')
        

def add_loop():
    #this function regulates and initiates the add_contact() function
    print('\n'*50)
    print('='*14)
    print('Add Contact')
    print('='*14)
    print()
    name = str(input('Please enter the name of the contact:'))
    number = str(input('Please enter the phone number of the contact:'))
    add_contact(name,number)
    print()
    input('Press ENTER to return to MAIN MENU:')
    main_loop()

def del_loop():
    #this function regulates and initiates the del_contact() function
    print('\n'*50)
    print('='*14)
    print('Delete Contact')
    print('='*14)
    print()
    print('Please enter the name of the contact you wish to delete:')
    while True:
        name = str(input())
        if name in db:
            del_contact(name)
            print()
            input('Press ENTER to return to MAIN MENU:')
            main_loop()
        elif name == 'quit'.lower():
            main_loop()
        else:
            print('Name does not exist in database.\nRe-enter the correct name, or type \'quit\' to return to the MAIN MENU:')

def search_loop():
    #this function regulates the search() function
    print('\n'*50)
    print('='*14)
    print('Search By Letter')
    print('='*14)
    print()
    print('Please enter a single letter to search contacts:')
    while True:
        letter = input()
        try:
            if len(letter) == 1:
                if str(letter) in 'abcdefghijklmnopqrstuvwxyz':
                    print('Name:                 Number:')
                    print('-'*32)
                    search(letter)
                    print('\n')
                    input('Press ENTER to return to MAIN MENU:')
                    main_loop()
                else:
                    print('You need to input a letter from the alphabet. Type \'quit\' if you want to return to MAIN MENU.')
            elif letter == 'quit'.lower():
                main_loop()
                break
            else:
                print('That\'s not a single letter! Type \'quit\' if you want to return to MAIN MENU.')
        except SystemExit:
            sys.exit()
        except:
            return False
    

def view_all_loop():
    print('\n'*50)
    print('='*14)
    print('All Contacts')
    print('='*14)
    print()
    print('Name:                 Number:')
    print('-'*32)
    view_all()
    print('\n')
    input('Press ENTER to return to MAIN MENU:')
    main_loop()


###### CONTROL ######

import dbm
import sys


db = dbm.open('contacts','c') #creating/opening database that contains names and numbers of contacts
main_loop()                   #initiate program

    

###### CURRENT BUGS ######

'''
1) exit_program() function behaving strangely.
Something to do with the 'try' loops layering over themselves,
causing the exit_program() function to be called multiple times
as the program unwraps itself. I'm concerned that this will become
a huge architectural problem in later versions :(

2) no error handling system for add_contact when the user inputs
a non-alphabetic character for the name of a contact
(will get around to implementing this)
'''

###### FUTURE FEATURES ######

'''
1) Improved search and delete functionality, including fuzzy string searching
that will suggest similar names to you if you misspell the name of a contact.
(Will need to research fuzzy string matching first)

2) 'Search by number' feature.

3) GUI [Will need to learn TkInter first :) ]
'''
