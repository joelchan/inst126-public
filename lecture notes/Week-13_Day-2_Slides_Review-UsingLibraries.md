### Announcements
- No learning check this week

---

### Game plan
- Translating problem formulation to code
- Files review / practice
- Brief intro to libraries

---
### Translating problem formulation to code
---

Target: a series of individual pieces where there are inputs and outputs (clearly understood in terms of their datatypes) and verbs in between

---

Once we have this, we can much more easily map to component skills we are learning. And search for it!

Protip: With your specific statement, search:
- Google: add "python" at the end. Often google will autocomplete nicely for you.
- Our github repository! 

It's also a good thing to add as comments in your code to guide your process

---

Let's look at some examples!

---

😟 check if the email address is in the emails" 

🙂 check if the email address (string) is in the emails (list of strings)

🙂 check if a string is in a list of strings

---

😟 go through the emails

🙂 go through the emails (list)

🙂 go through a list

---

😟 add the cleaned number to our results

🙂 add the cleaned number (int) to our results (list)

🙂 add int to list

---

Let's practice with some snapshots from your problem formulations!

---

Note: Sometimes a statement is too "big" and needs to be broken down more. And then make sure you have an understanding of each part that is clear about the data inputs/outputs

---

😟 "get a username out of an email"

🙂 "extract a username part (string) from an email (string)"

😃 "extract a username part (string), which is the left half of the `@` symbol (separator) in the email (string)"

😃 "break the email (string) into parts (list) based on the `@` symbol (separator)", THEN "get the first element of the parts (list)"

---

It's an iterative process! you try to get as detailed as you can, piece code together, and if it doesn't quite work, that's a cue that the way you formulated it might be wrong or unproductive, even if it's specific. But the specificity will still help you get going with code that you can look at

---

I *do* recommend that you try as much as possible at least for now to **write your code in pieces**. Not only does the specificity help you search; it also helps you *isolate* parts of your problem to write and test separately before putting them together.

---

Example: count how many times all of these usernames show up in the emails

---

Concept of the "starting and ending positions"

Follows from having a clear understanding of the pieces' inputs and outputs.

---

### Brief intro to libraries