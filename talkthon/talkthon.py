from random import choice

with open('nouns.txt') as n, \
    open('verbs.txt') as v, \
    open('adjectives.txt') as a:
        nouns = n.read().splitlines()
        verbs = v.read().splitlines()
        adjs = a.read().splitlines()

def talkthon():
    noun1 = choice(nouns)
    noun2 = choice(nouns)
    verb = choice(verbs)
    adj1 = choice(adjs)
    adj2 = choice(adjs)
    print(f'the {adj1} {noun1} {verb}s the {adj2} {noun2}')
