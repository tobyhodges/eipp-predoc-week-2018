# scope



def f():
    x = 1
    print(x)

x = 2
f()
print(x)

x = 2
a = [x**2 for x in range(10)]
print(a)
print(x)

# note that loops don't have their own scope but comprehensions do

# class definitions
class Sequence:
    '''A simple example of an object for representing biological sequences'''
    def __init__(self, identifier, sequence_string):
        self.seq = sequence_string
        self.id = identifier
    def to_fasta(self):
        '''Return a FASTA representation of the sequence as a string.'''
        fasta_record = '>{}\n{}'.format(self.id, self.seq)
        return fasta_record
    def __getitem__(self, key):
        return self.seq[key]

class RNA_Sequence(Sequence):
    def __init__(self, identifier, sequence_string):
        Sequence.__init__(self, identifier, sequence_string)
        self.alphabet = 'RNA'

class DNA_Sequence(Sequence):
    def __init__(self, identifier, sequence_string):
        Sequence.__init__(self, identifier, sequence_string)
        self.alphabet = 'DNA'
    def transcribe(self):
        table = {'A': 'U',
                 'C': 'G',
                 'G': 'C',
                 'T': 'A'}
        tt = str.maketrans(table)
        transcribed_sequence = self.seq.upper().translate(tt)
        transcribed_identifier = self.id + "_transcribed"
        print(transcribed_sequence)
        transcribed_obj = RNA_Sequence(transcribed_identifier, transcribed_sequence)
        return transcribed_obj

# warning about mutable attribute values

class Dog:

    # this is ok
    kind = 'canine'

    # mutable class variable
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(f'a pet called {d.name} of kind {d.kind}')
print(f'a pet called {e.name} of kind {e.kind}')

# operating on the `tricks` class variable in two separate instances
d.add_trick('roll over')
e.add_trick('play dead')

# changing the `kind` class variable
e.kind = 'super-dog'

print(d.kind)
print(d.tricks)
