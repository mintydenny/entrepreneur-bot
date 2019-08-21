import csv
import re
import numpy as np
import random
def decode_tweet_csv(csv_file_name):
    with open(csv_file_name,encoding="utf-8") as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) != 0:
                # row = [entry.decode("utf8") for entry in row]
                text = row[0][2:-1]
                text = re.sub('(?<!https://t)\.[\d|\w|\#]',r" ",text)
                splitted_text = [i for i in text.split(" ") if (i and i != ".")]
                add2chain1st(splitted_text)
chain = {}
count = {}
startKey = "__START__" # Start symbol
endKey = "__END__" # End sybbol
def add2chain2nd(splitted_text):
    """Creates a 2nd order markov chain"""
    # Our key is the unique occurrence of a pair of words
    inputText = splitted_text
    if len(inputText) > 1:
        for i, word in enumerate(inputText):
            if i == 0:  # Chaining the first and second word in tweet to start key
                if (None, startKey) not in chain:
                    chain[(None, startKey)] = [word]
                else:
                    chain[(None, startKey)].append(word)
            elif i == 1:
                if (startKey,inputText[i-1]) not in chain:
                    chain[(startKey,inputText[i-1])] = [word]
                else:
                    chain[(startKey,inputText[i-1])].append(word)
            else:
                if (inputText[i-2],inputText[i-1]) not in chain:
                    chain[(inputText[i-2],inputText[i-1])] = [word]
                else:
                    chain[(inputText[i-2],inputText[i-1])].append(word)
            if i == len(inputText)-1: # Use last two words as key to end
                if (inputText[i-1],word) not in chain:
                    chain[(inputText[i-1],word)] = [endKey]
                else:
                    chain[(inputText[i-1],word)].append(endKey)
        if (None,startKey) not in chain:
            chain[(None,startKey)] = [inputText[0]]
        else:
            chain[(None,startKey)].append(inputText[0])
        if (inputText[0],endKey) not in chain:
            chain[(inputText[0],endKey)] = [None]
        else:
            chain[(inputText[0],endKey)].append(None)
def add2chain1st(splitted_text):
    """Creates a 1st order markov chain"""
    # Our key is the unique occurrence of a pair of words
    inputText = splitted_text
    if len(inputText) > 1:
        for i, word in enumerate(inputText):
            if i == 0:  # Chaining the first and second word in tweet to start key
                if (startKey) not in chain:
                    chain[(startKey)] = [word]
                else:
                    chain[(startKey)].append(word)
            else:
                if (inputText[i-1]) not in chain:
                    chain[(inputText[i-1])] = [word]
                else:
                    chain[(inputText[i-1])].append(word)
            if i == len(inputText)-1: # If sentence ends here, connect to end
                if (word) not in chain:
                    chain[(word)] = [endKey]
                else:
                    chain[(word)].append(endKey)
        if (startKey) not in chain:
            chain[(startKey)] = [inputText[0]]
        else:
            chain[(startKey)].append(inputText[0])
        if (inputText[0]) not in chain:
            chain[(inputText[0])] = [endKey]
        else:
            chain[(inputText[0])].append(endKey)
def generate_tweet2nd(chain):
    startWord = chain[(None,startKey)][random.randint(0,len(chain[(None,startKey)])-1)]
    tweet = startWord
    firstWord = startWord
    print(startKey)
    print("=======")
    while True:
        newWord = chain[(firstWord,secondWord)][random.randint(0,len(chain[(firstWord,secondWord)])-1)]
        if len(tweet + " " + newWord) > 120 or newWord == endKey:
            break
        tweet = tweet + " " + newWord
        firstWord = secondWord
        secondWord = newWord
    print(tweet)
def generate_tweet1st(chain):
    startWord = chain[(startKey)][random.randint(0,len(chain[(startKey)])-1)]
    tweet = startWord
    firstWord = startWord
    while True:
        newWord = chain[(firstWord)][random.randint(0,len(chain[(firstWord)])-1)]
        if len(tweet + " " + newWord) > 120 or newWord == endKey:
            break
        tweet = tweet + " " + newWord
        firstWord = newWord
    print(tweet)
decode_tweet_csv("./tweets4.csv")
generate_tweet1st(chain)


