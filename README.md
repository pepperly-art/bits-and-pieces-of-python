# bits-and-pieces-of-python
little python projects / homework / etc used to learn

## links
[Python Cheat sheet](https://quickref.me/python.html) | [Future Coder](https://futurecoder.io/course/) | [30 days of Python](https://github.com/Asabeneh/30-Days-Of-Python) | [learnxinyminutes](https://learnxinyminutes.com/python/) | [Formatting Strings](https://www.programiz.com/python-programming/methods/string/format)

I think "learnxinyminutes" is probably all the notes I really need to worry about...?

## things I've learndeded

### AgeTest.py

- [import datetime](https://www.w3schools.com/python/python_datetime.asp)
- [while x is None](https://www.reddit.com/r/learnpython/comments/1blfl9e/comment/kw61i97/), None being a way to represent the absence of a value. For some reason(?????) I still have to define it as None or it throws an error.

### Extra Notes

- if you are getting weird errors, dump the terminal with the trashcan 🗑️
- and has a higher priority than or.
    Either add parentheses to be safe or break up your expression into smaller parts and assign each part to a variable. This will make your code clear, readable, and unambiguous, and will save you from painful mistakes.
- not has higher priority than or if there are no parentheses
- not also has higher priority than and

### Day 03 course comparisons

- is: Returns true if both variables are the same object(x is y)
- is not: Returns true if both variables are not the same object(x is not y)
- in: Returns True if the queried list contains a certain item(x in y)
- not in: Returns True if the queried list doesn't have a certain item(x not in y)

```'
if x:
    return False
else:
    return True
```
is equal to
```
return not x
```

### Day 04 escape sequences
```
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")
```

### Day 05 list???
```
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
```
*rest ????? neat

### Day 7 set
```
out of order lists?
update([list, item]) to add things to the set
find things 'in' with 'item in set'
```

### Day 8 set
```
Accessing with [] is cool when there's a list or dict inside the dict, like
entry['key1']['subkey0'] or 
entry['key2'][0]

entry.get('invalid_key') can get it similarly, but will be None if not there
```

## Day 9 set
- conditionals!
- remember:
- greaterthan or equal to >=
- lessthan or equal to <=