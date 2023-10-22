# Apriori Algorithm for Frequent Pattern Mining

## Overview
This Python code implements the Apriori algorithm for frequent pattern mining. The Apriori algorithm is used to discover patterns (itemsets) that appear frequently in a dataset. In this implementation, the code processes a list of transactions containing items and extracts frequent itemsets based on a specified minimum support threshold.

## Problem Statement
1. You need to implement the Apriori algorithm (Frequent Pattern Mining) and use it to mine category sets 
that are frequent in the input data. After implementing the Apriori algorithm, please set the relative minimum 
support to 0.01 and run it on the 77,185 category lists. 
In other words, you need to extract all the category sets that have an absolute support no smaller than 771.

a. Please output all the length-1 frequent categories (item sets) with their absolute supports in the descending 
order of their support count, into a text file named patterns_1.txt. Also report the total count of the frequent 
item sets. Every line corresponds to exactly one frequent category and should be in the following format: (7
points including implementing Apriori)
#Total count
Category : Support
For example, suppose a category (Fast Food) has an absolute support 3000, then the line corresponding to this 
frequent category set in patterns.txt should be:
Fast Food : 3000

b. Write all the frequent category sets along with their absolute supports in the descending order of their 
support count, into a text file named patterns_all.txt. Also report the total count of the frequent item sets. 
Every line corresponds to exactly one frequent category set and should be in the following format: (4 points)
#Total count
Category_1,category_2,category_3,... : Support 
For example, suppose a category set (Fast Food; Restaurants) has an absolute support 2851, then the line 
corresponding to this frequent category set in patterns_all.txt should be:
#Total count
Fast Food; Restaurants : 2851

2. Mine the set of all Closed Frequent Itemsets (CFI’s) for the relative minimum support of 0.01 that you used 
to mine the frequent item sets and write the output in the descending order of support count, into a file 
named patterns_close.txt in the following format. Also report the total count of the frequent item sets. (4
points) 
Category : Support
#Total_count

## Table of Contents
1. [Installation Instructions](#installation-instructions)
2. [Usage and Examples](#usage-and-examples)
3. [Features](#features)
4. [Documentation](#documentation)
5. [Author Details](#author-details)
6. [Contact Information](#contact-information)

## Installation Instructions
To run this code, you'll need Python installed on your system. You can follow these steps to get started:

1. Clone this repository or download the code files to your local machine.
2. Make sure you have Python installed (Python 3.x is recommended).
3. Open any python code editor and open the code files there.
Note: Before Running the file make sure to change the destination and input paths according to your machine. If you are running on google colab, just you have to change the input path link, and output files will appear in /content of the colab file only.
5. Run the code.
6. The code will process the transactions and generate two result files: `patterns_1.txt` and `patterns_all.txt`.

## Usage and Examples
You can use this code to mine frequent itemsets from a dataset. In the provided code, it reads a list of transactions from a text file and sets a minimum support threshold (0.01). The result files `patterns_1.txt` and `patterns_all.txt` contain the frequent itemsets and their support counts.

The code usage example is shown in the `if __name__ == "__main__":` block at the end of the code. You can customize it to use your own transaction data and minimum support threshold.

## Features
- Implements the Apriori algorithm for frequent pattern mining.
- Reads transactions from a text file.
- Extracts frequent itemsets based on a minimum support threshold.
- Outputs the results to text files.

## Documentation
For a detailed explanation of the code and its components, refer to the comments within the code itself. The comments provide insights into the functionality of each function and the overall logic of the Apriori algorithm.
The code is organized into the following components:

-Apriori class: Contains methods for reading transactions, generating itemsets, and finding frequent itemsets.
-read_transactions_from_file: Reads transactions from an input file.
-get_one_itemset: Generates one-item itemsets.
-self_cross: Performs self-cross to generate candidate itemsets of higher length.
-prune_Ck: Prunes candidate itemsets based on previous frequent itemsets.
-get_min_supp_itemsets: Counts support and finds frequent itemsets.
-frequent_item_set: Executes the Apriori algorithm to find all frequent itemsets.
-subsets and merge_sort: Helper functions.

## Author Details
- Author: Shruti Sangam
- Email: shrutisangam2@gmail.com

## Contact Information
If you have any questions or need assistance with this code, feel free to contact me using the provided email address.
