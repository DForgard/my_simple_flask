from flask import render_template
from flask import Flask
app = Flask(__name__)
# on définit les chemins ou:
# vous trouverez les templates
# vous trouverez les fichiers statiques
app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
# Cette route est formatée via le template jinja2.
# Elle va être affichée dans le navigateur web
# en suivant la structure du fichier index.html


@app.route('/formated')
def index():
    name = 'PIERRE'
    return render_template('index.html',
                           title='Welcome',
                           username=name)
