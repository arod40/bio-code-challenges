from trie_construction_problem import trie_construction
from collections import defaultdict


def lazy_list(list, from_idx):
    for i in range(from_idx, len(list)):
        yield list[i]


def is_leaf(trie_node):
    return "$" in trie_node


def prefix_terminal_query(trie, string):
    current = trie[0]
    if is_leaf(current):
        yield i + 1

    for i, symbol in enumerate(string):
        if symbol in current:
            current = trie[current[symbol]]
        else:
            break
        if is_leaf(current):
            yield i + 1


def trie_matching(text, patterns):
    patterns = [pattern + "$" for pattern in patterns]
    trie = trie_construction(patterns)
    res = defaultdict(list)

    for i in range(len(text)):
        string = list(lazy_list(text, i))
        for idx in prefix_terminal_query(trie, string):
            res[text[i : i + idx]].append(i)
    return res


if __name__ == "__main__":
    from pathlib import Path

    text, patterns = Path("./dataset_873271_8.txt").read_text().split("\n")[:-1]
    patterns = patterns.split()

    for key, value in trie_matching(text, patterns).items():
        print(f"{key}: {' '.join(map(str, value))}")
