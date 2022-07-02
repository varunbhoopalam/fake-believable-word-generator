from dataclasses import dataclass
import random
from typing import List
import itertools


@dataclass
class ExampleAndDefinition:
    example: str
    definition: str


@dataclass
class RootFamily:
    word_roots: List[str]
    meanings: List[str]
    origin: str
    examples_and_definitions: List[ExampleAndDefinition]


@dataclass
class SuffixFamily:
    word_roots: List[str]
    meanings: List[str]
    sample_words: List[str]


class AffixerException(Exception):
    pass


@dataclass
class Affixation:
    word: str
    definition: str
    origin: str


class Affixer:
    """
    I combine root families and suffixes families with smart rules
    I can probably even create definitions
    """
    VOWELS: List[str] = ['a', 'e', 'i', 'o', 'u', 'y']

    @classmethod
    def affix(cls, root_family: RootFamily, suffix_family: SuffixFamily) -> Affixation:
        print("Attempting to create affixation for families")
        root_words = [root.strip() for root in root_family.word_roots if root.strip() != '']
        suffix_words = [root.strip() for root in suffix_family.word_roots if root.strip() != '']

        root_definitions: List[str] = [example_and_definition['definition'] for example_and_definition in
                                       root_family.examples_and_definitions]

        if len(root_words) == 0 or len(suffix_words) == 0 or len(root_definitions) == 0 or len(suffix_family.meanings) == 0:
            raise AffixerException

        return Affixation(
            word=cls._find_valid_word(root_words, suffix_words),
            definition=cls._compile_definition(root_definitions, suffix_family.meanings),
            origin=root_family.origin
        )

    @classmethod
    def _compile_definition(cls, root_definitions: List[str], suffix_meanings: List[str]):
        return random.choice(suffix_meanings) + ' ' + random.choice(root_definitions)

    @classmethod
    def _find_valid_word(cls, root_words: List[str], suffix_words: List[str]):
        permut = itertools.permutations(root_words, len(suffix_words))
        unique_combinations = []
        for comb in permut:
            zipped = zip(comb, suffix_words)
            unique_combinations.append(list(zipped))

        if not unique_combinations:
            raise AffixerException

        for combination in unique_combinations:
            unlist_combo = combination[0]
            if cls._is_valid_combination(unlist_combo):
                return unlist_combo[0] + unlist_combo[1]

        random_combination: (str, str) = random.choice(unique_combinations)[0]
        return random_combination[0] + 'o' + random_combination[1]

    @classmethod
    def _is_valid_combination(cls, combination: (str, str)) -> bool:
        root_last_character = combination[0][-1]
        suffix_first_character = combination[1][0]
        if cls._is_vowel(root_last_character) and not cls._is_vowel(suffix_first_character):
            return True
        elif not cls._is_vowel(root_last_character) and cls._is_vowel(suffix_first_character):
            return True
        else:
            return False

    @classmethod
    def _is_vowel(cls, char: str) -> bool:
        return char in cls.VOWELS
