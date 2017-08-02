import pandas as pd
import matplotlib.pyplot as plt

# path to spreadsheet file - tab separated file format
file_path='data/Filtered Face Data - data_wo_hidden.tsv'
# pandas takes a .tsv as a default, so no need for parameters
# read in file, results in a DataFrame object
table = pd.read_table(file_path)

# list of all columns that fit within our 15%-85% range
cols_in_range = [
                'face color',
                'mouth',
                'mouth length',
                'mouth placement',
                'mouth color (or outline color)',
                'nose',
                'nose color',
                'nose shape',
                'nose size',
                'nose placement',
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
                ]

# list of all binary features that fit within our 15%-85% range
cols_features = [
                'mouth',
                'nose',
                'eyebrows',
                'pupil (y/n)',
                'cheeks (blush)'
                ]

# list of all feature color values that fit within our 15%-85% range
cols_feature_colors = [
                    'face color',
                    'mouth color (or outline color)',
                    'nose color',
                    'eyebrow color',
                    'eye color',
                    'lashes color'
                    ]

def plot_pie(s):
    """ generate pie chart for a given Series """
    s.plot.pie(
        autopct='%1.1f%%',
        figsize=(6, 6))
    plt.savefig('pie_chart.png')

def plot_area(df, filename):
    """ generate unstacked area chart for a given DataFrame """
    df.plot.area(stacked=False)
    plt.grid(which='both')
    # replace any forward slashes in the column title so the file name works
    plt.savefig(filename.replace("/", "-") + '_chart.png')

def plot_bar(df, col, filename):
    df.plot(x=col, figsize=(20,12), kind='bar')
    # replace any forward slashes in the column title so the file name works
    plt.savefig(filename.replace("/", "-") + '_chart.png')

def plot_feature_overlap(df, features_list, filename):
    """ generate unstacked area chart for several columns in a DataFrame """
    # create blank dataframe to store results
    results = pd.DataFrame()
    # iterate over dataframe parameter columns
    for col in df:
        # if current column is in list to be graphed, generate percentages
        # associated with the feature, and add it to the results dataframe
        if df[col].name in features_list:
            col_vals = df[col].value_counts(normalize=True)
            results[df[col].name] = col_vals
    # plot the area graph of chosen features
    plot_area(results, filename)

def plot_num_categories(df):
    # create blank dataframe to store results
    results = pd.DataFrame(columns=["category", "num_categories"])
    for col in df:
        # don't include the Name category in our results
        if df[col].name == 'Name':
            continue
        results = results.append({
                    "category": df[col].name,
                    "num_categories": len(df.groupby(col))
                    }, ignore_index=True)
    plot_bar(results, "category", "num_per_dimension")

# Ex: plot an area chart of all features that use colors
#plot_feature_overlap(table, cols_feature_colors, "feature_colors")
