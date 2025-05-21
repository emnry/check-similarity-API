# check-Similarity-API – API de Similarité Sémantique en Français

Cette API permet de calculer la **similarité sémantique entre deux mots français** en utilisant un modèle préentraîné Word2Vec de type **FastText**.

## 🚀 Fonctionnalités

* Calcul de similarité entre deux mots (`/similarity`)
* Vérification de l’état de l’API (`/health`)
* Serveur web simple avec Flask

---

## 🧠 Modèle utilisé

Le modèle Word2Vec utilisé est un **modèle français** disponible sur le site de FastText :
🔗 [https://fasttext.cc/docs/en/crawl-vectors.html](https://fasttext.cc/docs/en/crawl-vectors.html)

Modèle attendu : `frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin` (binaire)

Placez le modèle dans un dossier `models/`.

---

## 📦 Installation

### 1. Cloner le dépôt

```bash
git clone <url-du-repo>
cd checkSimilarityAPI
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 🛠️ Lancement de l’API

Assurez-vous que le modèle Word2Vec est bien dans `models/frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin`.

```bash
python app.py
```

Le serveur s'exécute par défaut sur `http://0.0.0.0:5000`.

---

## 📚 Routes disponibles

### `GET /`

Retourne un message de bienvenue.

---

### `GET /health`

Permet de vérifier si le modèle a été correctement chargé.

**Réponse :**

```json
{
  "status": "ok"
}
```

---

### `GET /similarity?word1=motA&word2=motB`

Calcule la similarité entre deux mots (`word1` et `word2`).

**Paramètres requis :**

* `word1` : premier mot (ex: "roi")
* `word2` : second mot (ex: "reine")

**Réponse en cas de succès :**

```json
{
  "similarity": 0.723,
  "vector1": [...],
  "vector2": [...]
}
```

**Réponse en cas d'erreur :**

```json
{
  "error": "Les deux mots doivent être fournis."
}
```

ou

```json
{
  "error": "Un ou les deux mots ne sont pas dans le vocabulaire."
}
```

---

## ✅ Exemples d’utilisation

```bash
curl "http://localhost:5000/similarity?word1=chat&word2=chien"
```

---

## 📁 Structure du projet

```
.
├── env
|   └── ...
├── static
|   └── index.html
|   └── main.js
├── app.py
├── requirements.txt
└── models/
    └── frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin
```

---

## 🧩 Dépendances principales

* `Flask` – pour exposer l’API
* `Flask-CORS` – pour gérer les requêtes cross-origin
* `gensim` – pour charger le modèle Word2Vec
* `numpy` – pour la manipulation des vecteurs

---

## 📄 License

Projet à usage pédagogique ou expérimental. Tu peux l'adapter librement.

---
