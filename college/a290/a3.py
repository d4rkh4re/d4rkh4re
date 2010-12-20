"""
a3.py
William C. Morris
<d4rkh4re@gmail.com>

Assignment 3
http://www.greenteapress.com/thinkpython/html/book012.html
http://www.greenteapress.com/thinkpython/html/book013.html
"""
def inver_dict(d_org):
    """ 11.5 concise version of invert_dict. """
    d_inv = dict()
    for key in d_org:
        val = d_org[key]

        if d_inv.setdefault(val, [key]) != [key]:
            d_inv[val].append(key)
    return d_inv

def has_duplicates(d):
    """ 11.8 takes a dict as a parameter and returns True if there is any object
        that appears more than once in the dict. """
    count = inver_dict(d)
    for val in count.values():
        if len(val) > 1:
            return True
    return False

def sumall(*args):
    """ 12.1 Write a function called sumall that takes any number of arguments
        and returns their sum. """
    result = 0
    for arg in args:
        result += arg
    return result

def most_frequent(text):
    """ Returns a string of the letters in the given text, in order of
        non-increasing frequency of occurrence in the text, ignoring case and
        characters that are not ASCII letters.
    """
    temp = dict()
    result = []
    for letter in text.lower():
        if temp.setdefault(letter, 0) >= 0:
            temp[letter] = temp[letter] + 1

    return sorted(temp.items(), key=lambda t: t[1])

text = "Jack and Jill went up the hill."
t = most_frequent(text)

def test():
    hist = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
    print(inver_dict(hist))

    du_1 = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
    du_2 = {'p': 1, 'r': 2}
    print(has_duplicates(du_1))
    print(has_duplicates(du_2))

    print(sumall(4,3,2,1,0))
    
    print(t)
