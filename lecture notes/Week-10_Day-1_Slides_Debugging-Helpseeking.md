Welcome!

Today we will learn about debugging strategies.

---
### Game plan
- Review functions: arguments and parameters
- Incremental problem solving
- Talk about and practice Debugging
	- If time: with some real examples from your PCEs
---

## Functions
---

Seeing these errors repeatedly in office hours. Warrants review of functions:
- Function gives expected output (printed out), but fails tests
- Function gives none

In all cases, there is an issue with parameters and arguments, so let's review!

---

One common error: hard-coding the parameters inside the function.
![](../resources/CleanShot%202022-03-29%20at%2016.16.17.png)

---

It may seem like the function is working as expected only if the cell where you call the function has values that are exactly the same as what is hard-coded in the cell.

Like this:
![](../resources/CleanShot%202022-03-29%20at%2016.16.51.png)

---

But you can catch it if you test it with a different set of values for the arguments you are passing into the parameters in the function call, and notice that it's giving the exact same output as before.
![](../resources/CleanShot%202022-03-29%20at%2016.17.37.png)

---

What's happening is you're ignoring the parameters, and the function only works for this exact set of values. It will effectively ignore the function call.

This is why it fails the test function even though it seems to "work" for the one test case.

---

Another error is operating on the *arguments* instead of the parameters. Like this:
![](../resources/CleanShot%202022-03-29%20at%2016.19.46.png)

---

Here, we are are ignoring the `string` and `direction` parameters, and instead operating on `s` and `dir`, which are the *arguments* being passed into the function in the function call.

---

This is harder to catch, because changing the values of the arguments in the test cell will still give you expected output. 
![](../resources/CleanShot%202022-03-29%20at%2016.20.33.png)

It only fails when you run it through the test function.

---

In both cases, there is a fundamental misunderstanding about how arguments and parameters work.

To review: You don't need to define the value of function parameters. They get their value from the *arguments* in the function call.

---

In sum: Anytime your function seems to work as expected, even when you test it a few ways, and it fails the test function, you should consider checking whether your function is operating correctly on its parameters.

---
## Incremental problem solving

Another repeated theme in office hours: feeling overwhelmed, not sure where to start.

I want to show you something that works well for me, follows from the problem formulation skill, and helped multiple people get unstuck in office hours.

(demonstrated at around 12:00 in the lecture recording).

---

Let's talk about bugs!

---

## What are bugs and debugging and why should we care about them?

---

Fun fact: in computing, there is [lore](https://en.wikipedia.org/wiki/Software_bug) that says the term "bug" can be traced to Grace Hopper finding a moth in the computer that caused a system error!

![](https://lh4.googleusercontent.com/OoyCJ3wMRxnHqtUFdQNzPoJURADLbC9hL_b5MaI9qQgx32ykHI7YrFOgOJcKiohJagPG6GUHnyIRS4-2_ev7RXRG_b9jOwmwwkxTEwnlS3sJ75ualR6ORjfhfE_6C3itfjWc_1Tn)

---

Bugs are basically problems in our code that make the program **do something different than what we want**.

---

Bugs are a fact of life. We all make mistakes. Basically nobody writes perfect code the first time for any real problem.

One estimate is that professional programmers spend about 35-50 percent of their time validating and debugging software.

---

So debugging is actually a fundamental computational thinking skill.

---

## How NOT to debug

---

The biggest mistake I see beginners make: keep changing things to make errors go away. 

Why did you do that? No idea... just want to tinker to see if "works"

![](https://lh4.googleusercontent.com/THn-ayOsghNTqG8qiYYCIGA96eA3CoV9ds11C1YMMl8O01v4OrkLlpvt4l2gsBQe6nZr6I3ydH-gHY4L1stVvEoxQEhjV7X-gkIEs7-VJuopy-H7wTR2pp17jC-o3biCMU6CjHor)

---

Why is this not productive/effective?

---

Often there are many different things going wrong. We want to keep track of what's happening and under what conditions so our "fixes" don't create new problems (this happens more often than you’d think!)!

---

Also this is really really inefficient, and eventually stops working when you’re attacking problems of realistic scale (e.g., towards the end of this class, or in INST 326).

In fact, it may have already stopped working for you.

---

## How to debug

---

The fundamental concept of debugging is **interrogating and refining a mental model of your code**: what is it actually doing? And how does it match up with what you *want* it to do?

---

This is because the root cause of a bug is a mismatch between what you want to happen, and what you're telling the computer to make happen (which is what will actually happen)

---

Sometimes it's a mismatch in syntax: you know what you want to happen, but you didn't express it in legal code. 

---

More commonly, it's a mismatch between what you thought you told the computer to do, and what you actually did.

You told the computer to do something, and it did, but what you said wasn't actually what you wanted/needed to happen.

---

In both cases, clarity on your *intent* is critical. 

This is why debugging is tightly related to problem formulation - the better and more explicit your model, the better you'll be able to pinpoint where something is going wrong

---

Here are some practical strategies and principles for debugging:

---

### Error messages as miscommunication detection

Frequently your program will need to be debugged not because the program was not "legal code", but because it produces unexpected behavior.

But sometimes you do get error messages, and it's useful to learn how to read them. We've talked about this before but let's review!

---


![|1200](../resources/CleanShot%202022-03-29%20at%2012.27.33.png)

Error code and message: useful for understanding the general types of reasons you might be seeing your problem, maps to common fixes

---

But! Also identifies mismatches between your intent/assumptions and what you're communicating to Python
- E.g., type error: you're expecting a value to be of a certain type, but it's not
- E.g., syntax error: you're expecting a line of code to be legal, but it's not

---

![](../resources/CleanShot%202022-03-29%20at%2012.35.54.png)

**Traceback**: roughly where in the program Python noticed that there was a problem.
- NOTE! This is not necessarily where the problem is! Often the problem (and fix) is located upstream
- But it is still a useful place to start

---

Remember: These error messages only show up for “syntax errors” (i.e., problems that stem from us not giving legal code to Python); they may or may not show up for semantic errors (i.e., problems that stem from us giving legal code to Python, but it’s different from what we actually want it to do).

---

### From "it's not working" to checking assumptions

---

The most common thing I hear when students ask for help is, "It's not working". 

We need to shift from "it's not working", to "i expected x, and i got y", or ". This requires something more specific than "i expected it to work, and it didn't!"

---

This is a massive bang-for-your-buck habit change to target.

Here are ways to get there:

---

#### Explicitly articulate your mental model

---

Be explicit about your mental model: what do you believe you are asking your code to do?

This is the job of our problem formulation!

And our [help-seeking template](https://github.com/joelchan/inst126-public/blob/master/Help-Seeking%20Template.md)

---

#### Document your code!

It also really helps to write comments for each line in your code: what is it actually doing? Is that the same as what it should be doing? Is anything missing?

---

You should try to write comments that are closer to your intended meaning / English, and not closer to pseudocode. 

Comments that simply restate the code (essentially) are not very useful. You should force yourself to think through what line of code is “actually” doing and whether it matches with what you want it to do.

---

### X-Ray your program to detect hidden miscommunications

---

In terms of detecting mismatches in your intent/assumptions vs. what you told Python when it's not a *syntax error*, you need strategies to "see what is happening" when your code is executing

---

Simplest is well-placed print statements!
If it's a loop, am I seeing multiple runs?
-   If I expect this data to be a string, can I verify that?
-   If I expect my data to be changing, can I see that?

---

There are also tools:
- Python tutor, which allows you to step through your code and see what is happening at each step
- Later you’ll start using something like an IDE (Integrated Development Environment)

---

### Systematic testing

---

Notice how we ask you to test your function in multiple ways? And our PCE scoring functions actually contain multiple test cases?

This is a core strategy that helps you to check your assumptions.

---
	    
Test cases are part of a more general strategy of automated testing, including “[unit testing](https://softwaretestingfundamentals.com/unit-testing/)" in professional practice, and is a cornerstone of effective programming, since it is somewhat feasible to use print statements to "see in your code" for the scale of programs you're working with rn, but is basically impossible for most real-world complex code bases.

---

###  Learn how to ask for help!

Last but not least, often it helps just to talk to someone or something out loud as you think through and work through the problem! Professional programmers call this "rubber duck debugging", a legendary method in software engineering practice: [https://rubberduckdebugging.com/](https://rubberduckdebugging.com/)

---

But there is actually a lot of commonality and inter-relatedness between debugging and help-seeking. So help-seeking strategies deserve their own discussion! Here is a short article with a step-by-step procedure that can really help you and help others help you efficiently and effectively: https://docs.google.com/document/d/1PXkXKko906a6zivJYvZQ8dMsLqFZ9RZbc5Aa4C-wWiw/edit?usp=sharing

---

That’s a lot of content! But this is quite effective and well worth practicing. 

---

To help you practice, your rubric for the final project deliverable will include the requirement that you include bug documentation, based on these help-seeking guidelines.

---
## Recommended resources:

[The Debugging Mindset - ACM Queue](https://queue.acm.org/detail.cfm?id=3068754) (excellent overview of the core concept of mental model mismatches being the root cause of bugs)

[How to debug small programs](https://ericlippert.com/2014/03/05/how-to-debug-small-programs/) (has some good overall ideas, plus pointers to more advanced techniques like assertions and unit testing)**