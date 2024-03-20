# Example Python Weather Project - Advanced Syntax
This repo contains an example of one way to solve the Python Weather project for the She Codes Plus Python unit.

You're currently looking at the `advanced_syntax` branch of this repo. This is an alternative solution to the project that uses "list comprehensions". 

## List Comprehensions
A handy and powerful piece of syntax that you'll see for the first time in this demonstration is a "list comprehension". 

This is a technique in python that lets us generate a list on the fly, using similar syntax to a `for` loop.

Since this is brand new, we'll quickly look at some examples here:


### What We Are Replacing:
As you know, we can add items to a list with a `for` loop, like so:

```py
input_list = [0, 1, 2, 3]

list_of_squares = [] # starting with an empty list

# Adding strings to it one by one...
for each_number in input_list:
    list_of_squares.append(each_number**2)

print(list_of_squares)
```

> The result:
> 
> ![](./img/four_strings.png)

This is how we solved it in the `main` branch example. The `for` loop works just fine, but it requires a few lines of code. It's such a simple task. If only we could do this in one line!

### Using A Comprehension Instead
The syntax for a list comprehension looks like we squashed a `for` loop into the square brackets of a list. Here's how we would convert the above example to a comprehension:

```py
input_list = [0, 1, 2, 3]

list_of_squares = [each_number**2 for each_number in input_list]

print(list_of_squares)
```

> The result is the same!
> 
> ![](./img/four_strings.png)

See how that works? I've named my loop variable `each_number` to make the syntax as close to a plain English sentence as possible. 

The square brackets indicate that we are creating a list. Then we specify an operation (in this case, squaring) that we want to perform on each number in some iterable. I think this is more readable. It's also slightly faster!

You'll find a couple more examples of list comprehensions in this example project solution. 

You may be interested to know that you can also write dictionary comprehensions and set comprehensions. It works exactly how you'd expect:

```py
# A dictionary comprehension:

input_list = [0, 1, 2, 3]

square_dict = {each_number: each_number**2 for each_number in input_list}
```

```py
# A set comprehension:

input_list = [0, 1, 2, 3]

{each_number**2 for each_number in input_list}
```