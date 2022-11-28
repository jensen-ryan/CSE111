import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]
        #Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
        #randomly chooses a noun and then returns it to form the sentence
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == 'past':
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == 'present' and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == 'present' and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    #randomly chooses a verb from 4 sets of verbs and then returns it
    word = random.choice(words)
    return word

def get_preposition():
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    #randomly chooses a preposition and returns it
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):

    #gets a preposition from the get_prepostion() function
    preposition = get_preposition()

    #gets an article from the get_determiner() with a random quantity
    determiner = get_determiner(quantity)

    #gets a nound from get_noun() with a random quantity
    noun = get_noun(quantity)

    prepositional_phrase = f'{preposition} {determiner} {noun}'
    return prepositional_phrase

def main():
    #these are the different combinations of determiners and verbs
    sentences = [['singular', 'past'], ['plural', 'past'], ['singular', 'present'],['plural', 'present'], ['singular', 'future'], ['plural', 'future']]

    for noun_and_verb in sentences:
        noun = noun_and_verb[0]
        tense = noun_and_verb[1]
        if noun == 'singular':
            quantity = 1
        else:
            quantity = 2

            determiner = get_determiner(quantity)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            determiner = determiner.capitalize()

            sentence = f'{determiner} {noun} {verb}.'

            print(sentence)

    print()
    
    for noun_and_verb in sentences:
        noun = noun_and_verb[0]
        tense = noun_and_verb[1]
        if noun == 'singular':
            quantity = 1
        else:
            quantity = 2

        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity, tense)
        phrase = get_prepositional_phrase(quantity)

        determiner = determiner.capitalize()
        sentence = f'{determiner} {noun} {verb} {phrase}.'
        print(sentence)

    print()
            
if __name__ == "__main__":
    main()