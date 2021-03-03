'''
Module that represents a notebook
'''

from datetime import date

last_id = 0

class Note:
    '''
    Represent a note in the notebook. Match
    against the string in searches and store
    tags for each one

        ...

    Attributes
    ----------
    memo : str
        text of a note
    tags : str
        tags of a note

    Methods
    -------
    match(filter: str)
        determine if the note matches the
        filter text.
    '''

    def __init__(self, memo: str, tags=''):
        '''
        initialize a note with memo and
        optional space-separated tags.
        Automatically set the note's
        creation date and a unique id

        Parameters
        ----------
        memo : str
            text of a note
        tags : str
            tags of a note
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Determine if the note matches the
        filter text.

        Parameters
        ----------
        filter : str
            string to match a given text
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    Represent a collection of notes that can be tagged,
    modified, and searched

        ...

    Attributes
    ----------
    notes : list
        list of notes

    Methods
    -------
    new_note(meo: str, tags: str)
        create a new note and add it to the list
    modify_memo(note_id: int, memo: str)
        find a note with a given id and change
        its memo to the given value
    modify_tags(self, note_id: int, tags: str)
        find a note with a given id and change
        its tags to the given value
    search(self, filter: str)
        find all notes that match the given
        filter string
    '''

    def __init__(self):
        '''
        initialize a notebook with an empty list
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list

        Parameters
        ----------
        memo : str
            text of a note
        tags : str
            tags of a note

        >>> n = Notebook()
        >>> n.new_note("hello world")
        >>> n.new_note("hello again")
        >>> n.notes[0].memo
        'hello world'
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        Find a note with a given id and change
        its memo to the given value

        Parameters
        ----------
        note_id : int
            id of a note that should be modified
        memo : str
            text of a note

        >>> n = Notebook()
        >>> n.new_note("hello world")
        >>> n.new_note("hello again")
        >>> n.modify_memo(1, "hi world")
        >>> n.notes[0].memo
        'hi world'
        '''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        '''
        Find a note with a given id and change
        its tags to the given value

        Parameters
        ----------
        note_id : int
            id of a note that should be modified
        tags : str
            tags of a note
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''
        Find all notes that match the given
        filter string

        Parameters
        ----------
        filter : str
            string to search a given text
        '''
        return [note for note in self.notes if note.match(filter)]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
