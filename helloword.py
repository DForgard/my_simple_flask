from flask import Flask
app = Flask(__name__)
# on appelle ce bloc une route
# elle sera accessible via: www.localhost:81/hello
@app.route('/hello')
def index():
   return 'Hello from Flask!'
# on appelle ce bloc une route
# elle sera accessible via: www.localhost:81/index
@app.route('/bonjour')
def index():
   return 'Bonjour depuis Flask!'
# nous allons exécuter l'application Flask sur l'ordinateur hôte:
# d'ou : localhost
# le port que nous allons attribuer au serveur est: 81
# debug= True nous permet de modifier le code et maintenir l'application
# flask en route.
app.run(host='localhost', port=81, debug=True)