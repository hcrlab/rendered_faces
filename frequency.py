from locale import normalize
import pandas as pd
import numpy as np

# path to spreadsheet file - tab separated file format
file_path='data/Filtered Face Data - data_wo_hidden.tsv'
# pandas takes a .tsv as a default, so no need for parameters
# read in file, results in a DataFrame object
table = pd.read_table(file_path)
# exclude faces which use back-projection screens
table = table[table['screen type'] != 'back']

# list of columns to ignore when clustering
cols_to_ignore = ['Name',
                  'robot type',
                  'category',
                  'screen type',
                  'physical features',
                  'robot height',
                  'embodiment',
                  'face turns other colors',
                  'face shape',
                  'screen size',
                  'head motion',
                  'face motion',
                  'info display',
                  'eye turns other colors (inside)',
                  'eye turns other shapes (exclude blink)',
                  'blink type',
                  'eye motion',
                  'pupil and/or iris motion',
                  'glare motion',
                  'wink',
                  'mouth motion',
                  'nose motion',
                  'eyebrow independent motion',
                  'eyebrow motion',
                  'country/region of origin',
                  'year']

cols_binary_features = ['full head',
                    'mouth',
                    'nose',
                    'eyebrows',
                    'cheeks (blush)',
                    'hair',
                    'ears',
                    'pupil (y/n)',
                    'lid',
                    'iris',
                    'eyelashes']

cols_no_NA_option = ['full head',
                    'mouth',
                    'nose',
                    'eyebrows',
                    'cheeks (blush)',
                    'hair',
                    'Ears',
                    'face color',
                    'eye color',
                    'eye shape',
                    'pupil (y/n)',
                    'Lid',
                    'Iris',
                    'eye size',
                    'eye placement',
                    'eye spacing']

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

def get_headers(df):
    """ return list of column headers in a DataFrame """
    return df.columns.values

def groupby_cols(df, col_list):
    """ return total amount of faces fitting certain column criteria """
    # group all robots according to list of column names
    results = df.groupby(col_list)['Name'].count()
    # order the results
    results = results.sort_values(ascending=False)
    print(results)
    # groupby_result.to_csv('groupby_results.txt', header=True, sep='\t')
    # print("results written to file")

def cluster_by_range(df, lower_bound):
    """ return total amount of faces fitting certain column criteria """
    # get total number of robot faces in data set
    total_rows = len(df)
    # determine the upper bound percentage
    upper_bound = 100 - lower_bound
    # lists of which columns to fix and which to cluster
    cols_to_fix = []
    cols_to_cluster= []
    # iterate over every column in dataframe
    for col in df:
        # drop any column we are ignoring
        if df[col].name in cols_to_ignore:
            df = df.drop(df[col].name, 1)
            continue
        # count & calculate percentage representation for each value of the column
        col_check = df.groupby(col).size().reset_index(name='count')
        col_check['as_percent'] = 100 * col_check['count']/float(total_rows)
        # if percentage is over the upper bound, add it to list of features to fix
        if not col_check[col_check['as_percent'] >= upper_bound].empty:
            cols_to_fix.append(df[col].name)
        # if percentage is over the lower bound, add it to list of features to vary
        elif not col_check[col_check['as_percent'] >= lower_bound].empty \
                and col_check[col_check['as_percent'] >= upper_bound].empty:
            cols_to_cluster.append(df[col].name)
    # generate clusters based on list of what features to vary
    groupby_result = df.groupby(cols_to_cluster).size().reset_index(name='count')
    groupby_result['as_percent'] = 100 * groupby_result['count'] / float(total_rows)
    groupby_result = groupby_result.sort_values(by='as_percent', ascending=False)
    # print results to file
    filename = str(lower_bound) + '_percent_clusters.tsv'
    groupby_result.to_csv(filename, header=True, sep='\t')
    print("results written to file")

# generate clusters for every range from 15-85% to 45-55%
for num in range(15,50,5):
    cluster_by_range(table, num)