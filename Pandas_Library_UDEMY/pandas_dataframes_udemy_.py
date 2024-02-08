"""
                            DATAFRAMES
--> Series : analogous to 1-Dimensional NumPy array with explicit index
--> DataFrame : analogous to 2-Dimensional NumPy array with an explicit index.
                --> for the rows
                --> for the columns (columns are known as Series)
    --> A DataFrame is simply a collection of Series objects with a common explicit index for the rows.
        --> Series are aligned
        --> The columns (Series) form a Series too.
            --> They can have explicit index which are the column names
--> A DataFrame is essentially a collection of columns that are aligned and have a common row index and the columns
themselves are indexed by an explicit index and an implicit index as well.
    --> It is basically a series of series
    --> It is also a dictionary of dictionaries

                    CONSTRUCTING A DATAFRAME
--> pd.DataFrame(some_arguments) : Arguments can be:
    --> a list of Series objects (columns)
    --> a list of python lists
    --> a list of dictionaries
    --> a dictionary of Series objects (a dictionary where element contains a series object)
    --> a dictionary of dictionaries.
        --> In some cases, row and column explicit indexes are created as expected.
        --> In some cases, we have to define the indexes manually.
    --> from files, e.g csv file, Excel spreadsheets.

                    SOME DATAFRAME PROPERTIES AND METHODS
--> .info() : returns some useful info about the DataFrames, e.g:
    --> a list of the columns, the names in terms of explict index, data type, number of null values and non-null
    values, etc.
--> .transpose() : transposes the dataframe but maintains the indexes.
--> .rename() : allows us to rename the index labels (either on rows and/or columns).
--> .set_index() : allows us to use an existing column in the data frame as a row index.
--> .index : returns the index object used to index the rows.
--> .columns() : returns the index object used to index the columns.
--> .drop() : used to drop rows and columns from the data frame.
"""

import numpy as np
import pandas as pd

# A dataframe is essentially a collection of series objects, and there's an index that is associated with all of the
# series, i.e each row in the DataFrame

# Creating DataFrames: from a list of series objects.
columns = pd.Index([
    'The Bronx',
    'Brooklyn',
    'Manhattan',
    'Queens',
    'Staten Island'
])  # Create the index

# Creating the Series
counties = pd.Series(
    ['Bronx', 'Kings', 'New York', 'Queens', 'Richmond'],
    index=columns,
    name='county')
print(counties)

populations = pd.Series(
    data=[1_418_207, 2_559_903, 1_628_706, 2_253_858, 476_143],
    index=columns,
    name='population')
print(populations)

gdp = pd.Series(
    [42.695, 91.559, 600.244, 93.310, 14.514],
    index=columns,
    name='gdp')

areas = pd.Series(
    [42.10, 70.82, 22.83, 108.53, 58.37],
    index=columns,
    name='area')
print(areas)
print(areas.shape, areas.size)

# Creating the DataFrame
new_york = pd.DataFrame([counties, populations, gdp, areas])
print(new_york)

print(new_york.transpose())

# # Creating DataFrames: from a dictionary of Series Objects

d = {
    'county2': counties,
    'population': populations,
    'gdp': gdp,
    'area': areas
}

new_york = pd.DataFrame(d)
print(new_york)

print(new_york.transpose())

# # # Creating DataFrames: from a dictionary of dictionaries
counties = {
    'The Bronx': 'Bronx',
    'Brooklyn': 'Kings',
    'Manhattan': 'New York',
    'Queens': 'Queens',
    'Staten Island': 'Richmond'
}
populations = {
    # note how the keys are not necessarily in the same order
    'Manhattan': 1_628_706,
    'Queens': 2_253_858,
    'Staten Island': 476_143,
    'The Bronx': 1_418_207,
    'Brooklyn': 2_559_903
}
gdp = {
    'The Bronx': 42.695,
    'Brooklyn': 91.559,
    'Manhattan': 600.244,
    'Queens': 93.310,
    'Staten Island': 14.514
}
areas = {
    'The Bronx': 2.10,
    'Brooklyn': 70.82,
    'Manhattan': 22.83,
    'Queens': 108.53,
    'Staten Island': 58.37
}

d = {
    'county': counties,
    'population': populations,
    'gpd': gdp,
    'area': areas
}

d = {
    'county': counties,
    'population': populations,
    'gdp': gdp,
    'area': areas
}

new_york = pd.DataFrame(d)
print(new_york)

# # # Creating DataFrames: from a list of dictionaries
new_york = pd.DataFrame([counties, populations, gdp, areas])
print(new_york)  # DataFrame would have numbers for row explicit index

# We can re-name row indices using .rename method
new_york = new_york.rename(
    index={
        0: 'county',
        1: 'population',
        2: 'gdp'})

print(new_york)

new_york = new_york.rename(
    index={
        0: 'county',
        1: 'population',
        2: 'gdp',
        3: 'area'})

print(new_york)

print(new_york.transpose())

new_york = pd.DataFrame([counties, populations, gdp, areas]).transpose()
print(new_york)

new_york1 = new_york.rename(
    columns= {
        0: 'county',
        1: 'population',
        2: 'gdp',
        3: 'area'}
)

print(new_york1)

# # # Creating DataFrames: from a list of lists
burroughs = ['The Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
counties = ['Bronx', 'Kings', 'New York', 'Queens', 'Richmond']
populations = [1_418_207, 2_559_903, 1_628_706, 2_253_858, 476_143]
gdp = [42.695, 91.559, 600.244, 93.310, 14.514]
areas = [42.10, 70.82, 22.83, 108.53, 58.37]

data = [burroughs, counties, populations, gdp, areas]

new_york1 = pd.DataFrame(
    data
)

print(new_york1)

new_york1 = pd.DataFrame(
    data,
    index=['burrough', 'county', 'population', 'gdp', 'area'])


new_york1 = new_york1.transpose()
print(new_york1)

# Setting a column to index
print(new_york1.set_index('burrough'))

print(new_york1.set_index('county'))


df = new_york1.set_index('county')

print(df.loc['Bronx'])

print(new_york1)
new_york1.set_index('burrough', inplace=True)
print(new_york1)

