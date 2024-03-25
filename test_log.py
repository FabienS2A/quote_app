from components.log import log_for_quotes
import logging


log_for_quotes()

try :
    print(a)
except:
    print("a n'est pas une variable")
    logging.error('Ceci est une erreur')