# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from asyncore import read
from itertools import count

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('./story.txt') as f:
        filename = f.read()
    return(filename)
        


def count_words():
    text = read_file_content('./story.txt')
    counts = dict()
    words = text.split(" ")

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)
    return(counts) 

count_words()