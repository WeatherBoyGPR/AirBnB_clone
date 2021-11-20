AirBnB clone - The console
===========================

<p>
This console project is very similar to shell except its a single use function.
"A Command-Line Interface" from where it allows us (nerds/developers), admin, etc., to;

  * Create,
  * Modify and,
  * Delete Objects.

All connected from the file storage. We are bulding a tool where you can manipulate what you want to work,
or fix something that doesnt work from the file storage. After whiteboarding your ideas, this is one of the first steps
before getting started to build the rest of a web application. In this case using AirBnB as an example, called
"AirBnB Clone" with the objective to fully building a working command interpreter to manage the AirBnB Clone's objects.

In the process you will understand what the console (command-line interface) can do?, how it will work?,
how user will use it? and more from a developers perspective.
The AirBnB Clone console is the perfect example to manage the entities of the system
using the commands explained further.
The goal of this console is to be able to manage and manipulate data like:

  * objects and,
  * data of the application

The objects that will be manipulated are basic classes:
  * Users
  * Places
  * States
  * Cities
  * Amenities
  * Reviews
</p>

# Geting started part 1: What’s a command interpreter?
<p>
Remember it was compared to the Shell?
It’s exactly the same but limited to a specific use-case.
The command-line interpreter is a tool that can read what it receives (what is written) from the terminal,
and manipulates the arguments put in place in the command-line and executes the proccess it it was commanded.
Converts the commands/arguments into instructions for the rpogram.
In this project, we are creating the command-interpreter with the functions/methods we want or need
in order to achieve the correct output while managing our Cloned AirBnB's objects, like:

  * Create a new object (ex: a new User or a new Place)
  * Retrieve an object from a file, a database etc…
  * Do operations on objects (count, compute stats, etc…)
  * Update attributes of an object
  * Destroy an object

## part 1.b: Writing a command interpreter to manage the AirBnB objects

***Step 1:***

  1. Create a parent/main class (called BaseModel) which will manipulate
  the initialization, serialization, and desirialization of future instances.
  2. Create a simple flow of serialization/deserialization:

    ```
	Instance <-> Dictionary <-> JSON string <-> file
	```

  3. Create all ***classes*** used for AirBnB that will inherit from `BaseModel`
    * `User`, `State`, `City`, `Amenities`, `Reviews`, etc...
  4. In the meantime you or your partner will build a storage engine of the project:
    * The <FileStorage>, where it'll be able to save and retrieve any data needed.
</p>

##How to USE and START the Command Interpreter:

There are 2 way to use the Interpreter.
The console execution examples interactive vs non-interactive:

***Interactive mode*** executes the command interpreter and displays the prompt.

  - `$./console.py` -> *"the command"*
  - `(hbnb)` -> *"the displayed prompt after execution"*
Once you have executed the interactive mode command (in this case the "./console.py) it initializes the console in interactive mode.
Asserting commands and wait for it to read and return what was needed, and continue using it accordingly.
Below you have some examples on how to use the interpreter after starting it.


```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb) help create
Creates a new instance of class

(hbnb)
(hbnb) quit
$
```

**VS. on how non-interactive mode looks**

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

| |**Console Commands available**|
|:-------:|-----------:|
| `all` | Allows displays all instances whether their based or not on the class name. |
| `create` | Allows to create an instance of the class and return it's id. |
| `show` | Allows to view more information of the command or id. |
| `destroy` | Allows to delete/destroy an instance of a class name and it's id. |
| `count` | Returns the ammount of objects tha exists in the speccified class. |

![alt text](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIF.AO7WKrxrWOEyAgfKr4X75g%26pid%3DApi&f=1.png)
## Concepts understanding to Building the AirBnB Console

* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
<p>
Unittest provides a base class, TestCase, which may be used to create new test cases.
test suite. A test suite is a collection of test cases, test suites, or both.
It is used to aggregate tests that should be executed together. test runner

It's the first level of software from the smallest testable parts are being checked for bugs.
It helps us validate that each unit of the functions preforms as it was architected or needed.
</p>

***Basic test case (TestClass)***

```
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```


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


|Keyword|***What it is***|
|:---------|------------|
| `*args` | is used to send a **non-keyworded variable** length argument list to the function.|
| `**Kwargs` | allows you to pass **keyworded variable** length of arguments, handle named arguments to/in a function.|

</p>

***More Info***

Resources
==========

*Read or watch:*

* [cmd module](https://docs.python.org/3.4/library/cmd.html)

**packages concept page**

  * [Creating a Python Package](https://www.pythoncentral.io/how-to-create-a-python-package/)
  * [Importing * From a Package](https://docs.python.org/3.4/tutorial/modules.html#packages)

* [uuid module](https://docs.python.org/3.4/library/uuid.html)
* [datetime](https://docs.python.org/3.4/library/datetime.html)
* [Unit Testing Framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## AUTHORS

**Gabriela Martinez** - [GabsMermaid](https://github.com/GabsMermaid)
**Gino** - [WeatherBoyGPR](https://github.com/WeatherBoyGPR)
**Johanne Lopez** - [johanne101](https://github.com/Johanne101)
