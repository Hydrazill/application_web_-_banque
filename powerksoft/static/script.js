
function afformconnexion() {
    document.getElementById('bouton-inscription').style.display = 'block';
    document.getElementById('forminscription').style.display = 'none';
    document.getElementById('bouton-connexion').style.display = 'none';
    document.getElementById('formconnexion').style.display = 'block';
}
function afforminscription() {
    document.getElementById('bouton-inscription').style.display = 'none';
    document.getElementById('forminscription').style.display = 'block';
    document.getElementById('bouton-connexion').style.display = 'block';
    document.getElementById('formconnexion').style.display = 'none';
}

let currentuser = null;
let balance = 0;
let transactions = [];

function deposer() {
    document.getElementById('sideright').style.display = 'block';
    document.getElementById('valeur').style.display = 'block';
    document.getElementById('bdepot').style.display = 'block';
    document.getElementById('bretrait').style.display = 'none';
    document.getElementById('destinataire').style.display = 'none';
    document.getElementById('btransfert').style.display = 'none';
}
function retirer() {
    document.getElementById('sideright').style.display = 'block';
    document.getElementById('valeur').style.display = 'block';
    document.getElementById('bdepot').style.display = 'none';
    document.getElementById('bretrait').style.display = 'block';
    document.getElementById('destinataire').style.display = 'none';
    document.getElementById('btransfert').style.display = 'none';
}
function transferer() {
    document.getElementById('sideright').style.display = 'block';
    document.getElementById('valeur').style.display = 'block';
    document.getElementById('bdepot').style.display = 'none';
    document.getElementById('bretrait').style.display = 'none';
    document.getElementById('destinataire').style.display = 'block';
    document.getElementById('btransfert').style.display = 'block';
}

function deposit() {
	const amount = document.getElementById('valeur').value;
	if(!isNaN(amount) && amount > 0) {
		balance += amount;
		transactions.push("Depot de " + amount + "FCFA");
		updateTransactionList();
	}else {
		alert("Montant invalide");
	}
}
function updateTransactionList() {
	const transactionList = document.getElementById('transaction-list');
	transactionList.innerHTML = "";
	for(const transaction of transactions) {
		const li = document.createElement("li");
		li.textContent = transaction;
		transactionList.append(li);
	}
	document.getElementById('transaction').style.display = "block";
}