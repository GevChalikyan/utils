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

    # Drops attributes with more than 1/3 null values
    THRESHOLD: int = df.shape[0] - (df.shape[0] / 3)
    logging.info(f'Dropping columns with less than {THRESHOLD} valid values...')
    INITIAL_COL = df.shape[1]

    df = df.dropna(axis=1, thresh=THRESHOLD)

    COL_DROPPED = INITIAL_COL - df.shape[1]
    logging.info(f'Successfully dropped {COL_DROPPED} columns...')





    # Drops all rows with ANY null values
    logging.info('Dropping any remaining rows with null values...')
    INITIAL_ROWS = df.shape[0]

    df = df.dropna(axis=0)

    ROWS_DROPPED = INITIAL_ROWS - df.shape[0]
    logging.info(f'Successfully dropped {ROWS_DROPPED} rows...')

  logging.info(f'Final shape of dataframe after cleaning: [{df.shape[0]} Rows, {df.shape[0]} Columns]')

  return df