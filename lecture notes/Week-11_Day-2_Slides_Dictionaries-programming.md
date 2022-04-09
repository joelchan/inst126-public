Welcome!

Today we will practice working with dictionaries.

---

### Announcements
- Project 2 grades are out today
- 

---

### Game plan
- In-class programming!

---

### In-class programming

Notes:

#### Q1: Create a dictionary

**error/issue**: used literal values for keys and values instead of the input params

```python
def make_dict(k, v): # fill out / check the parameters
    # we're making a dictionary where the key has the value of the
    # parameter k, and it's mapped to the value of the param v
    dictionary = {'k': 'v'}
    return dictionary # write the return value
```

**fix**: remove the quotes around k and v so they are actually variables, not literal string values of `k` and `v`:

```python
def make_dict(k, v): # fill out / check the parameters
    # we're making a dictionary where the key has the value of the
    # parameter k, and it's mapped to the value of the param v
    dictionary = {k: v}
    return dictionary # write the return value
```

#### Q2: Create a (bigger) dictionary

**error/issue:** used different order for params than expected; ran as expected, but failed test. this is bc test function maps arguments to parameters based on *position/order*, whereas our function calls use keyword arguments syntax, like `thefunction(param1=arg1, param2=arg2)`, where the order doesn't matter bc we are directly mapping arguments to parameters by name instead of order. we will fix this in future PCE test functions so they use keyword argument syntax instead of generic argument syntax (e.g., `thefunction(arg1, arg2)`, but it's good to be aware that you might encounter generic argument syntax in other code in the wild.

**error/issue:** forgot comma between items --> syntax error.
```python
def make_dict_multiple(k1, v1, k2, v2): # fill out / check the parameters
    # write the body of the function
    dictionary = {
        k1: v1
        k2: v2
    }
    return dictionary # write the return value
```

**fix:** add comma between entries:
```python
def make_dict_multiple(k1, v1, k2, v2): # fill out / check the parameters
    # write the body of the function
    dictionary = {
        k1: v1,
        k2: v2
    }
    return dictionary # write the return value
```


**fix: **

#### Q3: Access items from a dictionary

**error/issue:** made a dictionary inside the function instead of using the input param. may return key for specific dictionary, but will definitely fail test bc it works *only* for that *exact* dictionary, ignoring the parameter that holds the input dictionary.

```python
def get_details(d, key): # fill out / check the parameters
  # write the body of the function
    # make a dictionary with these keys and values
    dictionary = {
      'laptop_brand': 'Apple',
      'laptop_model': 'MacBook Air',
    }
    return dictionary.get(key) # write the return value
```

**fix:** make sure you don't hard-code / define an input parameter. it may look strange now, but get used to it! your parameters get their value from the parameters in the function call! you do *not* need (and do not *want* to) define them in the body of your function.

```python
```python
def get_details(d, key): # fill out / check the parameters
  # write the body of the function
    # make a dictionary with these keys and values
    return dictionary.get(key) # write the return value
```

DO NOT USE reserved words and keywords as variable names. Strange things will happen. `dict()`

#### Q4: add a new entry to a dictionary

mechanics of `.update()` - it takes a dictionary as an argument, where each `key-value` entry will result in an update/addition to the dictionary with that `key-value` pair

return `None` from a `.update()` call: you DO NOT WANT TO have a variable that receives a return value from a function call to a method call that modifies a mutable data structure like a list or dictionary

this function will return `None`:
```python
def add_entry(dict1, key, value): # fill out / check the parameters
    # write the body of the function
    dict2 = dict1.update({key: value})
    return dict2 # write the return value
```