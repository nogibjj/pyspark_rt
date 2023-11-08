# PySpark Data Processing Project
tra29

## Overview
This project utilizes Apache Spark, an open-source distributed computing system that provides an interface for programming entire clusters with implicit data parallelism and fault tolerance. Specifically, we are using PySpark, the Python API for Spark, to perform data processing tasks on a large dataset.

## Dataset
The dataset we're using contains customer reviews from an online retail platform. It includes detailed information such as the title of the product, the review text, ratings, and categorical classifications of the clothing items.

You can find the dataset at [Online Retail Dataset](https://www.kaggle.com/datasets/uzair01/amazon-books/)

## Data Processing
The Python script `main.py` performs the following operations on the dataset:

1. **Data Loading**: Reads the dataset from a CSV file into a PySpark DataFrame.
2. **Data Filtering**: Selects reviews with a 'Cons_rating' of 4 or higher.
3. **Data Transformation**: Groups the filtered data by 'Cloth_class' and counts the number of high-rated items in each class.
4. **Report Generation**: Creates a summary report with the results from the data filtering and transformation steps, then saves it to a text file.

## Usage
To run the PySpark script, use the following command:

spark-submit main.py

Ensure that you have Apache Spark installed and configured on your system.

## Spark Job Screenshot
Below is a screenshot of the Spark job in action:

![AmazonReviewsProcessing - Spark Jobs](https://github.com/nogibjj/pyspark_rt/assets/143838819/aeba50b4-2ad9-4b10-bebf-80f9e7db1be1)
