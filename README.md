# Example Python Weather Project
This repo contains an example of one way to solve the Python Weather project for the She Codes Plus Python unit.

Keep in mind that what's set out here is not intended to show the only way to solve this project, or even the recommended way to solve it. If every Python mentor demonstrated their own preferred solution to the project, each one would be different. Python lets us build our own solutions to problems any way we like, and if your project passed all the tests, then you were successful!

Instead, this repo is designed to demonstrate some common Python idioms to you that might serve you well in future projects, and to introduce you to some powerful techniques that you might not have had time to research within the (very tight!) project deadline.

For this reason, don't be discouraged if this example solution looks foreign to you or is hard to understand! Being a programmer is a constant journey of learning new techniques. We have plenty of documentation linked in the comments of this solution, and you are encouraged to approach the mentors or post in the help channels to help you interpret and apply the techniques set out here.

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

This works just fine, but it requires a few lines of code. It's such a simple task. If only we could do this in one line!

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