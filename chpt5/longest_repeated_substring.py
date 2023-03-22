from suffix_tree_construction_problem import suffix_tree_construction


def longest_repeated_substring(text):
    suffix_tree = suffix_tree_construction(text + "$")

    parents = [-1] * len(suffix_tree)
    depth = [0] * len(suffix_tree)
    is_leaf = [True] * len(suffix_tree)

    queue = [0]
    max_depth_no_leaf = 0
    max_depth_no_leaf_idx = 0
    while queue:
        i = queue.pop(0)
        for j, (frag_start, frag_len) in suffix_tree[i].values():
            parents[j] = (i, frag_start, frag_len)
            depth[j] = depth[i] + frag_len
            is_leaf[i] = False
            queue.append(j)

        if depth[i] > max_depth_no_leaf and not is_leaf[i]:
            max_depth_no_leaf = depth[i]
            max_depth_no_leaf_idx = i

    # backtrack longest repeated substring
    reversed_fragments = []
    current = max_depth_no_leaf_idx
    while current != 0:
        current, frag_start, frag_len = parents[current]
        reversed_fragments.extend(reversed(text[frag_start : frag_start + frag_len]))
    reversed_fragments.reverse()

    return "".join(reversed_fragments)


if __name__ == "__main__":
    from pathlib import Path

    text = Path("dataset_873273_5.txt").read_text().strip()
    print(longest_repeated_substring(text))
