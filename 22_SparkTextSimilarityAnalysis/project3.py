from pyspark import SparkContext
from itertools import combinations
import sys
import time

# Function to extract the title from each line of input
def extract_title(line_num, line):
    parts = line.split(',')
    date = parts[0][:4]
    title = parts[1]
    return (line_num, (title.split(" "), date.strip()))

# Function to create the inverted index
def create_inverted_index(record):
    line_num, (title, date) = record
    title = [word.lower() for word in title]
    return [(word, [(line_num, title, date)]) for word in title]

# Function to generate pairs and compute similarity
def generate_pairs_and_compute_similarity(record):
    word, entries = record
    pairs = []
    for pair in combinations(sorted(entries), 2):
        if pair[0][2] == pair[1][2]:  # Skip if the dates are the same
            continue
        min_size = min(len(pair[0][1]), len(pair[1][1]))
        if min_size == 0:  # Skip if either title has no words
            continue
        max_size = max(len(pair[0][1]), len(pair[1][1]))
        if tau >= 0.85 and max_size - min_size > 1:  # Skip if the difference in title length is more than 1
            continue
        if min_size == max_size:
            if set(pair[0][1]) == set(pair[1][1]):  # Exact match
                pairs.append(((pair[0][0], pair[1][0]), 1.0))
            else:  # Compute Jaccard similarity
                pairs.append(((pair[0][0], pair[1][0]), jaccard_similarity(pair[0][1], pair[1][1])))
        else:  # Compute Jaccard similarity
            pairs.append(((pair[0][0], pair[1][0]), jaccard_similarity(pair[0][1], pair[1][1])))

    return pairs

# Function to compute Jaccard similarity
def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(set(list2))))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union

# Function to format time
def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)

    return "{} hours {} minutes {} seconds".format(hours, minutes, remaining_seconds)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    tau = float(sys.argv[3])

    sc = SparkContext()

    try:
        print("===================Start====================")
        start_time = time.time()

        lines = sc.textFile(input_file).zipWithIndex().map(lambda x: extract_title(x[1], x[0]))

        inverted_index = lines.flatMap(create_inverted_index).reduceByKey(lambda a, b: a + b)

        pair_combinations = inverted_index.flatMap(generate_pairs_and_compute_similarity)

        filtered_pairs = pair_combinations.filter(lambda x: x[1] >= tau)

        # Output formatting and saving
        output = filtered_pairs.map(lambda x: ((x[0][0], x[0][1]), round(x[1], 15))).distinct() \
            .sortBy(lambda x: (x[0][0], x[0][1])) \
            .map(lambda x: '({},{})\t{}'.format(x[0][0], x[0][1], round(x[1], 15)))

        output.coalesce(1).saveAsTextFile(output_folder)

        print("======================Save====================")
        print("The time spent is: {}".format(format_time(time.time() - start_time)))

    except Exception as e:
        print("==================Error===================")
        print("An error occurred while running the job: ", str(e))
    finally:
        sc.stop()
