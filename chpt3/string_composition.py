if __name__ == "__main__":
    from pathlib import Path

    lines = Path("dataset_873144_3.txt").read_text().split()

    k = int(lines[0])
    text = lines[1]

    Path("out.txt").write_text(
        " ".join([text[i : i + k] for i in range(len(text) - k + 1)])
    )
