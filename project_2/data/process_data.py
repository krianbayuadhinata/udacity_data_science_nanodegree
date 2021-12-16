import sys
import pandas as pd
import numpy as np
import sqlalchemy
import sqlite3

def load_data(messages_filepath, categories_filepath):
    """
    Load and then merge dataset 'messages_filepath' and 'categories_filepath'.

    Parameters:
    messages_filepath: path of messages.csv file
    categories_filepath: path of categories.csv file

    Returns:
    merged_df: messages_filepath and categories_filepath that has been merged

    """
    # load datasets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    # merge datasets on common id and assign to df
    merged_df = messages.merge(categories, how='outer', on='id')
    return merged_df


def clean_data(df):
    """
    Check missing data, duplicated data, data type of the DataFrame,
    then doing some data cleansing e.g drop null, impute data, drop duplicate data.

    Parameters:
    df: merged messages and categories DataFrame

    Returns:
    df: cleaned DataFrame

    """
    categories = df['categories'].str.split(';', expand=True)
    row = categories.iloc[1]
    category_colnames = row.apply(lambda x: x.split('-')[0])
    categories.columns = category_colnames

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)

    df.drop(columns='categories', inplace=True)
    df = pd.concat([df, categories], axis=1)
    df.drop_duplicates(inplace=True)

    return df


def save_data(df, database_filepath):
    """
    store clean DataFrame into database using SQLite.

    Parameters:
    df: merged messages and categories DataFrame
    database_filename: path of database filename

    Returns:
    None

    """
    engine = sqlalchemy.create_engine(f'sqlite:///{database_filepath}')
    df.to_sql('messages', engine, index=False, if_exists='replace')


def main():
    if len(sys.argv) == 4:
        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)

        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)

        print('Cleaned data saved to database!')

    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'messages.db')


if __name__ == '__main__':
    main()
