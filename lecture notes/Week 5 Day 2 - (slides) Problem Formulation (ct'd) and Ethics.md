Welcome!

Today we will continue our discussion of **problem formulation**, and integrate discussion and skills for how to do this **ethically**.

---

### Announcements / logistics
- Functions PCE grades should be up now.

---
### Learning outcomes for the week
- Construct a computational problem formulation for an English problem statement
- Analyze problem formulations in terms of their values

---
### Game plan
- Finish discussion of problem formulation
- In-context introduction to overall topics of module
- Discuss analyzing problem formulations in terms of their values

---

### Where we left off
Problem formulation:
- Is a critical computational thinking skill
- Consists of 3 things: **operations**, **data** (input/output), and  **logical flow** between operations
- Can and should be done before you code!

---

### We did this
![](../resources/Pasted%20image%2020220222172000.png)
https://miro.com/app/board/uXjVOKy70qY=/?moveToWidget=3458764519532731974&cot=14

---

### Functions and problem formulation

If you have a good problem formulation, you can write good functions that you can reuse. The mapping is kind of like this:
![](../resources/Pasted%20image%2020220222125647.png)

---
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

Let's code up one of these examples, so you can get a flavor of how this moves forward into coding, and get introduced to high level concepts in action for this module

---

### Beyond the "purely technical" for problem formulation

---

Now so far we've only talked about how a good problem formulation makes things "easier" (and probably results in a "better" overall program that solves the problem).

But good problem formulation should consider more than just the "purely technical". Understanding this is a crucial part of being a professional information scientist and programmer.

---

Let's consider an example: a form for data entry for payment. Needs to account for possible data entry errors.

Let's formulate the problem together.

---

Let's formulate another problem together: a contact tracing system for UMD students.

---

One last example: an algorithm for predicting health risk so we can direct more resources to patients who are sicker.

---

What did you notice in our exercises?

---

I want you to notice how *values* shaped what happened in the problem formulation.

---

Values are *not the same as features*. Values determine the shape of the problem formulation. They determine what we leave out or include, and how we specify it.

You can think of values as higher- or deeper-level constraints and conceptions of what is Good.

---

So **problem formulation involves values**, whether you notice them or not. 

This will come up in more or less mundane settings, from data analysis (what counts as "extreme values", what does "clean data" mean, what is in/out of hte dataset), to visualization (do you encode as an explicit step a way to make the visualization accessible?). 

---

Sometimes not recognizing that these values are shaping your design decisions can lead to very different problem formulations, but also unintended consequences and harm for people whose values were not represented in your problem formulation, as we saw.

---

Sometimes a value isn’t so much missing altogether as deprioritized heavily in favor of something else, often unintentionally. 

---

For example, there is a big difference in your experience as a woman or POC on social media if you have scalable ways to block or bar unwanted attention, vs. just a manual process of individually blocking each interaction or even person. 

---

To get around this, people have hacked together blocklists and other workarounds to stem the often unbearable torrent of abuse. 

Do you think that, say, Twitter, doesn’t actually value making sure people are not harmed or abused? Or do the engineers perhaps not hold these values in the same way as some of their users?

---

I’m not necessarily saying that any one value set is better or worse in all cases. Often, it’s contextual. 

The point is not really to choose the right values (although sometimes it is!). 

The point is to recognize that values play an important shaping role, and to make sure that you check whether your values match up with the values of the people who will be impacted by what you build.

---

We’ll come back to this again throughout this semester (and definitely in the rest of your classes in the major). 

For now, I want you to practice this with your ethics assignment: take a piece of technology (from the news, etc.), and reflect on it: what values do you see encoded in the way they formulated the problem? What values are left out?
