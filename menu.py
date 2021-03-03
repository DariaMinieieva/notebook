"""
Menu for notebook
"""

import sys
from notebook import Notebook

class Menu:
    '''
    Display menu and respond to choices
    when run
    '''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")

    def run(self):
        '''
        Display menu and respond to choices
        '''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice")

    def show_notes(self, notes=None):
        '''
        Parameters
        ----------
        notes : list
            list of notes
        '''
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print(f"{note.id}: {note.tags}\n{note.memo}")

    def search_notes(self):
        '''
        Search for a note
        '''
        filter = input("Search for: ")
        notes = self.notebook.search(filter)

        self.show_notes(notes)

    def add_note(self):
        '''
        Add note to the notebook
        '''
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)

        print("Your note has been added.")

    def modify_note(self):
        '''
        Modify given note
        '''
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")

        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        '''
        Quit program
        '''
        print("Thank you for using your notebook today.")

        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
