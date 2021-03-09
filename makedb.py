from lutz import Person, Manager

bob = Person('Bob Smith', 'director', 7000)
sue = Person('Sue Jones', 'dev', 2500)
tom = Manager('Tom Jones', 5000)

import shelve

db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()