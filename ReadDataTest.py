import pandas as pd

# Initializing the pandas table and creating arrays for each dimension
table = pd.read_table('data/SpreadsheetData.tsv')
rows = table.axes[0]
columns = table.axes[1]

# Creating 2D array that will function as our 'spreadsheet'
array2D = []
for j in range(rows.size):
    array2D.append([columns[i] for i in range(columns.size)])


def findSame(item, column):
    count = 0
    for i in range(columns.size):
        if(columns[i].equals(column)):
            for j in range(rows.size):
                if(rows[j].equals(item)):
                    count+=1
    print('Found ' + str(count) + ' matching search ' + item)
    return count


# print(table)

print("Rows: " + str(rows.size))
print("Columns: " + str(columns.size))

print(array2D[0])
