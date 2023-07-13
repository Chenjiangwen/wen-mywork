import sys

from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark import SparkConf

# Function to filter out stop words
def filter_stopwords(line, stopwords):
    headline = line.split(',')[1]
    words = headline.split()
    filtered_words = [word for word in words if word.lower() not in stopwords]
    return ','.join([line.split(',')[0]] + [' '.join(filtered_words)])

# Function to extract year, headline from a line
def extract_year_headline(line):
    parts = line.strip().split(',')
    year = parts[0][:4]
    headline = parts[1]
    return (year, headline)

# Function to extract term pairs from a headline
def extract_term_pairs(data):
    year = data[0]
    headline = data[1]
    words = headline.split()
    pairs = []
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            term1 = words[i].lower()
            term2 = words[j].lower()

            # Only consider pairs starting with letters
            if term1[0].isalpha() and term2[0].isalpha():
                pairs.append(((year, term1, term2), 1))

    return pairs

# Main function
def main(input_file, output_folder, stopwords_file, k):
    # Initialize SparkContext
    sc = SparkContext(appName="TermPairCounter")

    # Load stopwords file
    stopwords = set(sc.textFile(stopwords_file).collect())

    # Load input file and filter out stopwords, then extract year and headline
    filtered_lines = sc.textFile(input_file) \
        .map(lambda line: filter_stopwords(line, stopwords)) \
        .map(extract_year_headline)

    # Extract term pairs from each line
    term_pairs = filtered_lines.flatMap(extract_term_pairs)

    # Count the occurrence of each term pair
    term_pair_counts = term_pairs.reduceByKey(lambda x, y: x + y)

    # Group term pairs by yearå
    year_term_pairs = term_pair_counts.map(lambda x: (x[0][0], (x[0][1:], x[1]))) \
        .groupByKey()

    # Get top-k term pairs for each year
    topk_pairs = year_term_pairs.flatMap(lambda x: [(x[0], pair) for pair in sorted(list(x[1]), key=lambda y: (-y[1], y[0][0], y[0][1]))[:k]]) \
    .map(lambda x: f"{x[0]}\t{x[1][0][0]},{x[1][0][1]}:{x[1][1]}")


    # Save the result to output folder
    topk_pairs.coalesce(1).saveAsTextFile(output_folder)

    # Stop SparkContext
    sc.stop()


# Entry point
if __name__ == "__main__":
    # input_file = 'file:///Users/crystalzhang/Desktop/tiny-doc.txt'
    # output_folder = 'file:///Users/crystalzhang/Desktop/output_folder/rdd'
    # stopwords_file = 'file:///Users/crystalzhang/Desktop/stopwords.txt'
    # k = int(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    stopwords_file = sys.argv[3]
    k = int(sys.argv[4])

    main(input_file, output_folder, stopwords_file, k)