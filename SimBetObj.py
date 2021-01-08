from collections import Counter
import math
import numpy
import unicodedata

# Data structure for each
# Let's parse the list to get the ID and the list

def read_file(filename):
    with open(filename,encoding = 'utf-8') as f:
        line = f.readline()
        cnt = 1

    matrix=[] #define empty matrix
    for i in xrange(3): #total row is 3
        row=[] #Credits for Hassan Tariq for noticing it missing
        for j in xrange(3): #total column is 3
            row.append(0) #adding 0 value for each column for this row
        matrix.append(row) #add fully defined column into the row
    print(matrix)

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

# print(counter_cosine_similarity(counterA, counterB) * 100)


def main():
    read_file('C:/Users/Lin/OneDrive/Documents/Sutygon/info1data.txt')


if __name__ == "__main__":
    main()
