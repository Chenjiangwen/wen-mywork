from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.feature import MinHashLSH, CountVectorizer, Tokenizer
from pyspark.sql.functions import udf, monotonically_increasing_id
from pyspark.sql.types import IntegerType
import sys
import time

def extract_year(date_string):
    return int(date_string[:4])

def format_time(seconds):
    # 将秒转换为小时、分钟和秒
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining_seconds = int(seconds % 60)

    return "{} hours {} minutes {} seconds".format(hours, minutes, remaining_seconds)

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    threshold = float(sys.argv[3])

    sc = SparkContext(appName="News Similarity")
    spark = SparkSession(sc)

    print("===================Start====================")
    start_time = time.time()

    # Load and preprocess data
    lines = sc.textFile(input_file)
    parts = lines.map(lambda l: l.split(","))
    data = parts.map(lambda p: (p[0], ' '.join(p[1:])))
    df = spark.createDataFrame(data, ["date", "headline"])

    df = df.withColumn("id", monotonically_increasing_id())               # add ID column
    df = df.withColumn("year", udf(extract_year, IntegerType())(df.date)) # extract year
    df = Tokenizer(inputCol="headline", outputCol="words").transform(df)  # tokenize words

    # CountVectorizer
    cv = CountVectorizer(inputCol="words", outputCol="features")
    model = cv.fit(df)
    df = model.transform(df)

    # Apply MinHash LSH
    mh = MinHashLSH(inputCol="features", outputCol="hashes")
    model = mh.fit(df)
    df = model.transform(df)

    # Self join to find similar pairs
    similar_headlines = model.approxSimilarityJoin(df, df, threshold, distCol="JaccardDistance")

    # Filter pairs with the same year
    filtered = similar_headlines.filter(similar_headlines.datasetA.year != similar_headlines.datasetB.year)

    
    # Select the required columns
    output = filtered.select("datasetA.id", "datasetB.id", "JaccardDistance")


    # Change the format
    formatted_output = output.rdd.map(lambda x: (f"({x[0]},{x[1]})\t{x[2]}"))

    # Save the output
    formatted_output.coalesce(1).saveAsTextFile(output_folder)
    # print('完成！')
    print("======================完成！====================")
    print("The time spent is: {}".format(format_time(time.time() - start_time)))