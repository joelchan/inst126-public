Welcome!

Today we will continue learning about iteration.

---

### Announcements
- Take a moment to fill out the weekly check in!

---

### Game plan
- Quick note on problem formulation: how to get started, how to know it's 'good'
- That one bug from last time
- In-class programming!

---

A strong theme in office hours this past couple weeks is: I feel like I understand what problem formulation is, but I'm having trouble getting started.

Here's something that worked well in office hours, so I'm sharing it more widely.

---

You start by looking at the problem description.

First, focus on the verb phrases: what is being described as needing to *happen*, for the program (or user) to *do*?

These are your yellow stickies.

---

Second, focus on the noun phrases: what objects or data are being described? What are their characteristics?

These are your blue stickies.

---

Third, you look at each yellow, and ask: "Do I know how to do this already"? If not, you can probably break it down a bit into more specific yellows.

---

Finally, think about how the yellows are related. Is there a sensible order in which things need to happen? Are there conditional branches? Are there things that need to happen in some kind of loop (repeatedly)? 

These are your logical relationships between subparts.

---

How do you know it's "good"? 

Like we said, ultimate test is whether it helps you write (and debug) your programs deliberately and effectively.

---

To repeat from [Week 5 Day 1 - (slides) Problem Formulation](Week%205%20Day%201%20-%20(slides)%20Problem%20Formulation.md):

Here are some heuristics I look out for:
- Detailed enough that you start to be able to map them to functions or bits of code that you know how to write.
- Allows you to write and test parts of your problem in isolation from others.
- More helpful Google / Stack Overflow search results

---

### That one bug

---

### In-class programming!

---

Notes
- Q1
	- you need to know something about strings and characters
		- strings are like lists - they have length and sequence. more on this next week.
		- characters are just strings that are of length 1 (i.e., 1 character long)
	- invalid syntax
		- make sure you have examples of valid while loops
	- asterisk - nothing is happening
		- infinite loop - check if you are modifying your stopping condition inside your loop
	- attribute error - string object has no append
		- this is because strings can't do `.append()`; only lists can. it's a list method.
		- illustrates importance of keeping track of your key bits of data and their types
	- alt solution: can do without loops - is this ok?

Q2
* how to put into new list
	* `.append()`!
* function transform error
	* this happens when you are returning the function
	* illustrates importance of variable naming - happened bc confused function name with the variable name for the list
* works when i run it, but not when i test it (none)
	* remember to always include a value in the return statement!