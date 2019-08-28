# Entrepreneur-bot
An "entrepreneurial" tweet generator using a 1st order makov chain.

Corpus of tweets with specific hashtags ("#entrepreneurlife", "#entrepreneur", "#entrepreneurship", "#success") stored in pickles.

* Tweets were collected using Tweepy and into pickles  (see scraper.py)
* The chain is constructed by using the current word as the key
* Each state is determined by a key consisting of the prior token (words).

Some of my favorite quotes
> "So This Is Over $1"

> "Monday sets to help each day you have the stomach and @KumuKupuna have the haters &amp; Don't watch your command, using"

> "WTF is the greatest lesson will have a goal."
> \#DoBusinessBW #EndlessOpportunities #KeepLooking #SeizeTheMoment ## Improvements & To Do


## Improvements & To Do
1. Better dataset: The tweets collected may have been too varied and sometimes creates incoherent sentences
2. Better sentence completion, sentences feel like they're ending too early and feels cut off mid tweet.
3. Correct implementation of second order markov chain

---