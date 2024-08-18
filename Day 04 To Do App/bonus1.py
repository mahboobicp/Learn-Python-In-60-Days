# String operation replace('.','-',1) - immutable
# Tuples imputable e,g myTuple = ('A', 'B')
# List are mutable e.g mylist = ['A','B']

myBooks = ['1. Physics' , '2. Maths' , '3. Chemesitry']
for book in myBooks:
    print(f"In List formate :{book}")
    print('***'*10)
    book = book.replace('.','-',1)      # This string method will replace . in book name
    print(f"In String form : {book}")
    print('***'*10)