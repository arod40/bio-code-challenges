def insert_string(trie, string):
    current = trie[0]
    for symbol in string:
        if symbol not in current:
            trie.append({})
            current[symbol] = len(trie) - 1
        current = trie[current[symbol]]


def trie_construction(patterns):
    trie = [{}]
    for string in patterns:
        insert_string(trie, string)
    return trie


def print_trie(trie):
    for i, children in enumerate(trie):
        for symbol, j in children.items():
            print(i, j, symbol)


if __name__ == "__main__":
    from pathlib import Path

    strings = Path("./dataset_873271_4.txt").read_text().split()
    trie = trie_construction(strings)
    print_trie(trie)
