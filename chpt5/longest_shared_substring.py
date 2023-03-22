from suffix_tree_construction_problem import suffix_tree_construction


def prefix_query(trie, text, pattern):
    i = 0
    shared = []
    node_idx = 0
    while True:
        symbol = pattern[i]
        node = trie[node_idx]
        if symbol not in node:
            break
        else:
            node_idx, (frag_start, frag_len) = node[symbol]
            cont = True
            for j in range(frag_start, frag_start + frag_len):
                if pattern[i] == text[j]:
                    shared.append(pattern[i])
                    i += 1
                else:
                    cont = False
                    break
            if not cont:
                break
    return "".join(shared)


def longest_shared_substring(text1, text2):
    suffix_tree = suffix_tree_construction(text1)

    max_len = -1
    max_shared = None
    for i in range(len(text2)):
        shared = prefix_query(suffix_tree, text1, text2[i:])
        if len(shared) > max_len:
            max_len = len(shared)
            max_shared = shared

    return max_shared


if __name__ == "__main__":
    from pathlib import Path

    text1, text2 = Path("dataset_873273_6.txt").read_text().split("\n")[:-1]
    print(longest_shared_substring(text1 + "$", text2 + "@"))
