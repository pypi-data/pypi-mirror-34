# list_property
Module for making list properties or named lists


## list_property - function
```python
import list_property

class Person(list):
    first_name = list_property(0)
    last_name = list_property(1)
    middle_initial = list_property(2, '')

p = Person(("John", "Smith"))
assert p == ["John", "Smith"]

assert p.first_name == 'John'
assert p[0] == 'John'
assert p.last_name == 'Smith'
assert p[1] == 'Smith'
assert p.middle_initial == ''
try:
    assert p[2] == ''
    raise AssertionError('Index 2 was not set and there should be an IndexError!')
except IndexError:
    pass  # Success

p.first_name = "Hello"
p.last_name = 'World!'
p.middle_initial = 'T'
assert p.first_name == 'Hello'
assert p[0] == 'Hello'
assert p.last_name == 'World!'
assert p[1] == 'World!'
assert p.middle_initial == 'T'
assert p[2] == 'T'  # Note: p[2] is now set
```
 This class also works like a property decorator
 
 ```python
import list_property
 
class Person(list):
    @list_property(0)
    def first_name(self):
        try:
            return self[0]
        except:
            return 'anonymous'

    middle_initial = list_property(2)
   
    @middle_initial.setter
    def middle_initial(self, value):
        self[2] = str(value)[0].upper()
```


## namedlist
Named list factory function like named tuple

```python
from list_property import namedlist, NamedList

Person = namedlist('Person', 'first_name last_name middle_initial', {'middle_initial': 'T'})

p = Person('John', 'Smith')
assert p.first_name == 'John'
assert p[0] == 'John'
assert p.last_name == 'Smith'
assert p[1] == 'Smith'
assert p.middle_initial == 'T'
assert p[2] == 'T'
assert isinstance(p, list)
assert isinstance(p, NamedList)
```
