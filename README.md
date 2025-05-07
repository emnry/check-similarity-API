# API de Similarité Sémantique (Word2Vec Français)

Cette API permet d'obtenir la similarité sémantique entre deux mots français (/similarity)

Elle utilise un modèle Word2Vec préentraîné en français fourni par Jean-Philippe Fauconnier.

## 🔧 Prérequis
* Python 3.7+
* pip
* Un modèle Word2Vec binaire préentraîné : `https://embeddings.net/embeddings/frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin`
  ou autre modèle sur `http://fauconnier.github.io/#data` (nécessite un changement du nom dans le MODEL_PATH de app.py)

## 📦 Installation

### 1. Cloner ce dépôt :

```bash
git clone https://github.com/emnry/check-similarity-API.git
cd check-similarity-API
```

### 2. Créer un environnement virtuel (recommandé) :

```bash
python -m venv venv
# Sur Windows
venv\Scripts\activate
# Sur Mac/Linux
source venv/bin/activate
```

### 3. Installer les dépendances :

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Mise en place du modèle :
Placer le model Word2Vec dans un nouveau dossier `models`

## 📁 Arborescence

```python
.
├──env/
│   └──...
├── app.py
├── models/
│   └── frWac_non_lem_no_postag_no_phrase_500_skip_cut100.bin
├── requirements.txt
└── README.md

```

## 🚀 Lancer le serveur

```python
python app.py
```

Le serveur tourne sur :
📍 http://127.0.0.1:5000

## 🔗 Exemmples d'utilisation
`/similarity?word1=mot1&word2=mot2`
Renvoie un score de similarité entre deux mots :
```
GET http://127.0.0.1:5000/similarity?word1=maison&word2=immeuble
```

## 🌐 Accès depuis un autre site (CORS)
L’API accepte les requêtes depuis d'autres domaines grâce à `flask-cors`.
