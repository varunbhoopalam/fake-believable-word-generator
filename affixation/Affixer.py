from dataclasses import dataclass
from typing import List


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


class Affixer:
    """
    I combine root families and suffixes families with smart rules
    I can probably even create definitions
    """
    @classmethod
    def affix(cls, root_family: RootFamily, suffix_family: SuffixFamily):
        return root_family.word_roots[0] + suffix_family.word_roots[0]
