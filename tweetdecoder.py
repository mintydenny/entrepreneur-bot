import csv
import re
import numpy as np
import random
import pickle
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
    tweet = ""
    firstWord = startWord
    secondWord = chain[(startKey,startWord)][random.randint(0,len(chain[(startKey,startWord)])-1)]
    tweet = tweet + secondWord
    while True:
        newWord = chain[(firstWord,secondWord)][random.randint(0,len(chain[(firstWord,secondWord)])-1)]
        if len(tweet + " " + newWord) > 120 or newWord == endKey:
            break
        tweet = tweet + " " + newWord
        firstWord = secondWord
        secondWord = newWord
    return tweet
def generate_tweet1st(chain):
    startWord = chain[(startKey)][random.randint(0,len(chain[(startKey)])-1)]
    tweet = startWord
    firstWord = startWord
    while True:
        newWord = chain[(firstWord)][random.randint(0,len(chain[(firstWord)])-1)]
        if newWord == endKey or len(tweet + " " + newWord) > 120:
            break
        tweet = tweet + " " + newWord
        firstWord = newWord
    return tweet

sentencesFile = open("./pickle/entrepreneurlife.pickle","rb")
sentencesFile2 = open("./pickle/entrepreneur.pickle","rb")
sentencesFile3 = open("./pickle/mindset.pickle","rb")
sentencesFile4 = open("./pickle/success.pickle","rb")
sentencesFile5 = open("./pickle/entrepreneurship.pickle","rb")
tweetList = pickle.load(sentencesFile)
tweetList2 = pickle.load(sentencesFile2)
tweetList3 = pickle.load(sentencesFile3)
tweetList4 = pickle.load(sentencesFile4)
tweetList5 = pickle.load(sentencesFile5)
tweetList_sum = tweetList + tweetList2 + tweetList3 + tweetList4 + tweetList5
print(len(tweetList_sum))

for tweet in tweetList_sum:
    add2chain1st(tweet)
print(generate_tweet1st(chain))
print("======================")
print(generate_tweet1st(chain))
print("======================")
print(generate_tweet1st(chain))
print("======================")
print(generate_tweet1st(chain))
print("======================")
print(generate_tweet1st(chain))
#


