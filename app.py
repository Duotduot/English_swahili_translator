from flask import Flask, request, jsonify 
from google.cloud import translate_v2 as translate
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://duot_duot:duotduot123@localhost/english_swahili'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
translate_client = translate.Client(390706)

@app.route('/translate', methods=['POST'])
class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_text = db.Column(db.Text)
    source_language = db.Column(db.String(2))
    target_language = db.Column(db.String(2))
    translated_text = db.Column(db.Text)

def translate():
    data = request.get_json()
    source_text = data.get('source_text')
    source_language = data.get('source_language')
    target_language = data.get('target_language')

    # Google Cloud Translation API
    translation = translate_client.translate(
        source_text, source_language=source_language, target_language=target_language
    )

    translated_text = translation['translatedText']

    response = {
        'translated_text': translated_text
    }
    return jsonify(response)

@app.route('/languages', methods=['GET'])
class Language(db.Model):
    language_id = db.Column(db.String(2), primary_key=True)
    language_name = db.Column(db.String(100))

def get_languages():

    response = translate_client.get_languages()

    languages = []
    for language in response:
        language_id = language['language']
        language_name = language['name']
        languages.append({'language_id': language_id, 'language_name': language_name})

        # Connect to the SQLite database
        connection = sqlite3.connect('english_swahili.db')
        cursor = connection.cursor()

        # Fetch the list of suppported languages
        cursor.execute("SELECT * FROM languages")
        languages = cursor.fetchall()

        # Close the database connection
        cursor.close()
        connection.close()

        response = {
            'languages': languages
        }
        return jsonify(response)




