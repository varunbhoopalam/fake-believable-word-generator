import random
import string
from enum import Enum
from typing import List, Optional

"""
Source - https://makingenglishfun.com/2021/04/01/what-are-the-digraphs-in-english-and-how-to-teach-them/#:~:text=An%20English%20digraph%20consists%20of%20a%20pair%20of,Examples%20include%20%2Fsh%2F%20%2Fch%2F%20%2Fth%2F%20%2Fai%2F%20%2Fee%2F%20%2Fie%2F.
Diagraphs - Pairs of letters placed together that make a single sound or phoneme
Diagraphs can be heterogenous (two different letters) and homogenous (same letters)
"""
ENGLISH_DIGRAPHS = {
    'vowels': [
        'ai',
        'ea',
        'ee',
        'ie',
        'oa',
        'oe',
        'ue',
        'ui',
        'oo',
        'a-e',
        'i-e',
        'u-e'
    ],
    'consonants': [
        'sh',
        'wh',
        'ph',
        'th',
        'kn',
        'wh',
        'ch',
        'gh',
        'gn',
    ]
}

"""
Consonant blends differ from digraphs as in blends you can hear each distinct sound

"""

"""
Source - https://www.brighthubeducation.com/esl-teaching-tips/102578-american-english-dipthongs/#:~:text=The%20most%20common%20diphthongs%20in%20American%20English%20are,word.%20For%20instance%2C%20five%20has%20the%20diphthong%20%2Fai%2F.
English dipthongs are words that have two vowel sounds in one syllable
"""
ENGLISH_DIPTHONGS = {
    '_(_Iə)': [
        'ee', #deer
        'ie', #fierce
        'ea' #beard
    ],
    'eə': [
        'ai', #fair
        'a', #care
        'ea' #pear
    ],
    'ʊə': [
        'oo', #poor
        'ou', #tour
        'u', #plural
        'ue', #cruel
    ],
    'eI': [
        'ey', #they
        'ay', #play
        'ai', #pain
        'a', #race
    ],
    'aI': [
        'i', #idea
        'igh', #light
        'y', #my
    ],
    'ɔI': [
        'oy', #boy
        'oi', #join
    ],
    'oʊ': [
        'ow', #show
        'oa', #load
        'o', #go
    ],
    'aʊ': [
        'ou', #sound
        'ow', #how
    ],
}


class WordGenerator:
    ascii_lowercase = string.ascii_lowercase

    @classmethod
    def generate(cls, length: int = random.randint(5, 12)):
        word: str = ''
        for _ in range(0, length):
            word += cls._generate_random_letter()
        return word

    @classmethod
    def _generate_random_letter(cls, choices: Optional[List[str]] = None):
        if not choices:
            return random.choice(cls.ascii_lowercase)

        return random.choice(choices)
