# class Counter:
#     def __init__(self):
#         self.counter = -1

#     def get(self):
#         self.counter += 1
#         return self.counter


# counter = Counter()


# def insert_strings(trie, strings):
#     for string in strings:
#         insert_string(trie, string)


# def insert_string(trie, string):
#     trie, from_idx = prefix_query(trie, string)
#     if from_idx < len(string):
#         terminal = extend_branch(trie, string, from_idx)
#         terminal.is_terminal = True


# def prefix_query(trie, string):
#     for i, symbol in enumerate(string):
#         if symbol in trie:
#             trie = trie[symbol]
#         else:
#             break
#     return trie, i


# def extend_branch(trie, string, from_idx):
#     for i in range(from_idx, len(string)):
#         trie[string[i]] = TrieNode(trie)
#         trie = trie[string[i]]
#     return trie


# def print_adj_list(trie):
#     stack = [trie]
#     while stack:
#         trie = stack.pop()
#         for symbol, child in trie:
#             print(trie.id, child.id, symbol)
#             stack.append(child)


# class TrieNode:
#     def __init__(self, parent=None, is_terminal=False):
#         self.id = counter.get()
#         self.children = {}
#         self.parent = parent
#         self.is_terminal = is_terminal

#     @property
#     def is_root(self):
#         return self.parent is None

#     @property
#     def is_leaf(self):
#         return len(self.children) == 0

#     def __getitem__(self, symbol):
#         return self.children[symbol]

#     def __setitem__(self, symbol, value):
#         self.children[symbol] = value

#     def __contains__(self, symbol):
#         return symbol in self.children

#     def __iter__(self):
#         return iter(self.children.items())


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
    # trie = TrieNode()
    # insert_strings(trie, strings)
    # print_adj_list(trie)
