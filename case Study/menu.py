import sys
from notebook import Notebook


class Menu:
    """Display a menu and respond to choices when run."""

    def __init__(self):
        self.noteBook = Notebook()
    def display_menu(self):
        print(
            """
Notebook Menu

1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
"""
        )

    def run(self):
        """Display the menu and respond to choices."""
        self.display_menu()
        self.add_note("test memo","test tags")
        #self.show_notes()
        #self.search_notes("test")
        self.modify_note((self.search_notes("test"))[0])
        self.quit()

    def show_notes(self, notes=None):
        if not notes:
            notes = self.noteBook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))

    def search_notes(self,filter):
        notes = self.noteBook.search(filter)
        self.show_notes(notes)
        return notes


    def add_note(self,memo,tags):
        self.noteBook.new_note(memo,tags)

    def modify_note(self,note):
        self.noteBook.modify_memo(note.id,note.memo)
        self.noteBook.modify_tags(note.id,note.tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
