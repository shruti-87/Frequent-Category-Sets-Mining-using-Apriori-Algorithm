# Import necessary libraries
import os
from collections import defaultdict
from itertools import combinations, chain

class Apriori:
    def __init__(self, minSupport):
        # Initialize Apriori with minimum support and a dictionary to store support counts.
        self.support_count = defaultdict(int)
        self.minSupport = minSupport

    def read_transactions_from_file(self, transaction_file):
        # Read transactions from a file and return them as a list of sets.
        with open(transaction_file, "r") as infile:
            transactions = [set(line.rstrip("\n").split(";")) for line in infile]
            return transactions

    def get_one_itemset(self, transactions):
        # Generate the initial one-itemset from transactions.
        one_itemset = set()
        for transaction in transactions:
            for item in transaction:
                one_itemset.add(frozenset([item]))
        return one_itemset

    def self_cross(self, Ck, itemset_size):
        # Generate Ck+1 itemsets from Ck itemsets using self-crossing.
        Ck_plus_1 = {itemset1.union(itemset2)
                     for itemset1 in Ck for itemset2 in Ck
                     if len(itemset1.union(itemset2)) == itemset_size}
        return Ck_plus_1

    def prune_Ck(self, Ck, Lk_minus_1, itemset_size):
        # Prune Ck itemsets based on Lk-1 (frequent itemsets of size k-1).
        Ck_ = set()
        for itemset in Ck:
            Ck_minus_1 = list(combinations(itemset, itemset_size-1))
            flag = 0
            for subset in Ck_minus_1:
                if not frozenset(subset) in Lk_minus_1:
                    flag = 1
                    break
            if flag == 0:
                Ck_.add(itemset)
        return Ck_

    def get_min_supp_itemsets(self, Ck, transactions):
        # Count the support for each itemset in Ck and return frequent itemsets.
        temp_freq = defaultdict(int)
        for transaction in transactions:
            for itemset in Ck:
                if itemset.issubset(transaction):
                    temp_freq[itemset] += 1
                    self.support_count[itemset] += 1
        N = len(transactions)
        Lk = [itemset for itemset, freq in temp_freq.items()
              if freq/N > self.minSupport]
        return set(Lk)

    def frequent_item_set(self, transactions):
        # Generate frequent itemsets of all sizes using the Apriori algorithm.
        K_itemsets = dict()
        Ck = self.get_one_itemset(transactions)
        Lk = self.get_min_supp_itemsets(Ck, transactions)
        k = 2
        while len(Lk) != 0:
            K_itemsets[k-1] = Lk
            Ck = self.self_cross(Lk, k)
            Ck = self.prune_Ck(Ck, Lk, k)
            Lk = self.get_min_supp_itemsets(Ck, transactions)
            k += 1
        return K_itemsets

    def subsets(self, iterable):
        # Generate all possible subsets of an iterable.
        list_ = list(iterable)
        subsets_ = chain.from_iterable(combinations(list_, len)
                                       for len in range(len(list_)+1))
        subsets_ = list(map(frozenset, subsets_))
        return subsets_

    def merge_sort(self, items):
        # Perform merge sort to sort items based on support counts.
        if len(items) > 1:
            mid = len(items) // 2
            left_half = items[:mid]
            right_half = items[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = 0  # index for the left half
            j = 0  # index for the right half
            k = 0  # index for the merged list

            while i < len(left_half) and j < len(right_half):
                if self.support_count[left_half[i]] > self.support_count[right_half[j]]:
                    items[k] = left_half[i]
                    i += 1
                else:
                    items[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                items[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                items[k] = right_half[j]
                j += 1
                k += 1

    def write_part_1(self, K_itemsets):
        # Write part 1 of the results to patterns_1.txt
        main_dir = "./results/merge/part_1/"
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)
        outfile_path = "./results/merge/part_1/patterns_1.txt"
        with open(outfile_path, "w") as outfile:
            frequent_items = sorted(K_itemsets[1], key=lambda x: -self.support_count[x])
            self.merge_sort(frequent_items)
            total_count = min(50, len(frequent_items))
            outfile.write("#Total count\n")
            outfile.write(str(total_count) + "\n")

            for item in frequent_items[:total_count]:
                support_ct = self.support_count[item]
                outfile.write("{label} : {support}\n".format(
                    support=support_ct,
                    label=list(item)[0]
                ))

    def write_part_2(self, K_itemsets):
        # Write part 2 of the results to patterns_all.txt
        main_dir = './results/merge/part_2'
        if not os.path.exists(main_dir):
            os.makedirs(main_dir)
        outfile_path = "./results/merge/part_2/patterns_all.txt"
        with open(outfile_path, "w") as outfile:
            frequent_items = []  # Initialize a list to store all frequent items

            for key, values in K_itemsets.items():
                frequent_items.extend(values)

            frequent_items = sorted(frequent_items, key=lambda x: -self.support_count[x])
            self.merge_sort(frequent_items)

            total_count = len(frequent_items)  # Count the number of frequent itemsets

            # Write the total count at the beginning of the file
            outfile.write("#Total count\n")
            outfile.write(str(total_count))

            # Write the frequent items with their support counts
            for value in frequent_items:
                support_ct = self.support_count[value]
                outfile.write("\n{label} : {support}".format(
                    support=support_ct,
                    label=";".join(list(value))
                ))

# Main program entry
if __name__ == "__main__":
    # Define the input transaction file
    in_transaction_file = "/content/drive/MyDrive/Big Data Assignment/categories.txt.txt"

    # Initialize the Apriori algorithm with minimum support
    ap = Apriori(minSupport=0.01)
    transactions = ap.read_transactions_from_file(in_transaction_file)
    K_itemsets = ap.frequent_item_set(transactions)
    ap.write_part_1(K_itemsets)
    ap.write_part_2(K_itemsets)
