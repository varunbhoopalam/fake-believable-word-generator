
# Source: https://udel.edu/~dlarsen/ling101/slides/Morphology.pdf
from typing import Optional


class Morpheme:
    """
    Any unit of speech that carries a meaning or function but not both
    """
    form: str  # sequence of sounds
    meaning: Optional[str]
    function: Optional[str]

    def __init__(self):
        pass


class FreeMorpheme(Morpheme):
    """
    A morpheme that can stand on its own
    """


class BoundMorpheme(Morpheme):
    """
    A morpheme that cannot appear on its own
    """

"""
Observations
1. Some words contain only bound morphemes lingu-ist
2. Some bound morphemes appear in one word only ( cran+berry, luke+warm )
3. Some words contain more than one free morpheme ( roof+top, book+store ). Compound words?
4. All words contain a root. Is a word a special kind of morpheme?
    a. The root carries the word's principal meaning
    b. The root may or may not be able to stand alone
5. Affixes are a special class of bound morphemes. Four types of affixes
    a. prefix - attaches to beginning of the stem
    b. suffix - attaches to end of the stem
    c. infix - inserted inside of another morpheme
    d. circumfix - (a-verb-ing)
6. Words have a hierarchical structure - It's meaning is related to the structure 
    a. The root of the word is the parent node
7. Ways of building new words ******
    a. affixation, reduplication, compounding, blending, alternation, suppletion, reduction, back formation
    b. borrowings, eponyms, functional shift, semantic shift
"""