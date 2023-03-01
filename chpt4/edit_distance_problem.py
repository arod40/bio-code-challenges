from global_alignment_problem import build_graph_from_scores, path_to_alignment
from longest_path_dag import longest_path_dag

if __name__ == "__main__":
    w1, w2 = input(), input()
    n1, n2 = len(w1), len(w2)

    # set match score to 0, and mismatch/indel penalties to 1 to yield the
    # path with the smallest edit distance
    g = build_graph_from_scores(w1, w2, 0, 1, 1)

    length, _ = longest_path_dag(g, (0, 0), (n1, n2))
    print(-length)
