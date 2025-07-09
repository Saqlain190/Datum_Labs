import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(levelno)s - %(funcName)s - %(message)s',
    filename='Even.log',
    filemode='w'
    )
try:
    logging.info("Printing even numbera from 1 to 20")
    for i in range(1,21):
        if i % 2 ==0:
            print(i)
except Exception as e:
    logging.error(f"Error occurred while printing even numbers: {e}")
