# For type hints
from __future__ import annotations
from typing import List, Tuple

# For printing out the results nicely in score()
import pprint

# For file manipulation
import os

# For pathlib
import pathlib
from functools import lru_cache


def process_dir(directory_path: str, process_file_fn: callable) -> List[Tuple]:
    """ Use the provided process_file_fn to process each of the files in the
    given directory and return a list of all the matches found.

    NOTE: You do not need to and should not modify this function or its
    interface, as any changes made locally to this function will not be used
    by the autograder script.
    """
    results = []
    for filename in os.listdir(directory_path):
        # Skip any files in the directory that start with '.'
        if filename[0] != '.':
            f_guesses = process_file_fn(filename, directory_path)
            results.extend(f_guesses)
    return results


def get_gold(gold_path: str) -> List[Tuple]:
    """ Return a list of tuples of the canonical form
    (filename, type, value) given a path to a tsv file of gold e-mails.

    NOTE: You do not need to and should not modify this function or its
    interface, as any changes made locally to this function will not be used
    by the autograder script.
    """
    gold_results = []
    for line in open(gold_path, 'r'):
        gold_results.append(tuple(line.strip().split('|')))
    return gold_results


def score(guess_matches: List[Tuple], gold_matches: List[Tuple]) -> None:
    """
    Score the user-extracted matches by comparing them to a list of gold
    matches and print the results. The comparison is done by computing the
    true positives, false positives and false negatives (from the set
    intersection and difference).

    NOTE: The scoring is case-insensitive (all of the extracted email
    addresses are converted to lower case before comparing)
    and removes duplicates.

    NOTE: You do not need to and should not modify this function or its
    interface, as any changes made locally to this function will not be used
    by the autograder script.
    """
    # Convert the emails (the guesses and the correct/gold)
    # to lowercase
    guess_matches = [
        (filename, match_type, match_value.lower())
        for (filename, match_type, match_value)
        in guess_matches
    ]

    gold_matches = [
        (filename, match_type, match_value.lower())
        for (filename, match_type, match_value)
        in gold_matches
    ]

    # Remove duplicates by converting the lists to sets
    guess_set = set(guess_matches)
    gold_set = set(gold_matches)

    # Compute the true positives, false positives, and false negatives
    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    # Print all of the results nicely
    pp = pprint.PrettyPrinter()
    print('Guesses (%d): ' % len(guess_set))
    pp.pprint(guess_set)
    print('Gold (%d): ' % len(gold_set))
    pp.pprint(gold_set)
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp), len(fp), len(fn)))


@lru_cache
def gpt2_bytes_to_unicode() -> dict[int, str]:
    """
    Returns a mapping between every possible byte (an integer from 0 to 255) to a
    printable unicode string character representation. This function is taken
    from the GPT-2 code.

    For example, `chr(0)` is `\x00`, which is an unprintable character:

    >>> chr(0)
    '\x00'
    >>> print(chr(0))

    As a result, this function returns a dictionary `d` where `d[0]` returns `Ā`.
    The bytes that are visually printable keep their original string representation [1].
    For example, `chr(33)` returns `!`, and so accordingly `d[33]` returns `!`.
    Note in particular that the space character `chr(32)` becomes `d[32]`, which
    returns 'Ġ'.

    For unprintable characters, the function shifts takes the integer representing
    the Unicode code point of that character (returned by the Python `ord`) function
    and shifts it by 256. For example, `ord(" ")` returns `32`, so the the space character
    ' ' is shifted to `256 + 32`. Since `chr(256 + 32)` returns `Ġ`, we use that as the
    string representation of the space.

    This function can simplify the BPE implementation and makes it slightly easier to
    manually inspect the generated merges after they're serialized to a file.
    """
    # These 188 integers can used as-is, since they are not whitespace or control characters.
    # See https://www.ssec.wisc.edu/~tomw/java/unicode.html.
    bs = list(range(ord("!"), ord("~") + 1)) + list(range(ord("¡"), ord("¬") + 1)) + list(range(ord("®"), ord("ÿ") + 1))
    cs = bs[:]
    # now get the representations of the other 68 integers that do need shifting
    # each will get mapped chr(256 + n), where n will grow from 0...67 in the loop
    # Get printable representations of the remaining integers 68 integers.
    n = 0
    for b in range(2**8):
        if b not in bs:
            # If this integer isn't in our list of visually-representable
            # charcters, then map it to the next nice character (offset by 256)
            bs.append(b)
            cs.append(2**8 + n)
            n += 1
    characters = [chr(n) for n in cs]
    d = dict(zip(bs, characters))
    return d