AirBnB clone - The console
===========================

***General***

* How to create a Python package
<p>

1. Create a directory and give it your package's name.
2. Put your classes in it.
3. Create a __init__.py file in the directory
i.g.
```
class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild Cat']
 
 
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
```
<p/>

* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID

### Usage of `*args` and `**kwargs`
-----------------------------------

<p>

`*args` and `**kwargs` are used in function definitions.
They allow you to pass a variable number of arguments to a function, handle keyword argument list in a funtion.
It can be used to call a function with a list or dictionary of arguments.


|:Keyword:|:What it is:|
|---------|------------|
| `*args` | is used to send a **non-keyworded variable** length argument list to the function.|
| `**Kwargs` | allows you to pass **keyworded variable** length of arguments, handle named arguments to/in a function.|

</p>

* How to handle named arguments in a function

***More Info***

Execution
Your shell should work like this in interactive mode:

Resources
==========

*Read or watch:*

* [cmd module](https://docs.python.org/3.4/library/cmd.html)

**packages concept page**

  * [Creating a Python Package](https://www.pythoncentral.io/how-to-create-a-python-package/)
  * [Importing * From a Package](https://docs.python.org/3.4/tutorial/modules.html#packages)

* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
