import ipdb

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        def refactor(word):
            word_to_refactor = list(word)
            word_to_refactor.sort()
            refactored_word = "".join(word_to_refactor)
            return refactored_word

        new_word_to_compare = refactor(self.word)
        matched_word = []
        
        for word in word_list:
            new_word = refactor(word)
            if new_word == new_word_to_compare:
                matched_word.append(word)
        return matched_word
            
            




