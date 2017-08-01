import pandas as pd
import numpy as np

# path to spreadsheet file - tab separated file format
file_path='data/Filtered Face Data - data.tsv'
# pandas takes a .tsv as a default, so no need for parameters
# read in file, results in a DataFrame object
table = pd.read_table(file_path)
# drop the "notes" column from the data file
# dataframe = dataframe.drop('column_name', 1) >> where 1 is the axis number (0 for rows and 1 for columns.)
table = table.drop('notes', 1)

def most_freq_cols(dataframe):
    """ display most frequent occurrences of a column value in a DataFrame """
    for col in dataframe:
        print(dataframe[col].value_counts())

def get_mode(dataframe):
    """ display the mode of a column constrained by another column. in this example, print
    the most common eye color for each face color """
    mode = lambda x: x.mode() if len(x) > 2 else np.array(x)
    print(dataframe.groupby('face color')['eye color'].agg(mode))

def groupby_cols(dataframe):
    """ return total amount of faces fitting certain column criteria """
    """ groupby_result = dataframe.groupby(['face color',
                                        'mouth',
                                        'mouth length',
                                        'mouth placement ',
                                        'mouth color (or outline color)',
                                        'nose',
                                        'nose color',
                                        'nose shape',
                                        'nose size',
                                        'nose placement ',
                                        'eyebrows',
                                        'eyebrow color',
                                        'eyebrow length',
                                        'eyebrow arch',
                                        'eye size',
                                        'eye shape',
                                        'eye placement',
                                        'eye color',
                                        '# glare circles',
                                        'pupil (y/n)',
                                        'iris',
                                        'lashes color',
                                        'cheeks (blush)',
                                        'cheek shape',
                                        'cheek size',
                                        'cheek placement',
                                        'cheek spacing'
                                        ])['Name'].count() """
    groupby_result = dataframe.groupby(['face color',
                                        'mouth',
                                        'nose',
                                        'eyebrows',
                                        'eye size',
                                        'eye shape',
                                        'eye placement',
                                        'eye color',
                                        '# glare circles',
                                        'pupil (y/n)',
                                        'iris',
                                        'lashes color',
                                        'cheeks (blush)',
                                        ])['Name'].count()
    groupby_result = groupby_result.sort_values(ascending=False)
    print(groupby_result)
    # groupby_result.to_csv('groupby_results.txt', header=True, sep='\t')
    # print("results written to file")