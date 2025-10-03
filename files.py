import logging
import os

def validate_dir(file_path):

  dir = os.path.dirname(file_path)
  if not os.path.isdir(dir):
    os.makedirs(dir)
    logging.info(f'Created new directory: \'{dir}\'')