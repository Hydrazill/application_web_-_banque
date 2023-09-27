#--- coding:UTF-8 ---

from flask import Flask, request, render_template
from pickle import *
from copy import deepcopy
from module import *

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'root'

@app.route('/', methods=['GET', 'POST'])
def demarrage():
    return render_template('index.html')

@app.route('/inscription', methods=['GET', 'POST'])
def formulaireinscription():
    if request.method == 'POST' and 'inscription-form' in request.form:
        nomins = request.form.get('nomins')
        motdepasseins = request.form.get('motdepasseins')
        cmotdepasseins = request.form.get('cmotdepasseins')
        
        if motdepasseins == cmotdepasseins:
            if searchUser(nomins) == False:
                chaine = str(nomins) + " " + str(motdepasseins) + " " + str(0) + "\n"
                with open('comptes.dat', 'ab') as fichier:
                    dump(chaine, fichier)
            else:
                return render_template('alert3.html')
        else:
            return render_template('alert1.html')
        
        
        return render_template('index.html')
        
@app.route('/connexion', methods=['GET', 'POST'])
def formulaireconnexion():
    global user
    
    if request.method == 'POST' and 'connexion-form' in request.form:
        nomcon = request.form.get('nomcon')
        motdepassecon = request.form.get('motdepassecon')
        
        
        if searchUser(nomcon, motdepassecon) == False:
            return render_template('alert2.html')
        else:
            user = deepcopy(searchUser(nomcon, motdepassecon))
 
    chaine = user[0]
    chaine = chaine.upper()
    liste = transactionList(user[0])   
    return render_template('acceuil.html', nom_utilisateur = chaine, listes = liste)

@app.route('/operation', methods=['GET', 'POST'])
def transactionbancaire():
    global user
    
    if request.method == 'POST' and 'depot-form' in request.form:
        montant = request.form.get('valeur')
        try:
            montant = int(montant)
        except:
            return render_template('acceuil.html')
        
        if depot(montant, user[0]) == 'succes':
            print('succes')
            listes = transactionList(user[0])
            return render_template('acceuil.html', listes=listes)
        elif depot(montant, user[0]) == 'echec':
            print('echec')
            return render_template('acceuil.html')
    elif request.method == 'POST' and 'retrait-form' in request.form:
        montant = request.form.get('valeur')
        try:
            montant = int(montant)
        except:
            return render_template('acceuil.html')
        
        if retrait(montant, user[0]) == 'succes':
            print('succes')
            listes = transactionList(user[0])
            return render_template('acceuil.html', listes=listes)
        elif retrait(montant, user[0]) == 'echec':
            print('echec')
            return render_template('acceuil.html')
    elif request.method == 'POST' and 'transfert-form' in request.form:
        montant = request.form.get('valeur')
        destinataire = request.form.get('destinataire')
        try:
            montant = int(montant)
        except:
            return render_template('acceuil.html')
        if transfert(montant, user[0], destinataire) == 'succes':
            print('succes')
            listes = transactionList(user[0])
            return render_template('acceuil.html', listes=listes)
        elif retrait(montant, user[0], destinataire) == 'echec':
            print('echec')
            return render_template('acceuil.html')

user = []
        
if __name__ == '__main__':
    app.run(debug=True)