def suffix_match(node, text, suffix_start):
    symbol = text[suffix_start]
    if symbol not in node:
        return 0
    else:
        _, (frag_start, frag_len) = node[symbol]
        for offset in range(frag_len):
            if text[suffix_start + offset] != text[frag_start + offset]:
                return offset
        return -1


def update_suffix_tree(trie, node_idx, text, suffix_start, offset):
    node = trie[node_idx]
    if offset != 0:
        trie.append({})
        symbol = text[suffix_start]
        old_child_idx, (frag_start, frag_len) = node[symbol]
        node[symbol] = (len(trie) - 1, (frag_start, offset))

        node = trie[-1]
        symbol = text[frag_start + offset]
        node[symbol] = (old_child_idx, (frag_start + offset, frag_len - offset))

        suffix_start += offset

    trie.append({})
    symbol = text[suffix_start]
    node[symbol] = (len(trie) - 1, (suffix_start, len(text) - suffix_start))


def insert_suffix(trie, text, suffix_start):
    node_idx = 0
    while True:
        node = trie[node_idx]
        offset = suffix_match(node, text, suffix_start)
        if offset == -1:
            node_idx, (_, frag_len) = node[text[suffix_start]]
            suffix_start += frag_len
        else:
            update_suffix_tree(trie, node_idx, text, suffix_start, offset)
            return


def suffix_tree_construction(text):
    suffix_trie = [{}]
    for i in range(len(text)):
        insert_suffix(suffix_trie, text, i)

    return suffix_trie


def print_suffix_tree_edges(text, suffix_tree):
    for children in suffix_tree:
        for _, (_, (frag_start, frag_len)) in children.items():
            print(text[frag_start : frag_start + frag_len])


if __name__ == "__main__":
    from pathlib import Path

    text = Path("dataset_873273_4.txt").read_text().strip()

    suffix_tree = suffix_tree_construction(text)
    print_suffix_tree_edges(text, suffix_tree)
