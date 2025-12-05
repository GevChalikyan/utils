import logging
import pandas as pd



def hasNull(df):

  numNullValues = df.isna().sum().sum()
  
  if numNullValues != 0:
    logging.info(f'{numNullValues} null values found!')
    return True
  return False

def cleanData(df):

  if hasNull(df):

    INITIAL_COL = df.shape[1]
    INITIAL_ROWS = df.shape[0]



    # Drops attributes with more than 1/3 null values
    THRESHOLD: int = df.shape[0] - (df.shape[0] / 3)
    logging.info(f'Dropping columns with less than {THRESHOLD} valid values...')

    df = df.dropna(axis=1, thresh=THRESHOLD)



    # Drops all rows with ANY null values
    logging.info('Dropping any remaining rows with null values...')

    df = df.dropna(axis=0)



    # Drops any attributes without any variation
    constant_cols = [col for col in df.columns if df[col].nunique() <= 1]
    logging.info(f'Dropping constant columns:\n\t\t{constant_cols}')

    df = df.drop(columns=constant_cols)



    COL_DROPPED = INITIAL_COL - df.shape[1]
    ROWS_DROPPED = INITIAL_ROWS - df.shape[0]
    logging.info(f'Successfully dropped {COL_DROPPED} columns & {ROWS_DROPPED} rows...')

  logging.info(f'Final shape of dataframe after cleaning: [{df.shape[0]} Rows, {df.shape[0]} Columns]')

  return df