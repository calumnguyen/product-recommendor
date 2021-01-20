from collections import Counter
import math
import numpy
import unicodedata

# This function calculates the similarity between two counters using the cosine law
def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

# This function takes in a json file, parse it, put the data into a list
# then call counter_cosine_similarity function to generate similarity matrix
# This function also takes in choice. If choice is 1, customer has an ID of
# an item and wants to look for similar items. If choice is 2, customer
# wants to look up similar item based on a description of the item
# This function returns the similarity matrix as well as the column index
# of the target item
def read_file(filename, choice):
    # Number of items in the list
    number = 0

    # List of lists of item, each list containing the tag of an item
    list_items = [];
    list_ID = [];

    # New file processed JSON file into the ideal format (without endline)
    # Tag 'wb' to write Unicode
    new_file = open("newfile/processed_json.txt","wb")

    # Parse the file to get the tags for each item
    with open(filename,encoding = 'utf-8') as f:
        for line in f:
            if line[0] != '}':
                list_word = line.split()
                line = ' '.join(line.split())
            new_file.write(line.encode('utf8'))
    new_file.close();

    # Open the processed filed again for reading
    # Try json lib but doesn't work well with utf-8
    with open("newfile/processed_json.txt",encoding = 'utf-8') as f:
        for line in f:
            number += 1
            # get the name ID of the item
            try:
                name_index = line.find("ObjectId")+10
                try:
                    name = line[name_index:(name_index+24)]
                    list_ID.append(name)
                    print(name)
                except:
                    print("ERROR: Can't parse name")
                    return "none",-1
            except:
                print("ERROR: Item doesn't have an ID.")
                return "none",-1

            # parse for items' tags
            # combine all tags in one single string
            total_string = ""
            try:
                name_index = line.find("name")+7
                try:
                    name = line[name_index:(line.find("produ")-3)]
                    try:
                        total_string = name.replace(',','')
                    except:
                        print("ERROR: Can't split the string in name tag")
                        return "none",-1
                except:
                    print("ERROR: Can't find \"")
                    return "none",-1
            except:
                print("ERROR: Item doesn't have a name tag")
                return "none",-1

            # Other Tags
            try:
                name_index = line.find("tags")+6
                try:
                    name = line[name_index:(line.find("ima")-3)]
                    try:
                        total_string = name.replace(',','')
                        total_string = total_string + name
                    except:
                        print("ERROR: Can't split the string in other tags")
                        return "none",-1
                except:
                    print("ERROR: Can't find \"")
                    return "none",-1
            except:
                print("ERROR: Item doesn't have a tag")
                return "none",-1
            list_items.append(total_string)

    # # if want to add a general item
    if choice == "2":
        number += 1
        description = input("Please enter description as a string without comma: ")
        list_items.append(description)
        column = number-1
    else:
        ID = input("Please enter the ID of the item: ")
        try:
            column = list_ID.index(ID)
        except:
            print("ERROR: Can't find the item ID")
            return "none", -1

    # Design a similarity matrix
    matrix = numpy.zeros(shape=(number,number))

    # i run from 0 to num-1 and j runs from i+1 to num-1 (num here because of the syntax of range)
    # only need to consider the upper half of the matrix because this should be a symmetrix matrix
    for i in range(0,number): #total row is 3
        for j in range(i+1,number): #total column is 3
            matrix[i][j] = counter_cosine_similarity(Counter(list_items[i]),Counter(list_items[j]))

    # Save matrix into a file, each number has 4 digit of significant figure
    numpy.savetxt("newfile/similarity_items_only.csv", matrix, fmt = "%.4f", delimiter=",")
    return matrix

# This function inserts the entry score into the topscore if it lies in the range
# topscore is ordered from biggest to smallest
def insertscore(id,score,topscore,N):
    if score < topscore[N-1]:
        return topscore
    else:
        for i in range(0, N):
            if score > topscore[i]:
                topscore.inserts(i,score)
                topname.inserts(i,id)
                topscore.pop()
                topname.pop()

# This function finds the top-N items that are most related to the item in position (x)
def top(matrix,N,x):
    # List of N zeros -> foundation of the score
    topscore = [0]*N
    # List of name
    topname = ["Nan"]*N

    # Traverse the matrix to find the top score
    for i in range(0,number): #total row is 3
        for j in range(i+1,number): #total column is 3
            topscore = insertscore(score,topscore,N)
    return topname

def main():

    # Allow user to enter the ID of the products to generate top-10 cloths
    # that are similar
    print("Hello customer!")
    print("Press 1 if you have the ID of the cloth and want to find similar item.")
    print("Press 2 if you want to enter general description of the item")
    choice = input("Please enter your choice here: ")
    matrix, col = read_file('dat/products.json', choice)

    if col == -1:
        print("ERROR: exiting program")
    else:
        # Ask for how many related items
        print(col)
        N = input("Please input how many related items you want to see: ")



if __name__ == "__main__":
    main()
