var amqp = require('amqplib/callback_api');
const AppDAO = require('./dao');
const accountsRepo = require('./accounts');
const dao = new AppDAO('./db/bonk');
const accounts = new accountsRepo(dao);

url = 'amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth';

amqp.connect(url, function (error0, connection) {
	if (error0) {
		throw error0;
	}
	consumeUpdate(connection);
	consumeTransfer(connection);
});

function consumeTransfer(connection) {
	connection.createChannel(function (error1, channel) {
		if (error1) {
			throw error1;
		}

		var queue = '6666-transfer';

		channel.consume(
			queue,
			function (msg) {
				msg = JSON.parse(msg.content);
				accounts.getByCnCvc(msg.orginCardNumber, msg.originCVC).then((acc) => {
					accounts.update(acc.accountNumber, -msg.amount);
					newMsg = {
						accountNumber: msg.targetAccountNumber,
						amount: msg.amount,
						sourceAccountNumber: acc.accountNumber,
						sourceRegNumber: 6666,
					};
					channel.sendToQueue(
						msg.targetRegNumber + '-update',
						Buffer.from(JSON.stringify(newMsg))
					);
				});
			},
			{
				noAck: true,
			}
		);
	});
}

function consumeUpdate(connection) {
	connection.createChannel(function (error1, channel) {
		if (error1) {
			throw error1;
		}

		var queue = '6666-update';

		channel.consume(
			queue,
			function (msg) {
				msg = JSON.parse(msg.content);
				accounts.update(parseInt(msg.accountNumber), parseInt(msg.amount));
			},
			{
				noAck: true,
			}
		);
	});
}

// {
//     "accountNumber": 2233,
//     "cardNumber": 4571888888812408,
//     "cvc": 395,
//     "balance": 237864
//   }
