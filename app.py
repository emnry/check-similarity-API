from flask import Flask, request, jsonify
from flask_cors import CORS
from gensim.models import KeyedVectors

MODEL_PATH = "models/frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin"

app = Flask(__name__)
CORS(app)

print("Chargement du modèle Word2Vec...")
model = KeyedVectors.load_word2vec_format(MODEL_PATH, binary=True, unicode_errors="ignore")
print("Modèle chargé avec succès.")

@app.route("/similarity", methods=["GET"])
def word_similarity():
    word1 = request.args.get("word1", "").strip()
    word2 = request.args.get("word2", "").strip()
    if not word1 or not word2:
        return jsonify({"error": "Deux mots doivent être fournis (word1 et word2)."}), 400
    try:
        similarity = model.similarity(word1, word2)
        return jsonify({
            "word1": word1,
            "word2": word2,
            "similarity": round(float(similarity), 4)
        })
    except KeyError as e:
        return jsonify({"error": f"Mot introuvable dans le modèle : {str(e)}"}), 404

if __name__ == "__main__":
    app.run(debug=True)
