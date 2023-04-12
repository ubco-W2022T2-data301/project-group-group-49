'''
First Python Module Made by Anilov Laxina ID 36694933

'''
import pandas as pd

'''
Takes the URL to csv file and filters out the United States.
It does this to help demonstrate the most common occurrences of Mental Health Issues
in the U.S as well as remove/drop the extreme values such as a negative and overly old age.

Returns the pivot table, which is a table that has the ages of individuals from the U.S as columns.
The rows are the occurrences themselves.
'''
def load_and_isolate_US(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)
    df = (
          pd.read_csv(url_or_path_to_csv_file)
      )

    # Method Chain 2 (Filter out non-US data)
    filtered_df = (
          df[df['Country'] == 'United States']
          .reset_index(drop=True)
      )

    # Method Chain 3 (Group the data by Country and Age, and count the occurrences)
    grouped = (
          filtered_df.groupby(['Country', 'Age'])
          .size()
          .reset_index(name='counts')
      )
    
    # Method Chain 4 (Remove Negative & Extreme Ages)
    pivot = (pd.pivot_table(grouped, values='counts', index=['Country'], columns=['Age'], aggfunc='sum', fill_value=0)
             .drop([-29, -1,329], axis=1)
             
      )

    return pivot