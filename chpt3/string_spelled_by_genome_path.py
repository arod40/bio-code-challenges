def string_spelled_by_genome_path(path):
    return "".join([path[0]] + [kmer[-1] for kmer in path[1:]])

if __name__ == "__main__":
    from pathlib import Path
    path = Path("dataset_873145_3.txt").read_text().split()
    
    print(string_spelled_by_genome_path(path))