import logging
import os
from pathlib import Path





try:
  LOG_DIR = '../logs/'
  LOG_FILE = 'app.log'
  LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
  log_setup_info = []



  if not os.path.isfile(LOG_PATH):
    log_setup_info.append((logging.WARNING, 'Log file missing'))

    if not os.path.isdir(LOG_DIR):
      log_setup_info.append((logging.WARNING, 'Log directory missing'))

      os.mkdir(LOG_DIR)
      log_setup_info.append((logging.INFO, f'Successfully created log directory at \'{LOG_DIR}\''))

    with open(LOG_PATH, 'w') as f:
      log_setup_info.append((logging.INFO, f'Successfully created log file at \'{LOG_PATH}\''))



  logging.basicConfig(
    filename=LOG_PATH, 
    level=logging.INFO, 
    filemode='w',
    format='%(asctime)s | %(levelname)s:\n\t%(message)s'
  )

  

  for log in log_setup_info:
    logging.log(level=log[0], msg=log[1])

  logging.info('Successfully setup logger.')
  print(f'Read logs for full information at {(Path.cwd() / LOG_PATH).resolve()}')

except Exception as e:
  print(f'Logging setup failed:\n{e}')
  exit(1)