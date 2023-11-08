from pyspark.sql import SparkSession

def main():
    # Initialize SparkSession
    spark = SparkSession.builder.appName("AmazonReviewsProcessing").getOrCreate()
    
    # Read the CSV file into a DataFrame with headers
    file_path = "data_amazon.xlsx - Sheet1.csv"
    reviews_df = spark.read.option("header", "true").csv(file_path)
    
    # Show the DataFrame to verify it's loaded correctly
    reviews_df.show(truncate=False)
    
    # Register DataFrame as a temporary SQL table/view
    reviews_df.createOrReplaceTempView("reviews")

    # SQL query to select reviews with 'Cons_rating' of 4 or higher, including 'Cloth_class'
    high_ratings_sql = "SELECT Title, Review, Cons_rating, Cloth_class FROM reviews WHERE Cons_rating >= 4"
    high_ratings_df = spark.sql(high_ratings_sql)
    
    # Show the result of the SQL query
    high_ratings_df.show(truncate=False)

    # Data transformation: count the number of high-rated items per 'Cloth_class'
    high_rated_clothes_df = high_ratings_df.groupBy("Cloth_class").count()
    
    # Show the transformed DataFrame
    high_rated_clothes_df.show()

    # Combine the results into the report_content
    report_content = "Highly Rated Items (Cons_rating >= 4):\n"
    high_ratings_list = high_ratings_df.collect()
    for row in high_ratings_list:
        report_content += f"Title: {row['Title']}, Review: {row['Review']}, Rating: {row['Cons_rating']}, Cloth Class: {row['Cloth_class']}\n"

    report_content += "\nCount of Highly Rated Items by Cloth Class:\n"
    high_rated_clothes_list = high_rated_clothes_df.collect()
    for row in high_rated_clothes_list:
        report_content += f"Cloth Class: {row['Cloth_class']}, Count: {row['count']}\n"

    # Save the summary report to a text file
    report_file_path = "report.txt"
    with open(report_file_path, "w") as file:
        file.write(report_content)

    print("Report saved to report.txt")

if __name__ == "__main__":
    main()