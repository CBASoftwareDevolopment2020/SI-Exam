var express = require('express');
var app = express();
const AppDAO = require('./dao');
const itemsRepo = require('./items');

const dao = new AppDAO('./db/stock');
const items = new itemsRepo(dao);

app.route('/items').get((req, res) => {
	items.getAll().then((items) => res.json(items));
});

//GetItem(itemId)
app.route('/item/:id').get((req, res) => {
	items.getById(parseInt(req.params.id)).then((item) => res.json(item));
});

// RemoveItem(itemId)
app.route('/item/:id').delete((req, res) => {
	items.delete(parseInt(req.params.id)).then(res.json('item ' + req.params.id + ' is delete'));
});

// AddItem(itemName, itemDesc, price)
app.route('/item/:id/:name/:desc/:price').post((req, res) => {
	items
		.create(req.params.id, req.params.name, req.params.desc, req.params.price)
		.then((item) => res.json(item));
});

// UpdateItem(itemId, itemName, itemDesc, price)
app.route('/item/:id/:name/:desc/:price').put((req, res) => {
	items
		.update(req.params.id, req.params.name, req.params.desc, req.params.price)
		.then((item) => res.json(item));
});

app.listen(3000, () => {
	console.log('Server running on port 3000');
});
