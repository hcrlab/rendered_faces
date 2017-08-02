import pandas as pd
import numpy as np

# path to spreadsheet file - tab separated file format
file_path='data/Filtered Face Data - data_wo_hidden.tsv'
# pandas takes a .tsv as a default, so no need for parameters
# read in file, results in a DataFrame object
table = pd.read_table(file_path)

def category_freq(dataframe):
    """ display descending list of category frequencies per column, with percentages """
    total_rows = len(dataframe)
    for col in dataframe:
        # don't include the Name category in our results
        if dataframe[col].name == 'Name':
            continue
        num_categories = len(dataframe.groupby(col))
        print(
            "---- %s TOTAL CATEGORIES FOR %s ----"
            % (num_categories, dataframe[col].name))
        # generate series to list occurrences of each column value
        col_vals = dataframe[col].value_counts()
        # store series as DataFrame
        result_df = col_vals.to_frame()
        # generate series to display percentages
        as_percent = 100 * col_vals/float(total_rows)
        # append percentages column to DataFrame
        result_df['percentage'] = as_percent
        print(result_df)

def get_mode(dataframe):
    """ display the mode of a column constrained by another column. in this example, print
    the most common eye color for each face color """
    mode = lambda x: x.mode() if len(x) > 2 else np.array(x)
    print(dataframe.groupby('face color')['eye color'].agg(mode))

def groupby_cols(dataframe):
    """ return total amount of faces fitting certain column criteria """
    # group all robots by feature presence/absence
    groupby_result = dataframe.groupby([
                                        'mouth',
                                        'nose',
                                        'eyebrows',
                                        'pupil (y/n)',
                                        'cheeks (blush)',
                                        'hair',
                                        'ears'
                                        ])['Name'].count()
    # order the results
    groupby_result = groupby_result.sort_values(ascending=False)
    print(groupby_result)
    # groupby_result.to_csv('groupby_results.txt', header=True, sep='\t')
    # print("results written to file")