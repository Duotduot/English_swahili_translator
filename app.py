from flask import Flask, request, jsonify, abort
from google.cloud import translate_v2 as translate
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://swahili_user:swahiliuser123@localhost/swahili_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
translate_client = translate.Client()

# Translation model definition 
class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_text = db.Column(db.Text)
    source_language = db.Column(db.String(2))
    target_language = db.Column(db.String(2))
    translated_text = db.Column(db.Text)

# Language model definition 
class Language(db.Model):
    language_id = db.Column(db.String(2), primary_key=True)
    language_name = db.Column(db.String(100))

# Error handling decorator 
@app.errorhandler(Exception)
def handle_error(error):
    response = {
        'error': 'An unexpected error occurred.'
    }
    return jsonify(response), 500

# Translate endpoint 
@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        source_text = data.get('source_text')
        source_language = 'en'
        target_language = 'sw'

        if not source_text or not source_language or not target_language:
            abort(400, 'Invalid request. Missing required parameters.')

        # Google Cloud Translation API
        translation = translate_client.translate(
            source_text, source_language=source_language, target_language=target_language
        )

        translated_text = translation['translatedText']

        response = {
            'translated_text': translated_text
        }
        return jsonify(response)
    except Exception as e:
        abort(500, 'An error occurred during translation.')

# Languages endpoint
@app.route('/languages', methods=['GET'])
def get_languages():
    try:
        response = translate_client.get_languages()

        languages = []
        for language in response:
            language_id = language['language']
            language_name = language['name']
            languages.append({'language_id': language_id, 'language_name': language_name})

            # Connect to the database
            connection = psycopg2.connect('postgresql://swahili_user:swahiliuser123@localhost/swahili_db')
            cursor = connection.cursor()

            # Fetch the list of supported languages
            cursor.execute("SELECT * FROM language")
            languages = cursor.fetchall()

            # Closing the database connection
            cursor.close()
            connection.close()

        response = {
            'languages': languages
        }
        return jsonify(response)
    except Exception as e:
        abort(500, 'An error occurred while retrieving languages.')
    
    
    
if __name__ == '__main__':
    app.run()




