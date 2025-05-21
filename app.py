from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from gensim.models import KeyedVectors
import numpy as np

MODEL_PATH = "models/frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin"

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Bienvenue sur l'API Word2Vec Francaise"

# Charger le modèle Word2Vec
print("Chargement du modèle Word2Vec...")
try:
    model = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True, unicode_errors="ignore")
    print("Modèle chargé avec succès.")
except Exception as e:
    print(f"Erreur lors du chargement du modèle: {e}")
    model = None  # S'assurer que le modèle est bien défini même en cas d'erreur

@app.route('/similarity', methods=['GET'])
def similarity():
    word1 = request.args.get('word1') 
    word2 = request.args.get('word2')

    if not word1 or not word2:
        return jsonify({'error': 'Les deux mots doivent être fournis.'}), 400

    if word1 not in model or word2 not in model:
        return jsonify({'error': f'Un ou les deux mots ne sont pas dans le vocabulaire : {word1}, {word2}'}), 400

    try:
        similarity_score = float(model.similarity(word1, word2))
        vector1_list = model[word1].tolist()
        vector2_list = model[word2].tolist()

        return jsonify({
            'similarity': similarity_score,
            'vector1': vector1_list,
            'vector2': vector2_list
        })

    except Exception as e:
        print(f"Erreur de calcul de similarité : {e}")
        return jsonify({'error': 'Erreur interne lors du calcul de la similarité.'}), 500

@app.route('/health', methods=['GET'])
def health():
    # Vérifier que le modèle est chargé pour répondre positivement
    if model is None:
        return jsonify({'status': 'error', 'message': 'Le modèle n\'est pas chargé.'}), 500
    
    # Retourner un status 200 si tout va bien
    return jsonify({'status': 'ok'}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)