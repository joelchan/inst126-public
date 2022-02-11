Welcome back!

Today we continue learning about functions.

---

### Announcements/logistics
- Samar's office hours are now confirmed! See syllabus for schedule; there are slots today 5-6p
- This week, after you complete the first two PCEs, would be a good time to start the Project, before Tuesday's class. You will likely not succeed, but you will be better prepared to learn
- LC for functions is now live

---

### Game plan
1. Quick verbal review of functions
2. In-class programming
3. Revisit errors with functions

---

### Quick verbal review

---

Two parts writing programs with functions?

---

1. Function *definition*
```python
def some_function(a):
	result = a*2
	return result
```

2. Function *call*
```python
something = 3
print(some_function(something))
```

---

Which one's the argument and which one's the parameter?
```python
def some_function(a):
	result = a*2
	return result

something = 3
print(some_function(something))
```

---

`a` is a parameter

`something` is an argument

---

How does python know what value to give `a` in the function?
```python
def some_function(a):
	result = a*2
	return result

something = 3
print(some_function(something))
```

---

When you call a function, the argument's value is assigned to the matching parameter, which can then be used in the function body

---

What's the relationship between functions and variables?

---

Functions are like variables in that they are boxes with names that Python stores stuff in (code for functions, values for variables)

Arguments are to parameters what value are to variables; when you call a function, the argument's value is assigned to the matching parameter, just like a variable assignment statement assigns a value to a variable.

---

### Time to program!

---

### Common errors in functions