import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE = "./data/quotes_js.csv"


def main():
    # Load the dataset
    df = pd.read_csv(CSV_FILE)
    df = df.drop_duplicates(subset=["text"])

    # Count quotes per author and show the top ones
    author_counts = df["author"].value_counts()
    print("Top Authors:")
    print(author_counts.head())

    # Count tags' frequency and show the top ones
    all_tags = []
    for tags in df["tags"]:
        all_tags.extend(tags.split("|"))
    tag_counts = pd.Series(all_tags).value_counts()
    print("\nTop Tags:")
    print(tag_counts.head())

    # Visualization on Authors' Distribution
    author_counts.head(10).plot(kind="bar", title="Top 10 Authors by Quote Count")
    plt.ylabel("Number of Quotes")
    plt.tight_layout()
    plt.savefig("./data/authors.png")
    plt.close()

    # Visualization on Tags' Distribution
    tag_counts.head(10).plot(kind="barh", title="Top 10 Tags")
    plt.xlabel("Frequency")
    plt.tight_layout()
    plt.savefig("./data/tags.png")
    plt.close()


if __name__ == "__main__":
    main()