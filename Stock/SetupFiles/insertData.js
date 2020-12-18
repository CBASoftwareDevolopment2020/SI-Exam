const AppDAO = require('../dao');
const itemsRepo = require('../items');
const fs = require('fs');

const dao = new AppDAO('./db/stock');
const items = new itemsRepo(dao);

items.createTable();

fs.readFile('SetupFiles/data.json', 'utf8', (err, jsonString) => {
	if (err) {
		console.log('File read failed:', err);
		return;
	}
	JSON.parse(jsonString).forEach((item) => {
		console.log(item);
		items.create(item.itemID, item.itemName, item.itemDesc, item.price);
	});
});
