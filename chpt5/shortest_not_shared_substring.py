from suffix_tree_construction_problem import suffix_tree_construction
from longest_shared_substring import prefix_query


def shortest_not_shared_substring(text1, text2):
    if len(text2) < len(text1):
        text1, text2 = text2, text1
    suffix_tree = suffix_tree_construction(text1)

    min_len = len(text2)
    min_notshared = text2

    for i in range(len(text2)):
        shared = prefix_query(suffix_tree, text1, text2[i:])

        if i + len(shared) + 1 < len(text2) and len(shared) + 1 < min_len:
            min_len = len(shared) + 1
            min_notshared = text2[i : i + len(shared) + 1]

    return min_notshared


if __name__ == "__main__":
    from pathlib import Path

    text1, text2 = Path("dataset_873273_7.txt").read_text().split("\n")[:-1]

    if text1 == text2:
        print("nan")
    print(shortest_not_shared_substring(text1 + "$", text2 + "@"))
