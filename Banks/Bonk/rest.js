var express = require('express');
var app = express();
const AppDAO = require('./dao');
const accountsRepo = require('./accounts');

const dao = new AppDAO('./db/bonk');
const accounts = new accountsRepo(dao);

app.route('/accounts').get((req, res) => {
	accounts.getAll().then((accs) => res.json(accs));
});

app.route('/validate/account/:aN').get((req, res) => {
	accounts.getByAn(parseInt(req.params.aN)).then((acc) => res.json(acc));
});

app.route('/validate/card/:cN/:cvc').get((req, res) => {
	accounts
		.getByCnCvc(parseInt(req.params.cN), parseInt(req.params.cvc))
		.then((acc) => res.json(acc.accountNumber));
});

app.route('/update/:aN/:amount/:source').get((req, res) => {
	accounts
		.update(parseInt(req.params.aN), parseInt(req.params.amount))
		.then((acc) => res.json(acc != null));
});

app.listen(3000, () => {
	console.log('Server running on port 3000');
});
