Many of you have expressed uncertainty about how to get started on the PCEs. It seems overwhelming and you're not sure where to start. 

This is normal and ok. And there is a way to deal with it.

## The basic pattern for getting started.

We'll discuss this in much more detail in the next module when we discuss problem formulation, but the basic steps are:
1. Take that large problem and break it down into smaller problems you can solve. 
2. Solve those problems.
3. Attempt to stitch the solutions together. 

Sometimes step 3 might spark new problems to solve, or require you to modify those solutions. Rinse and repeat from Step 1.

Concretely, in the PCEs you always have two big subproblems:
1. Write the code that does the work the question is asking for
2. Put that code into a function

Once you get familiar with functions, you may find it is possible to do both steps at once by just writing the code in the function definition cell and testing it.

But I recommend for now at least (and probably always!) creating new cells *above* the initial function definition cell to think through and solve the subproblems of the main thing being asked for.

## Example 1: Q1 of Variables and Expressions PCE

Let's take the example of Q1 from the variables PCE

Here is what you see to start with:
![](../resources/Pasted%20image%2020220207112854.png)
It looks daunting! Where do you start?

### Formulating and writing code for the first subproblem

Here's a way to tackle it. Start by creating a "scratchpad" cell above the function definition cell. Highlight the function definition cell and select from the menubar `Insert > Insert Cell Above`

![](../resources/Pasted%20image%2020220207113002.png)
Now let's go back and read the description of the problem. Look for key verbs and statements. Here, we see that the code takes in two numbers, and returns their *sum*. That's our clue on what to test out first in the scratchpad cell. Let's write that in comments. This is the step of **breaking down the problem**. 

![](../resources/Pasted%20image%2020220207113148.png)
Now we need to figure out what code to write in the cell to solve the subproblem. This is the step of **solving the broken down problem**. 

We know we eventually need this to be in a function, but we can worry about that later. For now, focus on the fact that we know we need to write a Python chunk of code that computes the sum of two numbers. How do we do that?

As you learn more, you will be able to write most of this from your head. But not always! And certainly not now. So what to do?

I suggest you go back to the lecture notes, or Google, but with the specific question in mind "How do I compute the sum of two numbers in Python?" 

Let's think this through. This is a chunk of code that is producing something. So it's... probably an expression? I know what the values are (two numbers), I just need to figure out what the operator is.

Let's look at the lecture notes from Week 2 Day 1, where we discussed types of operations.
![](../resources/Pasted%20image%2020220207113521.png)
We can see here that we have an operator `+` that seems to fit the bill, since it maps to arithmetic operations. Let's try that!

We go back to our cell, and see if we can make addition happen.

![](../resources/Pasted%20image%2020220207213028.png)

Success! We have an expression that adds two numbers. What next?

### Formulating and writing code for the second subproblem
The second subproblem is figuring out how to get the two numbers to add together. The problem says that the program should work for any two numbers, and that the numbers are given. How do we get the numbers?

Any number... any number suggests a variable. So we need to modify the expression so that it works with variables, not literal numbers.

For now, we'll need to define the variables to make it work.
![](../resources/Pasted%20image%2020220207213112.png)

Viola! What next?

### Stitching things together

Here is where we need to interface with functions a bit, and I think where we are getting confused.

Let's look back at the function definition cell. 

![](../resources/Pasted%20image%2020220207213126.png)

We see that there are `x` and `y` variables in the parentheses. These are the inputs to the function. They're our two numbers. They get their values when we *use* (or "call") the function. We'll talk about this this week in much more detail, but for now you can imagine that when this function runs, x and y are given values, and the line of code that does something with x and y doesn't need to worry about how. 

This means that we don't need the lines that define `x` and `y` to be in the function. That's taken care of already. So the only thing that needs to go into the function is the expression that operates on `x` and `y`.

As I said in class, I like the design pattern of always having a `result` variable that we put our result values in, and return that value. We can use this design pattern in basically all of our functions.

Like this: 
![](../resources/Pasted%20image%2020220207213304.png)

The result of the addition operation is what we want to return from the function as `output`. So we can put it on the right hand side of a variable assignment statement, to put the resulting value of `x + y` into the `result` variable.

Like this:
![](../resources/Pasted%20image%2020220207213413.png)
And just like that, we have a function! Note how I highlighted what we prototyped in terms of the component solution, and how it maps to the stitched-together solution in the function

*NOW* we can run the function definition cell and test our function in the next cell. I encourage you to mess with the values being assigned to the test variables to see if your expectations are met for what values should come out depending on different inputs. 

A common tell that something is wrong is if you change these variables and the output remains unchanged. Probably this means you hard-coded the variable values inside the function, instead of letting the values come from the function definition, as we discussed. Again, this will make more sense tomorrow.

## Example 2: Q4

Let's do this with one more example!

### Formulating and writing code for the first subproblem

First, let's make a cell above to formulate and write code for subproblems.
![](../resources/Pasted%20image%2020220207213531.png)

Ok, so what do we need to do here. We have a two variables coming in. They will be strings. But we want to do math with them. Can we do math with strings? No, we learned in class that **values constrain operators**. So I somehow need to make sure both variables are numbers that are `int` values, not strings. Let's write that first.

![](../resources/Pasted%20image%2020220207213712.png)

Ok how do I do that? How do I turn a `string` into an `int`? Let's go back to the lecture to see if something like this is covered. 

Aha! Looks like that's covered in this section:
![](../resources/Pasted%20image%2020220207213848.png)

And there's something here about casting functions, and some examples. But I'm not quite sure what's going on. Let me google.
![](../resources/Pasted%20image%2020220207214020.png)
Ah! Looks like it's something like "convert". Let's look closer.

At this link, it looks like there's something like "type conversion"
![](../resources/Pasted%20image%2020220207214130.png)
I notice the `int()` and `float()` things here look similar to what is in the lecture notes:
![](../resources/Pasted%20image%2020220207214300.png)
*Side note: in building this out, I realize I should do a better job of making sure you know what useful references are if I'm not going to show you all ways to do X, so you don't have to guess which source is going to do the trick.*

Let's give it a shot and see if it works!
![](../resources/Pasted%20image%2020220207214411.png)
Hmm it ran, but... did it work? How do I know? It looks the same.

### Formulating and writing code for the second subproblem

Oh, if it's actually an int, it should do math instead of treating it like a string. Let's do it with two and test by adding an expression to add them together. Wait! That's the other subproblem we need to solve anyway! Good thing we know how to write expressions that add two variables in the math sense!

![](../resources/Pasted%20image%2020220207214536.png)
Ok we'll know it works if the result here is 8, instead of 53. Let's run it.
![](../resources/Pasted%20image%2020220207214558.png)
Hurray!

Side note: I also did another thing here that we didn't talk about - you can update a variable by doing something with it, and assigning the resulting value back to the same variable name. I did this for brevity. But an equivalent would be to assign the type conversion result to a different variable, like this:

![](../resources/Pasted%20image%2020220207214742.png)
This would make sense if you want to make sure to distinguish from the variable name what its type is.

### Stitching it together

In any case, we have our component solution! Now to stitch it back together in the function.

First, let's put in the `result` variable pattern.
![](../resources/Pasted%20image%2020220207214938.png)
Now, as before, we don't need to define `x` and `y` when we're in the function if they're in the function definition as parameters. So we just need to put in the bit that takes in x and y and does stuff with them.

First, the bits that convert them into ints.

![](../resources/Pasted%20image%2020220207215136.png)

Then, the part that adds the two variables, which.. we know how to do from before!
![](../resources/Pasted%20image%2020220207215151.png)
And... run it and test it!

## In sum
Hope this is helpful! The key patterns here for getting started, to review:
2. **Formulate subproblems** from the big problem. Make a cell above the function definition cell and start filling this cell with one or more of these subproblems. Write them out in comments (or somewhere) else, in plain not-code language, what you need to do.
3. Figure out how to **write code** to tell Python to do those things, using the lecture notes and/or Google, with a pattern "<the thing you want to do> Python". Iterate on this with step 1 until you've solved all the subproblems.
4. When you've solved the subproblems and have something giving you the output you expect given inputs, **stitch the solutions together** into the function definition cell.