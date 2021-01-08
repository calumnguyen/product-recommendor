from collections import Counter
import math
import numpy
import unicodedata

# Data structure for each
# Let's parse the list to get the ID and the list

def read_file(filename):
    # Number of items in the list
    number = 2

    # List of lists of item, each list containing the tag of an item
    list_items = [];
    list_names = [];
    # Parse the file to get the tags for each item
    with open(filename,encoding = 'utf-8') as f:
        for line in f:
            # get the name ID of the item
            try:
                name_index = line.find("oid")+6
                try:
                    name = line[name_index:(name_index+24)]
                    list_names.append(name)
                except:
                    print("ERROR: Can't parse name")
                    return
            except:
                print("ERROR: Item doesn't have an ID.")
                return
    print(list_names)

    # Trial variable for list, should be equivalent to lists_item
    list = [["ha ha", "hi hi"],["ha ha", "he he"]]

    # Design a similarity matrix
    matrix = numpy.zeros(shape=(number,number))

    # i run from 0 to num-1 and j runs from i+1 to num-1 (num here because of the syntax of range)
    # only need to consider the upper half of the matrix because this should be a symmetrix matrix
    for i in range(0,number): #total row is 3
        for j in range(i+1,number): #total column is 3
            matrix[i][j] = counter_cosine_similarity(Counter(list[i]),Counter(list[j]))
    #print(counter_cosine_similarity(Counter(list[0]),Counter(list[1])))
    print(matrix)
    # Save matrix into a file
    numpy.savetxt("similarity_items_only.csv", matrix, delimiter=",")

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

# print(counter_cosine_similarity(counterA, counterB) * 100)


def main():
    read_file('C:/Users/Lin/OneDrive/Documents/Sutygon/info.txt')


if __name__ == "__main__":
    main()
