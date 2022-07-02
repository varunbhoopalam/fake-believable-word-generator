# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random
import pickle
from affixation.Affixer import Affixer, RootFamily, SuffixFamily


def main():
    with open( "root_words_and_prefixes.p", "rb" ) as f:
        root_words_and_prefixes = pickle.load(f)

    with open( "suffixes.p", "rb" ) as f:
        suffixes = pickle.load(f)

    random_root = random.choice(root_words_and_prefixes)
    random_suffix = random.choice(suffixes)
    chosen_root_family = RootFamily(**random_root)
    chosen_suffix_family = SuffixFamily(**random_suffix)
    return Affixer.affix(chosen_root_family, chosen_suffix_family)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(main())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
