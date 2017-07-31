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
    robots = []
    for col in range(columns.size):
        if(columns[col] == column):
            for row in range(len(array)):
                print('len = ' + str(len(array)))
                print('len[row] = ' + str(len(array[row])))
                print('array[' + str(col) + ']')
                print('array[' + str(row) + '][' + str(col) + ']')
                if(array[row][col] ==  item):
                    robots.append(array2D[i])
    print(robots)
    return robots

# String item1 - the first item to be searched for (examples: blue, x, cen...)
# String column1 - the first column to be searched (examples: eye color, pupil (x/y), eye position...)
# String item2 - the second item to be searched for
# String column2 - the second column to be searched
# int return - the number of times item appeared in column
def find2Combo(item1: str, column1: str, item2: str, column2: str) -> int:
    count = 0
    matches = findSame(array2D, item1, column1)
    countSame(array2D, item1, column1)
    count = countSame(matches, item2, column2)
    return count

# print(table)
countSame(array2D, "blue", "eye color")
find2Combo("black", "face color", "blue", "eye color")

print("Rows: " + str(rows.size))
print("Columns: " + str(columns.size))

#for i in range(10):
#    print(array2D[i])
