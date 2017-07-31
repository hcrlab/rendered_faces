import pandas as pd

# Initializing the pandas table and creating arrays for each dimension
table = pd.read_table('data/SpreadsheetData.tsv')
rows = table.axes[0]
columns = table.axes[1]

# Creating 2D array that will function as our 'spreadsheet'
array2D = []
#array2D.append(table.axes[1])
for i in range(rows.size):
    array2D.append(table.values[i])
#for j in range(rows.size):
#    array2D.append([table[i] for i in range(table.size)])

# A simple search function that returns the number of times a certain item is contained in a single column
# String item - the item to be searched for (examples: blue, x, cen...)
# String column - the column to be searched (examples: eye color, pupil (x/y), eye position...)
# int return - the number of times item appeared in column
def findSame(item: str, column: str) -> int:
    count = 0
    for i in range(columns.size):
        if(columns[i] == column):
            for j in range(len(array2D)):
                if(array2D[j][i] ==  item):
                    count+=1
    print('Found ' + str(count) + ' matching search ' + item)
    return count


# print(table)
findSame("blue", "eye color")

print("Rows: " + str(rows.size))
print("Columns: " + str(columns.size))

for i in range(10):
    print(array2D[i])
