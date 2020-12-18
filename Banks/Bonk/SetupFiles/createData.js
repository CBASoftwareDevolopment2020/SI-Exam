var fs = require('fs');

function genAn() {
	return parseInt(Math.random() * 8999 + 1000);
}

function genCn() {
	return parseInt(4571666600000000 + Math.random() * 99999999);
}

function genCvc() {
	return parseInt(Math.random() * 899 + 100);
}

function genBal() {
	return parseInt(Math.random() * 10000000);
}

let accs = [];

for (let i = 0; i < 10; i++) {
	accs[i] = { aN: genAn(), cN: genCn(), cvc: genCvc(), bal: genBal() };
}

fs.writeFile('SetupFiles/data.json', JSON.stringify(accs), function (err) {
	if (err) throw err;
	console.log('Saved!');
});
