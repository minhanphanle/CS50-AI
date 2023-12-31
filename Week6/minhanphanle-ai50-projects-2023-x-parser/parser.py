import nltk
import sys
from nltk.tree import *

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP NP | NP VP | NP VP NP Conj NP VP | NP VP NP Conj VP | NP VP Conj VP
NP -> N | Det N | Det AP N | P NP Adv | P NP | NP P NP
VP -> V | Adv VP | VP NP | VP Adv
AP -> Adj | Adj AP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic character.
    """

    word_list = nltk.tokenize.word_tokenize(sentence)
    contain_alpha_list = [word for word in word_list if any(
        char.isalpha() for char in word)]

    processed_list = [word.lower()
                      for word in word_list if word in contain_alpha_list]

    return processed_list


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """

    np_chunks = []

    for s in tree.subtrees():
        if s.label() != "NP":
            continue

        contained_NP = False

        for sub_s in s:
            if sub_s.label() == "NP":
                contained_NP = True

        if contained_NP:
            continue
        np_chunks.append(s)

    return np_chunks


if __name__ == "__main__":
    main()
