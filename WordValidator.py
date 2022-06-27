import pickle
from typing import Set


class WordValidator:
    valid_words: Set[str]

    def __init__(self):
        with open("word_set.p", "rb") as word_set:
            self.valid_words = pickle.load(word_set)

    def is_alpha_numeric_word(self, word: str) -> bool:
        return word in self.valid_words
