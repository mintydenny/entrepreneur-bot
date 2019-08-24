# Entrepreneur-bot
An "entrepreneurial" tweet generator using a 1st order makov chain. 

Corpus of tweets with specific hashtags ("#entrepreneurlife", "#entrepreneur", "#entrepreneurship", "#success") stored in pickles.

* Tweets were collected using Tweepy and into pickles  (see scraper.py)
* The chain is constructed by using the current word as the key
* Each state is determined by a key consisting of the prior token (words).

## Improvements
1. Better dataset: The tweets collected may have been too varied and sometimes creates incoherent sentences
2. Better sentence completion, sentences feel like they're ending too early and feels cut off mid tweet.
3. Correct implementation of second order markov chain

---
Sidenote: 
I had what I thought was a second order markov chain implemented in which I dictated that the future state (our next word) is determined by using the previous two words as key. However, this seemed to not be the case. But upon further reading, this seemed to not be the case. Each key should be a unique word, for both first and second order.  