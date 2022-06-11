import logging

# DEBUG -> INFO -> WARNING -> ERROR -> CRITICAL

name = "some text"
number = 52

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

# doing ssom random things...
logging.info("doing some string concatenation...")
logging.info("doing str to int typcasting...")
try:
    number = str(number)
    logging.info("str to int typcasting successful!")
except:
    logging.warning("str to int casting failed! Setting to 0")
    number = '0'
try:
    print("some text with some number " + number)
    logging.info("string concatenation successful!")
except:
    logging.error("string concatenation failed!")
