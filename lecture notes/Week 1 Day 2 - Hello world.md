
Welcome back!

```python
print("Hello world!")
```

---

#### Announcements

- We have need for a **peer notetaker** in this class. If you're interested and available, please get in touch with me by email.

---

Our goals today:
- Get Jupyter up and running
- Build our intuition about how it works and how to program in it

---

#### Observations from pre-semester survey

---

You are amazing. I'm glad you're here! 

So much curiosity and energy.

---

If you're new to programming, you're in good company!
![[sp22 previous programming experience.png]]

---

If you're concerned about not being able to keep up, you're also in good company!

We would like to target this head-on. The course is designed for you to succeed.

Help us! Stop us, talk to us, as soon as you hit any snags. We are in this together.

---

#### Brief orientation to your computing environment: Jupyter

---

Jupyter is a "literate computing" environment: a computational notebook where you can read and write (and execute!) code alongside English.

![[Pasted image 20220126211120.png]]
   https://osf.io/h9gsd

---

Jupyter is one of the most popular of these environments. Ubiquitious in data science.

This means lots of access to learning materials, tutorials, ideas to play with, code snippets to remix, etc.

See, e.g., https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks

---

Computational notebooks are great for getting started:
- Tighter feedback loops because of interactive computing
- More narrative alongside code (great for “keeping the plot” as you program)

---

But! Computational notebooks can be a bit tricky to reason about, in terms of sequence and state. 

We'll get into that today. 

But also keep an eye on later this semester getting introduced to programming in scripts (aka the "normal way").

---

#### First look, kicking the tires

---

Let's first set up your working directory.

Pick a location on your computer's filesystem. It could be your Desktop, or Documents, or something else. Then create a folder for this class. 

This will be your **WORKING DIRECTORY**, This is where I want you to put all your files and notebooks for INST126. 

---

Everytime you work on a PCE or project, or open up lecture notes that are `.ipynb` files, you will do the same steps:
1. Download the `.ipynb` file (from ELMS, or github if you like), and save it to your **WORKING DIRECTORY**
2. Fire up Jupyter (if it's not already running)
3. Navigate to your **WORKING DIRECTORY** in Jupyter
4. Open the `.ipynb` file (notebook) and do stuff with it.

---

Now let's download our first `.ipynb` file to play with. Download (from ELMS or github) these notebooks:
- `Week 1 Day 2 - Intro to Jupyter.ipynb`
- `Week 1 Day 2 - Reasoning about kernel state and sequence, Hello world`

MAKE SURE YOU SAVE IT AS A `.ipynb` FILE, else you will not be able to open the notebook in Jupyter.

---

Now let's fire up Jupyter:
- From Anaconda Navigator, click "launch" for Jupyter Notebooks OR Open your Terminal (mac, linux) or Command Prompt (windows), then type `jupyter notebook` (VERIFY YOUR SPELLING), and press Enter
- You should see Jupyter Notebooks open in your browser.

---

Now, navigate to your **working directory** (you saved the file there, right??), and open the `Week 1 Day 2 - Intro to Jupyter` notebook.

Let's walk through it together.

---

#### Building more intuition about the kernel

---

The last thing we want to do together is build some more intuition about the kernel, and sequence of commands, and what's in the kernel environment.

Let's open and walk through the `Week 1 Day 2 - Week 1 Day 2 - Reasoning about kernel state and sequence, Hello world` notebook.

---
Great job today!

Don't forget to complete LC-01 by tomorrow.

And get a headstart on Variables for next week.