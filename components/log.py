import logging
import os
import socket
from datetime import datetime


def log_for_quotes():
    # Configurez le niveau de journalisation
    log_file_path = 'logs/app.log'

    # Vérifiez si le dossier 'logs' existe, sinon, créez-le
    log_folder = os.path.dirname(log_file_path)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Vérifiez si le fichier journal existe, sinon, créez-le
    if not os.path.isfile(log_file_path):
        with open(log_file_path, 'w'):
            pass  # Créez simplement le fichier vide

    # Configurez le niveau de journalisation et le format des messages
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_file_path, 'a'), logging.StreamHandler()])


    # Ajoutez le filtre au logger
    logger = logging.getLogger()
    

    #Écrivez des messages dans le journal
    #logging.debug('Ceci est un message de débogage')
    #logging.info('Ceci est un message informatif')
    #logging.warning('Ceci est un avertissement')
    #logging.error('Ceci est une erreur')
    #logging.critical('Ceci est une erreur critique')

#log_for_quotes()

#try :
    #print(a)
#except:
    #print("a n'est pas une variable")
    #logging.error('Ceci est une erreur')
          
