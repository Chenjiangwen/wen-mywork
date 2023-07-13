from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col, lower, struct, row_number, posexplode, concat_ws
from pyspark.sql.window import Window
import sys

def main(input_file, output_folder, stopwords_file, k):
    # Initialize SparkSession
    spark = SparkSession.builder.appName("TermPairCounter").getOrCreate()

    # Load stopwords file
    stopwords = set(spark.sparkContext.textFile(stopwords_file).collect())

    # Load input file
    df = spark.read.text(input_file) \
        .selectExpr("split(value,',')[0] as year", "split(value,',')[1] as headline") \
        .withColumn('year', col('year').substr(1, 4)) \
        .select('year', posexplode(split('headline', ' ')).alias('pos', 'words'))

    # Filter out stopwords and non-alphabetic terms
    df_clean = df.filter(~lower(df.words).isin(stopwords)) \
        .filter(df.words.rlike("^[a-z].*"))

    # Extract and count term pairs
    df_pairs = df_clean.alias('df1').join(df_clean.alias('df2'), (col('df1.year') == col('df2.year')) & (col('df1.pos') < col('df2.pos'))) \
        .groupBy('df1.year', 'df1.words', 'df2.words') \
        .count()

    # Define window partitioned by 'year', ordered by 'count' descending and then lexicographically by 'df1.words' then 'df2.words'.
    window = Window.partitionBy(df_pairs['year']).orderBy(df_pairs['count'].desc(), df_pairs['df1.words'], df_pairs['df2.words'])

    # Add a row_number over the window
    df_pairs = df_pairs.withColumn('rn', row_number().over(window))

    df_topk_pairs = df_pairs.filter(df_pairs['rn'] <= k)

    # Generate output format
    output = df_topk_pairs.selectExpr("concat(year, ' ', df1.words, ',', df2.words, ':', count) as result")

    # Order by year in ascending order
    output = output.orderBy('result')

    # Write result to output_folder
    output.coalesce(1).write.format('text').option('header', 'false').mode('overwrite').save(output_folder)

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    # input_file = 'file:///Users/crystalzhang/Desktop/tiny-doc.txt'
    # output_folder = 'file:///Users/crystalzhang/Desktop/output_folder/df'
    # stopwords_file = 'file:///Users/crystalzhang/Desktop/stopwords.txt'
    # k = int(1)

    input_file = sys.argv[1]
    output_folder = sys.argv[2]
    stopwords_file = sys.argv[3]
    k = int(sys.argv[4])

    main(input_file, output_folder, stopwords_file, k)
