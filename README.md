

---

# Python Functions 

Welcome to your **Python Functions** crash course! This lesson will walk you through the basics of creating and using functions in Python. Simple language, simple code, powerful skills.

---

## 📌 What Is a Function?

A **function** is a block of code that only runs when it's called. You can pass data into a function, and it can return data as a result.

### ✅ Why Use Functions?

- Keeps your code **organized**  
- Avoids repetition (DRY principle: Don't Repeat Yourself)  
- Makes code **easier to read and debug**  
- Helps with **reusability** in larger programs  

---

## 🧠 Learning Goals

By the end of this, you’ll be able to:

1. Write your own functions  
2. Use arguments and return values  
3. Understand function scope  
4. Use default, variable, and keyword arguments  
5. Work with small extras like `lambda` and decorators  

---

## 🧩 Table of Contents

1. Basic Function  
2. Arguments  
3. Return Values  
4. Default Arguments  
5. *args and **kwargs  
6. Lambda Functions  
7. Function Scope  
8. Decorators (Intro)  
9. Practice Exercises  
10. More Learning Links  

---

## 1. 📌 Basic Function

```python
def greet():
    print("Hello, world!")

greet()
```

---

## 2. 🧾 Arguments

```python
def greet_user(name):
    print("Hello, " + name)

greet_user("Sarah")
```

---

## 3. 🔁 Return Values

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

---

## 4. ⚙️ Default Arguments

```python
def greet(name="friend"):
    print("Hello, " + name)

greet()
greet("Lerato")
```

---

## 5. 📦 *args and **kwargs

```python
def total(*numbers):
    print(sum(numbers))

total(2, 4, 6)

def print_info(**info):
    print(info)

print_info(name="Alex", age=30)
```

---

## 6. ⚡ Lambda Functions

```python
square = lambda x: x * x
print(square(4))
```

---

## 7. 🔒 Function Scope

```python
def show():
    message = "Hello inside"
    print(message)

show()
# print(message)  # This will give an error – variable not available outside the function
```

---

## 8. 🎁 Decorators (Intro)

```python
def decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@decorator
def say_hi():
    print("Hi!")

say_hi()
```

---

## 9. 📝 Practice Exercises

Try writing these on your own:

- A function to multiply two numbers  
- A function that returns "Even" or "Odd" based on a number  
- A function that greets a list of names  
- A function that calculates the factorial of a number using recursion  
- A lambda function that adds 10 to a given number  

---

## 10. 🔗 More Learning Links

- [Python Docs – Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
- [W3Schools – Python Functions](https://www.w3schools.com/python/python_functions.asp)  
- [Real Python – Functions Guide](https://realpython.com/defining-your-own-python-function/)  
- [Programiz – Python Functions](https://www.programiz.com/python-programming/function)  
- [GeeksForGeeks – Python Functions](https://www.geeksforgeeks.org/python-functions/)  

---

## 💬 Final Thought

**Functions are your first real tool to write smarter Python. Master them early, and everything else becomes easier.**

Happy coding! 🚀

---
