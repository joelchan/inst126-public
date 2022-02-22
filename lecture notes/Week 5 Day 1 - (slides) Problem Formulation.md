Welcome!

This week we will revisit the fundamental skill of **problem formulation**, and practice it again together. 

We will also integrate discussion and skills for how to do this **ethically**.

---

### Announcements / logistics
- Variables and Expressions PCE grades and feedback posted (for current submissions), Functions will be posted by tonight.
- Sarah's office hours are virtual this week

---
### Learning outcomes for the week
- Construct a computational problem formulation for an English problem statement
- Analyze problem formulations in terms of their values

---
### Game plan
- Review conditionals
- Discuss and practice problem formulation

---
### Review conditionals

---

Other than practice, there seems to be one fundamental conceptual difficulty re: conditionals: understanding when/how to use the different blocks

---

Key point:
- If you only have two branches/possibilities you care about, just use if/else
- If you have more than two *mutually exclusive* branches/possibilities you care about, use nested *or* chained. Deciding between the two is a matter of logic

---

Another key point: multiple if statements are *not the same* as a chained or nested conditional. 

---

Let's practice together!

Follow along from here: https://education.launchcode.org/intro-to-professional-web-dev/chapters/booleans-and-conditionals/exercises.html

We may also get into here: https://csiplearninghub.com/python-if-else-conditional-statement-practice/

---

### What is problem formulation and why should we care about it?

---
Remember the overarching division between "solving problems" (computational thinking) and "coding" (giving instructions to the computer in Python) that we talked about in [Week 1 Day 1 - Introductions](Week%201%20Day%201%20-%20Introductions.md)?

---

A BIG part of computational thinking is **problem formulation**. 

To do real-world programming, you need to know more than how to write code. 

You need to be able to take a relatively vague problem like "get all the email addresses out of this file", and model the problem so that it can be solved by a computer.

---

Let's practice together!

As a user, I want to get all email addresses out of a file

Here: https://miro.com/app/board/uXjVOKy70qY=/

---

If you don't learn this skill (and it is a skill!) in this class, you *will* struggle in 326 and any other area where you're actually needing to *use* programming to solve information science problems.

---

Ex: note I got from a 326 instructor:

> "They are struggling with programming in general. Even though this is their second course, they ==don’t have much ability to think about how to solve problems==. We’re in the “I watched everything you did and followed but have absolutely no idea where to start” phase, even with very simple work. ==I suspect they are sneaking through 126 without learning what they need and suddenly have to create from scratch with me and are panicked=="

---

If you can't formulate a problem in computational terms, it doesn't matter whether you know how to write a legal conditional statement, or how to assign variables, and so on. 

You’ll know *how* to instruct the computer, but not what instructions to give it! The *what* comes from problem formulation. It’s absolutely critical!

---

### Anatomy of a problem formulation

---

The three key parts of a problem formulation are:
1. The key steps/**operations** of your program
2. The **data** that is going in and out of the steps/operations
3. The **logical flow** of how all the pieces fit together

Let's look back at our problem formulation example for these bits.

---

You should be able to think through these bits without knowing how to write the code for it! 

In fact, it's a **really good idea** to do this *before* you write any code, as we have discussed in [How to get started solving the PCEs](How%20to%20get%20started%20solving%20the%20PCEs.md). 

---

Your problem formulation doesn't have to be perfect or complete, and you will refine it as you go, but it will guide what you write, and help you think through your debugging and help-seeking as well.

This is why we have your first assignment for Project 2 be a problem formulation.

---

### More practice!
Let's look at another simple example: I'm going to give you a list of numbers, and I want you to give me back a list that only has odd numbers in it.

With a partner, take a first crack at this: What are the main substeps/**operations** in this problem, what **data** is going in/out of the operations, and what is the **logical flow** of how they fit together?

---

Now let's do it together, here: https://miro.com/app/board/uXjVOKy70qY=/?moveToWidget=3458764519532731974&cot=14

---

### Even more practice!
Let's look at slightly more complex example that we *definitely* don't know how to code yet: 

I'm going to give you a bunch of birth certificates (N=500,000), and I want you to tell me what the top 50 and top 10 baby names are, because I want to choose names that are recognizable (i.e., in the top 50), but not too common (top 10).

---

Now let's do it together, here: https://miro.com/app/board/uXjVOKy70qY=/?moveToWidget=3458764519532732816&cot=14

---

### Even more practice!
We're wanting to build a Discord bot for our class as a side quest (will likely attach extra credit to this).

One idea to start with is an in-built glossary - common terms, errors

Let's work on this together, here: https://miro.com/app/board/uXjVOKy70qY=/?moveToWidget=3458764519532982189&cot=14

---

### Functions and problem formulation

If you have a good problem formulation, you can write good functions that you can reuse. The mapping is kind of like this:
![](../resources/Pasted%20image%2020220222125647.png)
So one way to think about a program is as a series of *functions* that are related to each other in logical ways.

---

### How do you know if you have a good problem formulation?

---

There are probably some formal metrics that could apply in some limited cases. 

But I don't know them.

---

IME problem formulation is more of an art. 

Here are some heuristics I look out for:
- Detailed enough that you start to be able to map them to functions or bits of code that you know how to write.
- Allows you to write and test parts of your problem in isolation from others.
- More helpful Google / Stack Overflow search results

---

I also look for these affective/emotional/high-level senses:
- I feel like I can see the logical "structure" of my program. 
- The problem feels more managable: I recognize pieces I know how to tackle, and the ones I don't are specific in ways that makes it easier to learn / seek help

---


