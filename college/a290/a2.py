"""
a2.py
William C. Morris
<d4rkh4re@gmail.com>
"""
import math
import random
import bisect as bisect_module
import io

""" 8.12 """
def rotate_word(word, rotation):
    """ returns a new string that contains the letters from the \
        original string “rotated” by the given amount. """
    new_word = ""
    for c in word:
        new_word += chr(ord(c) + rotation)
    return new_word

""" 10.4 """
def is_anagram(word_1, word_2):
    """ takes two strings and returns True if they are anagrams. """
    l_w1 = list(word_1).sort()
    l_w2 = list(word_2).sort()    
    if l_w1 == l_w2:
        return True
    else:
        return False
    
""" 10.8 """
def bisect(sorted_list, target):
    """ takes a sorted list and a target value and returns the index \
        of the value in the list, if it’s there, or None if it’s not. """
    insertion_point = bisect_module.bisect_left(sorted_list, target)
    if insertion_point  >= len(sorted_list):
        return False
    else:
        if sorted_list[insertion_point] == target:
            return True
        else:
            return False
    
""" 10.9 """
def rev_pairs(word_list):
    """ Write a program that finds all the reverse pairs in the word list. """
    l_pairs = []
    for x_word in word_list:
        for y_word in word_list:
            if y_word == x_word[::-1]:
                l_pairs.append([x_word, y_word])
    return l_pairs

""" 10.10 """
def interlocks(n):
    """ Write a program that finds all pairs of words that interlock. """
    f = open("words.txt")
    word_dict = {}
    dict_index = 0

    result = []

    for word in f:
        word_dict[dict_index] = str(word)[:-1]
        dict_index += 1

    for w1 in word_dict.items():
        for w2 in word_dict.items():
            if len(w1) == len(w2):
                inter_word = interlock_word(w1, w2)
                if  inter_word in word_dict.items():
                    result.append(inter_word)

    return result

def interlock_word(w1, w2):
    """ """
    result = ""
    for i in range(len(w1)):
        result = result + str(w1[i]) + str(w2[i])
    return result

def test():
    print(rotate_word("cheer", 7)) # jolly

    print(is_anagram("word", "word")) # True
    print(is_anagram("word", "rdow")) # True

    word_list = ["ant", "bear", "cat", "dog", "elephant", "fish"]
    print(bisect(word_list, "cat")) # True
    print(bisect(word_list, "cobra")) # False

    rev_word_list = ["dog", "god", "word", "drow", "hey", "just"]
    print(rev_pairs(rev_word_list)) # [['dog', 'god'], ['god', 'dog'], ['word...

def test_interlock_and_rev_pairs():
    interlocks(5)
