# You are working on a brand new dictionary. Instead of adding weird contractions for various parts of speech (like v, n, adj, adv, etc.), you decided to provide far more useful information: you put an article before each noun (you haven't chosen between definite and indefinite articles yet, so you use a, an or the), to before each verb, and write all other words as is. This is a dictionary, so the words are still supposed to go in alphabetical order disregarding supplementary words. For example, what was cat (n), hiss (v), kitten (n), meow (v), playful (adj), purr (v), now may become the cat, to hiss, a kitten, to meow, playful, to purr. If a list contains two words which belong to different parts of speech but are written in the same way, include supplementary words into comparison, i.e. to desert should be preceded by the desert, and to upset should go before upset.

# You're afraid that people will not understand your groundbreaking approach. To make sure that your time is not wasted, you decide first to apply your method only to a short list of words, show it to your friends and see how it goes. Before showing the list to friends, you would like to make sure that you didn't mess up the order. Given a list of words wordList (some of which are preceded by supplementary parts), check if they are sorted lexicographically according to the above-described rules.

# Example

# For wordList = ["the cat", "to hiss", "a kitten", "to meow", "playful", "to purr"], the output should be
# unusualDictionary(wordList) = true;

# For wordList = ["to desert", "the desert", "a dessert"], the output should be
# unusualDictionary(wordList) = false.

# The correct order is the desert, to desert, a dessert: the first two words should be compared together with supplementary words (so they differ at the second position where h precedes o), while the last two words should be compared without supplementary words (so they differ at the fourth position where e precedes s).
# .........................................................................
def unusualDictionary(wordList):
    def key(w):
        xs = w.split()
        return (xs[1], xs[0]) if len(xs) >= 2 else (w, w)
    return sorted(wordList, key=key) == wordList

print(unusualDictionary(["to desert", 
 "the desert", 
 "a dessert"]))