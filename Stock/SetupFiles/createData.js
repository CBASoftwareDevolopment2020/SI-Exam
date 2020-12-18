var fs = require('fs');

// itemId, itemName, itemDesc, price

let items = [
	{
		itemId: 0,
		itemName: 'Egg',
		itemDesc: 'round strong and dont need no chicken',
		price: 5,
	},
	{
		itemId: 1,
		itemName: 'Apple',
		itemDesc: 'the best design, we know you want it',
		price: 999,
	},
	{
		itemId: 2,
		itemName: 'Onion',
		itemDesc: 'onion is onion in onion in onion',
		price: 13,
	},
	{
		itemId: 3,
		itemName: 'Milk',
		itemDesc: 'gotta drink your milk',
		price: 22,
	},
	{
		itemId: 4,
		itemName: 'Joice',
		itemDesc: 'get the JUICE',
		price: 17,
	},
];

fs.writeFile('SetupFiles/data.json', JSON.stringify(items), function (err) {
	if (err) throw err;
	console.log('Saved!');
});
