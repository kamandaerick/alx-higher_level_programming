Python - Input/Output

1. Write a function that reads a text file (UTF8) and prints it to stdout:

2. Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

3. Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

4. Write a function that returns the JSON representation of an object (string):

5. Write a function that returns an object (Python data structure) represented by a JSON string:

6. Write a function that writes an Object to a text file, using a JSON representation:

7. Write a function that creates an Object from a “JSON file”:

8. Write a script that adds all arguments to a Python list, and then save them to a file:

9. Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

10. Write a class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module

11. Write a class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

12. 
