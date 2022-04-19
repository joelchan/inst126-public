Welcome!

Today we will introduce Module 4, and revisit our discussion of ethics in programming.

---

### Announcements
- 

---

### Game plan
- Introduce Module 4
- Ethics 2

---
### Introducing Module 4
---

We are now focusing on an application of programming to info sci: data analysis!

---

By the end of this module, you will learn the skills that enable you to take something like this:

![](https://lh6.googleusercontent.com/TbFiGK3KQl65_00a_7IEG73xqPIepUquvsCRUkhsvwdj2CiIakcAXaxs4V8IyKdHvPJcXZ-iUE0rdOiMxvLRrBiGzpa6uEf8zIuJuNxXmu4fcaPvDkvLrgADBQBYCujs6SZkR5-q)

---

And generate something like this:

![](https://lh5.googleusercontent.com/jRBwmPNbldwZ_bPAE5VuBCQgZ7mVIp23ADfZ_QLkjjVKlZStHaT2VzgQZ0f9eOPjqNyV-YZhC4nkdcNhF-FjnquwFislGu9cnHO-N7RYhmLEVJI596Ng5upta2Ayu3yFiOc-Yd7y)

---

Or at least the dataset and answers (sans plot). 

This was an actual student project from Fall 2018! Slides from their final presentation here: https://drive.google.com/file/d/1cSw811UUgXY9x2nCk1M2b7_64MPYXEIS/view

---

The Project 4 problems are all variants of a data analysis problem.

---

We’ll learn a specific library called Pandas, which is a collection of data structures and functions that are very helpful for data analysis. You’ll also continue building on your understanding of functions, and control structures like conditionals and iteration, and strings for data cleaning.

---

You’ll start trying to think through the parts of the problem, then get feedback on a potential formulation pattern in Week 14 that articulates how to solve problems like this

---

Let's look at an example notebook!

---

### Ethics 2

---

Review: what are values?

Values are not features.

They're deeper: they're the *why* behind features.

---

**Why** do you want the page to load faster?

**Why** do you want to recommend items that are similar to what you've already seen?

**Why** do you not have two-factor authentication?

---

Examples:

---

**Feature: [auto closed captioning on Zoom](https://www.theverge.com/2021/2/25/22300740/zoom-live-transcription-closed-captions-accessibility-free-accounts)**

Value(s)?: accessibility, lowering the barrier to accessibility
Gaps/tensions?: don't just use English; make sure you account for diff. accents and languages

---

**Feature: [Twitter safety mode](https://www.theverge.com/2021/2/25/22301388/twitter-auto-block-mute-abusive-accounts-safety-mode) (auto-muting accounts that are being abusive)**

Value(s)?: online safety, inclusivity
Gaps/tensions?: procedural justice; inclusivity across cultural variations; free speech

---

**Feature: [DeepNostalgia from MyHeritage](https://www.theverge.com/2021/2/28/22306097/ai-brings-still-photos-life-meme-twitter-geneaology-myheritage)**

Value(s)?
Gaps/tensions?

---

**Feature: [automatically suggest tags for photos on Facebook](https://www.theverge.com/2021/2/27/22304618/judge-approves-facebook-privacy-settlement-illinois-facial-recognition)**

Value(s)?: convenience
Gaps/tensions?: privacy considerations

---

### Values are important to consider during problem formulation

---

One reason values matter is that they can be "blind spots" that leave open the door for great harm to occur. They can also leave us blind to great opportunity!

---

We decide what technology gets built. This also means we decide what technology doesn't get built. A lot of this is governed by what we do or do not value (or what our balance of priorities for values are).

---

Sometimes a mismatch in (unspoken) values can lead to harms from gaps in what does get built.

---

Examples from [this discussion of gender bias in design](https://www.evoke.org/articles/july-2019/data-driven/deep_dives/the-dangers-of-gender-bias-in-design) show how valuing cost efficiency over, say, inclusivity, can have deadly consequences

![](../resources/CleanShot%202022-04-18%20at%2022.44.44.png)

---

So values are one big piece of the puzzle for ethical programming: being mindful from the very beginning, before you write your first line of code, what values are (not) shaping what you will build

---

### How do we anticipate/mitigate harms from what we build?

---

Being aware of our values is only one step. 

We still need to figure out if mismatches/tensions in our values will lead to harm and if so how to mitigate those harms or even decide that we shouldn’t build something!

---

This is fundamental to the ACM Code of Ethics: [https://www.acm.org/code-of-ethics](https://www.acm.org/code-of-ethics)

![](https://lh5.googleusercontent.com/49atZjCYETW9VzoUWLjahBQnrbYsFIemNSiEqcOScrQlIps4eSMKI2QwssYrqmifpwRGqW9THW1vyB6-oGxRtjpMliwa_xCVhVmNTAyw9xmwNCkDTMIhvyK-3hASKlNZB6kHLH5a)

---


One example is the ongoing debate over the cost/benefit analysis of large language models like GPT-3. 

---

Here is an example of what these models might enable: [https://twitter.com/jungofthewon/status/1357868753476677635](https://twitter.com/jungofthewon/status/1357868753476677635)

![](../resources/CleanShot%202022-04-18%20at%2022.51.45.png)

---

But there are also potential harms and misuses:

- These models work by drawing from GIANT datasets of text from the Internet that are very hard to audit for quality or bias. This can (and has been demonstrated to) lead to harmful or biased language outputs
- What could happen if the cost of mass-producing plausible text went to basically zero? What could propagandists, spammers, and others do?

---

For more details, see OpenAI’s [blogpost](https://openai.com/blog/better-language-models/) on this for the smaller GPT-2 model that was published in 2019, and coverage of it in [the Verge](https://www.theverge.com/2019/2/21/18234500/ai-ethics-debate-researchers-harmful-programs-openai). 

The company is continuing this trend with their GPT-3 model, which was released in 2020 (see some discussion of its potential harms [here](https://techcrunch.com/2020/08/07/here-are-a-few-ways-gpt-3-can-go-wrong/))

---

Recent example: using large language models to include ["inclusive warning" suggestions for writing in Google Docs](https://www.vice.com/en/article/v7dk8m/googles-ai-powered-inclusive-warnings-feature-is-very-broken:
![](../resources/CleanShot%202022-04-19%20at%2014.14.58.png)

---

Here is a potential harm that surprised me:
![](../resources/CleanShot%202022-04-19%20at%2014.13.48.png)

---

![](../resources/CleanShot%202022-04-19%20at%2014.14.24.png)

---

**So how do we mitigate/anticipate these harms?**

---

OpenAI is dealing with this by [carefully controlling access to their full model with private beta and other safety mechanisms](https://openai.com/blog/openai-api/).

This is a variant of the idea of: "red" teaming your ideas. Some call worst-case scenario thinking" or "design fictions".

---

Let's get a feel for this!

What's the worst-case scenario for  [Twitter safety mode](https://www.theverge.com/2021/2/25/22301388/twitter-auto-block-mute-abusive-accounts-safety-mode) (auto-muting accounts that are being abusive)

Brainstorm on Miro board

---

What about [DeepNostalgia from MyHeritage](https://www.theverge.com/2021/2/28/22306097/ai-brings-still-photos-life-meme-twitter-geneaology-myheritage)?

Again, brainstorm on Miro board

---

One insight is that red-teaming is tough if the people you do this with have the same blind spots as you! 

So another powerful idea: make sure you engage people who can surprise you.

- Diverse teams
- Intentional user and stakeholder engagement

---

Some researchers and practitioners have also experimented with toolkits for structuring conversations and thinking on this: https://ethicalexplorer.org/

![](../resources/CleanShot%202022-04-18%20at%2023.01.42.png)

---

I've uploaded copies of the ethical explorer field guide and risk zone cards to the course Github repo:
- [Field-Guide](../resources/Field-Guide.pdf)
- [Tech-Risk-Zones](../resources/Tech-Risk-Zones.pdf)

---

To help you practice and get a feel for how difficult this task can be (and brainstorm/practice ideas for making it better), your 2nd ethics assignment will involve a “design worst case scenario” exercise, where you take the piece of tech you picked for your first ethics quest, and write a “black mirror” story of the worst possible scenario you could imagine that involved the technology.
