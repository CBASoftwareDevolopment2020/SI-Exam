var amqp = require('amqplib/callback_api');
var secret = require('./secret');

url = secret;
// params = pika.URLParameters(url);
// connection = pika.BlockingConnection(params);

amqp.connect(url, function (error0, connection) {
	if (error0) {
		throw error0;
	}
	connection.createChannel(function (error1, channel) {
		if (error1) {
			throw error1;
		}

		var queue = '6666-transfer';
		var msg = {
			targetAccountNumber: 2389,
			orginCardNumber: 4571666609930868,
			originCVC: 816,
			amount: 10000000000,
			targetRegNumber: 6666,
		};

		// channel.assertQueue(queue, {
		// 	durable: false,
		// });
		channel.sendToQueue(queue, Buffer.from(JSON.stringify(msg)));

		console.log(' [x] Sent %s', msg);
	});
	setTimeout(function () {
		connection.close();
		process.exit(0);
	}, 500);
});
