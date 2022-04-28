
### Announcements:
- ncaa dataset (for Problem 2, Project 4) already has win/loss ratio calculated: no need to calculate it

### PCE notes

Q5
- `unbound local error result referenced before assignment` happens if you don't cover all possible cases, and you never get into an if/else branch that assigns a value to `result` before you return it. fix is to cover all the 6 cases!

Q3
- common error: not saving results of not in place operation
- the first "ascending" parameter in `df.sort_values(by=col, ascending=ascending)` is the parameter for the `sort_values()` method. 

Note: there are errors in the test cases for Q3 and Q4 that will cause the tests to fail even if the output is correct. Pushing a fix tonight/tomorrow.