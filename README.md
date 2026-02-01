# bits-and-pieces-of-python
little python projects / homework / etc used to learn

## links
[Python Cheat sheet](https://quickref.me/python.html) | [Future Coder](https://futurecoder.io/course/) | [30 days of Python](https://github.com/Asabeneh/30-Days-Of-Python)

## things I've learndeded

### AgeTest.py

- [import datetime](https://www.w3schools.com/python/python_datetime.asp)
- [while x is None](https://www.reddit.com/r/learnpython/comments/1blfl9e/comment/kw61i97/), None being a way to represent the absence of a value. For some reason(?????) I still have to define it as None or it throws an error.

### Extra Notes

- and has a higher priority than or.
    Either add parentheses to be safe or break up your expression into smaller parts and assign each part to a variable. This will make your code clear, readable, and unambiguous, and will save you from painful mistakes.
- not has higher priority than or if there are no parentheses
- not also has higher priority than and

if x:
    return False
else:
    return True

is equal to

return not x