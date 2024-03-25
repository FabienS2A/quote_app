from flask import Flask, render_template
from pymongo import MongoClient
from bson import json_util
from components.mail import send_email_alert
from components.log import log_for_quotes
import logging


app = Flask(__name__)

# Configuration de la connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['briek_quotes']
collection = db['quotes_scrap']

log_for_quotes()

# Route pour effectuer une requête
@app.route('/', methods=['GET'])
def get_data():
    random_quote = db.quotes_scrap.aggregate([{ '$sample': { 'size': 1 } }]).next()
    #Formater les données pour la réponse JSON
    result = {
        'text': random_quote['text'],
        'author': random_quote['author'],
    }

    send_email_alert()
    
    logging.info('Ceci est un message informatif')
    

    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)