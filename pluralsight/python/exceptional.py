import sys

DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# IndexError - an integert index is out of range. Usually happens whne trying to access an non-existent list index
# ValueError - Object is of the right type but contains inappropriate value
# KeyError - lookup in a mapping fails, such as looking up a non-existent key in a dict
# TypeErrors are not usually caught in python and are allowed exist

def convert(s):
    #Try..except blocks used to handle exceptions.
    #Try block contains code that COULD raise an exception
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    #Except block contains code that does error handling in the event an exception occurs
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", file=sys.stderr)
        raise
        #return -1
        #pass special statement that is known as a "no-op". 

print(convert("hello world"))
print(convert(513))