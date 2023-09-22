# Answers
## 1. Basic Python Knowledge:
- Explain the difference between Python 2 and Python 3.
Python has two version one is Python 2 and the other is python 3. Python 2 is the older version and not supported anymore, along with security issues. Now python3 is more popularized and used worldwide. Python 3 was released to improve the issues in python 2. 
    Here are few examples:
    Print statement:

        In Python 2: print is a statement and doesn't require parentheses.

        Example in Python 2: print "Hello, World!"

        In Python 3: print is a function and requires parentheses.

        Example in Python 3: print("Hello, World!")

    Integer division:

        In Python 2, dividing two integers results in an integer, truncating any remainder.

        Example in Python 2: 5 / 2 would yield 2.

        In Python 3, dividing two integers results in a float, providing a more accurate result.

        Example in Python 3: 5 / 2 yields 2.5.

    Unicode and strings:

        Python 2 has ASCII strings by default, and Unicode strings are designated with u prefix.

        Example in Python 2: u"Hello" is a Unicode string.

        Python 3 uses Unicode strings by default, and byte strings are designated with b prefix.

        Example in Python 3: b"Hello" is a byte string.

    xrange vs. range:

        In Python 2, range generates a list, while xrange generates an xrange object, which is more memory-efficient for large ranges.

        In Python 3, range behaves like Python 2's xrange, providing memory-efficient generation of ranges.

    Exception handling:
    
        The as keyword is used in Python 3 for exception handling, providing a cleaner syntax.
        Example in Python 3: except ExceptionType as e:

- Describe Python's data types, such as integers, strings, lists, dictionaries, and sets. 

- Describe your understanding of variables, data assignment, and variable scope.

## 2. Control Structures:
- Write a simple if statement to check a condition.
    ```
    #check if num is odd or even
    num = 5 
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    ```
- Advice / write a code that uses a for loop to iterate over a list or range.
    ```
    #iterate over a list named nums using range
    nums = [1,2,3,4,5,6]
    
    for i in range(len(nums)):#len(nums) provides the length of the nums list, 
        # range creates a list of values from 0 till length -1
        #which can be used as indexes
        print(nums[i]) #prints the value in the index of nums
        
    # iterate over a list nums without using range
    for num in nums:
        print(num)
    ```
- Tell us some example of using while loops.
    ```
    #must initialize the value for which the condition is to be set for while loop
    count = 0
    while count < 5: #iterate until count is less than 5
        print("Count:", count)
        count += 1 # count get added by one    
        
    #creating an infinite loop which asks for input from the user
    # it breaks if the user puts the input quit
    while True:
        user_input = input("Enter 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break
        print("You entered:", user_input)
    ```
    
## 3. Functions:
- Define a function that takes parameters and returns a value.
    ```
    #the function takes an integer value and checks if the value is even
    # returns True if even else False
    def check_if_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
            
    val = check_if_even(5)
    print(val) # prints False
    val = check_if_even(4)
    print(val) # print True
    ```
- Describe about the usage of keyword arguments and default parameter values.
    ```
    def check_if_even(num=4):
        if num % 2 == 0:
            return True
        else:
            return False
    
    # Calling the function without providing any arguments
    result_default = check_if_even()
    print("Is the default number even?", result_default)  # Output: Is the default number even? True
    
    # Calling the function with a specific argument
    result_specific = check_if_even(7)
    print("Is 7 even?", result_specific)  # Output: Is 7 even? False
    
    # Calling the function with a keyword argument
    result_keyword = check_if_even(num=10)
    print("Is 10 even?", result_keyword)  # Output: Is 10 even? True
    
    # Using the default argument
    result_default_arg = check_if_even()
    print("Is the default number even?", result_default_arg)  # Output: Is the default number even? True
    
    ```
In this example, we first define the check_if_even function, which checks if a given number is even or not. The num parameter has a default value of 4, which is used if no argument is provided.

We then call the function in different ways:

- Without providing any arguments, using the default parameter value.
- Providing a specific argument.
- Using a keyword argument.
- Using the default argument again, to demonstrate its usage.

The outputs show whether the given numbers are even based on the function's logic.
 
- Request an example of a function that uses the return statement.
   ```
    #the function takes an integer value and checks if the value is even
    # returns True if even else False
    def check_if_even(num):
        if num % 2 == 0:
            return True
        else:
            return False
            
    val = check_if_even(5) # returns the value provided by the function check_if_even
    print(val) # prints False
    val = check_if_even(4)
    print(val) # print True
    ```
## 3 Data Structures
- Tell us about your knowledge of lists and their methods (e.g., append , pop ,
index ).
Lists are a fundamental data structure in Python, which acts similary to array in other languages, it is used to store collections of items. They are ordered, mutable (can be changed), and can contain a mix of different data types, including numbers, strings, and other objects.
###### append(item):
Adds an item to the end of the list.
```
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
###### pop(index):
Removes and returns the item at the specified index. If no index is provided, it removes and returns the last item.
```
my_list = [10, 20, 30, 40]
item = my_list.pop(1)
print(item)  # Output: 20
print(my_list)  # Output: [10, 30, 40]
```
##### index(item)
Returns the index of the first occurrence of the specified item in the list. Raises a ValueError if the item is not found.
```
my_list = ['a', 'b', 'c', 'd']
index = my_list.index('c')
print(index)  # Output: 2
```
There are many more methods like sort, remove and etc. 

- Advice about work with dictionaries, including adding, modifying, and accessing keys and values.
Dictionaries uses a key value pair data type which can be used to store other data types specified to a 
unique key. They key has to be unique and it is stored as a hash value, thus a duplicate value cannot be used.
Moreover, it is used as a memory in cases where we want to store a value associating with a specific key
which can be used to check whether that value exists or not. Likewise, we can get the value with a time complexity of
O(1), which makes it very efficient to search for the key rather than storing it inside a list. Usually,
string, int, tuples etc(immutable objects) can be used as keys.
    ```
    #to create a dictionary
    my_dict = {"name": "Alice", "age": 30, "city": "New York"}
    
    #to access the value
    print(my_dict["name"])  # Output: Alice
    
    #adding or modifying
    my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
    my_dict["age"] = 31  # Modifying an existing value
    
    # checking if the key exists
    print("age" in my_dict)  # Output: True
    print("gender" in my_dict)  # Output: False
    
    # deleting a key-value pair
    del my_dict["city"]  # Removing a key-value pair
    
    # accessing the keys, values and items which are both and values together inside a tuple of a list
    keys = my_dict.keys()
    values = my_dict.values()
    items = my_dict.items()
    
    print(keys)  # Output: dict_keys(['name', 'age', 'email'])
    print(values)  # Output: dict_values(['Alice', 31, 'alice@example.com'])
    print(items)  # Output: dict_items([('name', 'Alice'), ('age', 31), ('email', 'alice@example.com')])
    
    #iterating over a dictionary and printing their values
    for key in my_dict:
        print(key, "->", my_dict[key])  # Output: name -> Alice, age -> 31, email -> alice@example.com
    ```

## 5 Exception Handling:
- Write a code that handles exceptions using try and except blocks.
     ```
     def check_if_even(num):
        try:
            # Check if num is an integer
            if type(num) is not int:
                raise TypeError("Input must be an integer")
    
            # Check if the number is even
            if num % 2 == 0:
                return True
            else:
                return False
    
        except TypeError as e:
            print("Error:", e)
            return None
    
    # Test the function with valid and invalid inputs
    val1 = check_if_even(5)  # Not an integer
    print(val1)  # Output: Error: Input must be an integer
    val2 = check_if_even(4)  # Valid input
    print(val2)  # Output: True
    
     ```
- Tell us about the purpose of the finally block.
The finally block is executed regardless of whether an exception is raised or not
    ```
    def check_if_even(num):
        try:
            # Check if num is an integer
            if type(num) is not int:
                raise TypeError("Input must be an integer")
    
            # Check if the number is even
            if num % 2 == 0:
                return True
            else:
                return False
    
        except TypeError as e:
            print("Error:", e)
            return None
    
        finally:
            # This block will be executed regardless of an exception
            print("Cleanup or finalization code can go here")
    
    # Test the function with valid and invalid inputs
    val1 = check_if_even(5)  # Not an integer
    print(val1)  # Output: Error: Input must be an integer
    val2 = check_if_even(4)  # Valid input
    print(val2)  # Output: True
    ```
I have added a finally block after the except block.
The code in the finally block will execute regardless of whether an exception is raised.
```
#output
Error: Input must be an integer
Cleanup or finalization code can go here
True
Cleanup or finalization code can go here
```

## 6 File Handling:
- Provide a code to read from and write to a text file.
- Explain the difference between reading modes ('r', 'w', 'a')


## 7 Object-Oriented Programming (OOP)
- Tell us about your understanding about the basics of classes and objects in
Python.
A class is a blueprint for creating objects. It defines the structure and behavior of the objects that will be created based on it. A class encapsulates data (attributes) and functions (methods) that operate on that data. It's a way to organize and model concepts in your program. We can represent the human world using objects and attributes, which helps us to write pogrammes which can be associated to solve real world problems

- Create a simple class with attributes and methods.
One example could be of a human class with attributes
    ```
    class Human:
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
    
        def introduce(self):
            return f"Hello, I'm {self.name}, {self.age} years old, {self.gender}."
    
    # Create instances of the Human class
    person1 = Human("Alice", 30, "female")
    person2 = Human("Bob", 25, "male")
    
    # Introduce the persons
    print(person1.introduce()) # Hello, I'm Alice, 30 years old, female.
    print(person2.introduce()) # Hello, I'm Bob, 25 years old, male.
    ```

## 8 Modules and Libraries
- Tell us about the importing and using external modules (e.g., math , random ).
- 

- Tell us about the purpose of commonly used libraries like os , sys , or
datetime .

## 9 Basic Algorithms and Problem Solving
- Present a coding problem that involves iterating over data and performing a
simple operation (e.g., finding the sum of all even numbers in a list).
```
nums = [1, 2, 3, 4, 5, 6]

total_sum = 0

#Calculate the sum of all even numbers in the list
for num in nums:
    if num % 2 == 0: #if the num in the list is even the modulo operator returns the remainder of the calculation
    # which results in 0 if the num is even
        total_sum += num

print(total_sum)
```


## 10 Coding Exercises
- Write a Python code that could solve a problem by include tasks like reversing
a string, calculating Fibonacci numbers, or implementing a simple data
structure.

Reverse String
```
def reverse_string(input_str):
    """Reverse the given string using a for loop."""
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

# Get user input
user_input = input("Enter a string: ")

# Call the function to reverse the string
reversed_str = reverse_string(user_input)

# Print the reversed string
print("Reversed string:", reversed_str)
```

Fibonacci numbers optimized using memory and implementing a simple data structure, time complexity O(n) and memory O(n)
```
d = { 0 : 0, 1: 1}

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 1:
        return d[n] # using the memory so that same calculation is not required
    else:
        if n in d:
            return d[n]
        fib1 = fibonacci(n-1)
        fib2 = fibonacci(n-2)
        fib = fib1 + fib2
        d[n] = fib #storing it inside memory so that the same calculation is not required
        return d[n]

# Get the value of n from the user
n = int(input("Enter a non-negative integer (n): "))

# Check for valid input
if n < 0:
    print("Please enter a non-negative integer.")
else:
    # Calculate and display the Fibonacci series up to the nth term
    print("Fibonacci sequence up to the", n, "th term:")
    for i in range(n):
        print(fibonacci(i), end=" ")
```

## 11 Version Control
- Tell us about your understanding of basic Git commands.
Git is a technology used for version control. It helps out to maintain code and code version, this helps us to keep track of the codes we have written and collaborate with other developers. Likewise, helps us to maintain a repository and roll back to older version incase the current version of application breaks. Furthermore, we can use it for varying purposes such CICD, branching, issue tracking, documenting and etc.
few basic commands:

to see the documentation
```
git --help
```
to see the current status
```
git status
```
to add all files for staging
```
git add .
```
to commit the staged files with a message
```
git commit -m "{message to be written}"
```
to push it to a branch named master
```
git push origin master
```
In all these cases, the configuration is set along with authentication and the remote origin is also set to the repository.
    

