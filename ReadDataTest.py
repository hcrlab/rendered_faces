import pandas as pd

# Initializing the pandas table and creating arrays for each dimension
table = pd.read_table('data/SpreadsheetData.tsv')
rows = table.axes[0]
columns = table.axes[1]

# Creating 2D array that will function as our 'spreadsheet'
array2D = []
for i in range(rows.size):
    array2D.append(table.values[i])


# A simple search function that returns the number of times a certain item is contained in a single column
# String[] array - the array of robots to search
# String item - the item to be searched for (examples: blue, x, cen...)
# String column - the column to be searched (examples: eye color, pupil (x/y), eye position...)
# int return - the number of times item appeared in column
def countSame(array, item: str, column: str) -> int:
    count = len(findSame(array, item, column))
    print('Found ' + str(count) + ' matching search \"' + item + '\" in \"' + column + '\"')
    return count


# A simple search function that returns all the robots with a certain feature in a certain column
# String[] array - the array of robots to search
# String item - the item to be searched for (examples: blue, x, cen...)
# String column - the column to be searched (examples: eye color, pupil (x/y), eye position...)
# [] return - the the array of robots for which item appeared in column
def findSame(array, item: str, column: str):
    print('Searching for \"' + str(item) + '\" in \"' + str(column) + '\"')
    robots = []
    # For every column,
    for col in range(columns.size):
        # If the current column is the desired one,
        if(columns[col] == column):
            # For each robot in that column,
            for row in range(len(array)):
                #print('len = ' + str(len(array)))
                #print('len[row] = ' + str(len(array[row])))
                print('columns[' + str(col) + '] = ' + str(columns[col]))
                print('array[' + str(row) + '][' + str(col) + ']')
                print(str(array[row][col]) + ' is not equal to ' + str(item))
                # If a robot's feature matches,
                if(array[row][col] ==  item):
                    # Add it to the list
                    robots.append(array2D[i])
    print('len(robots) = ' + str(len(robots)))
    return robots


# String item1 - the first item to be searched for (examples: blue, x, cen...)
# String column1 - the first column to be searched (examples: eye color, pupil (x/y), eye position...)
# String item2 - the second item to be searched for
# String column2 - the second column to be searched
# int return - the number of times item appeared in column
def find2Combo(item1: str, column1: str, item2: str, column2: str) -> int:
    count = 0
    # The robots with the first feature are saved
    matches = findSame(array2D, item1, column1)
    countSame(array2D, item1, column1)
    # Out of the robots with the first feature, the robots with the second feature also are returned
    count = countSame(matches, item2, column2)
    return count

# print(table)
countSame(array2D, "blue", "eye color")
find2Combo("black", "face color", "blue", "eye color")

print("Rows: " + str(rows.size))
print("Columns: " + str(columns.size))
