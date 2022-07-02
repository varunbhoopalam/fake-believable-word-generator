import random
import pickle

from WordValidator import WordValidator
from affixation.Affixer import Affixer, RootFamily, SuffixFamily, AffixerException, Affixation


def create_affixation() -> Affixation:
    with open( "root_words_and_prefixes.p", "rb" ) as f:
        root_words_and_prefixes = pickle.load(f)

    with open( "suffixes.p", "rb" ) as f:
        suffixes = pickle.load(f)

    random_root = random.choice(root_words_and_prefixes)
    random_suffix = random.choice(suffixes)
    chosen_root_family = RootFamily(**random_root)
    chosen_suffix_family = SuffixFamily(**random_suffix)

    word_validator = WordValidator()
    done = False
    while not done:
        try:
            affixation: Affixation = Affixer.affix(chosen_root_family, chosen_suffix_family)
            if not word_validator.is_alpha_numeric_word(affixation.word):
                done = True
            else:
                print(f'Oops I created a real word | {affixation.word}')
        except AffixerException:
            pass
    return affixation


if __name__ == '__main__':
    print(create_affixation())
