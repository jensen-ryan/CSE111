from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
from random import randint
import pytest

#list of all of the words used in sentences.py
singular_determiners = ["the", "one"]
plural_determiners = ["some", "many"]
singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
past_tense = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
present_tense_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
present_tense_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
future_tense = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

def test_get_determiner():
    #Test the singular determiners 4 times.
    for _ in range(4):
        word = get_determiner(1)

        #Verify that the word returned from get_determiner is one of the words in the singular_determiners list.
        assert word in singular_determiners
        
    #Test the plural determiners 4 times.
    for _ in range(4):
        word = get_determiner(2)
        
        #Verify that the word returned from get_determiner is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    #tests singular nouns
    for _ in range(4):
        word = get_noun(1)
        assert word in singular_nouns
        
        #test plural nouns
        for _ in range(4):
            word = get_noun(0)
            assert word in plural_nouns

def test_get_verb():
    #past tense verb
    for _ in range(4):
        word = get_verb(1, 'past')
        assert word in past_tense
        
    #present and singular verb
    for _ in range(4):
        word = get_verb(1, 'present')
        assert word in present_tense_singular
        
    #present and plural verb
    for _ in range(4):word = get_verb(2, 'present')
    assert word in present_tense_plural
    
    #future verb
    for _ in range(4):
        word = get_verb(1, 'future')
        assert word in future_tense

def test_get_preposition():
    #tests prepositions
    for _ in range(5):
        word = get_preposition()
        assert word in prepositions, "False"

def test_get_prepositional_phrase():
    #preposition, determiner, noun
    for _ in range(40):
        #gets a random number to decide if phrase is singular or plural
        quantity = randint(1, 2)
        sentence = get_prepositional_phrase(quantity)
        sentence_splitted = sentence.split(' ')
        #splits returned phrase
        assert sentence_splitted[0] in prepositions
        assert sentence_splitted[1] in singular_determiners or plural_determiners
        assert sentence_splitted[2] in singular_nouns or plural_nouns
    
    pass

pytest.main(["-v", "--tb=line", "-rN", 'test_sentences.py'])