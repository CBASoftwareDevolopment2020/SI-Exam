var amqp = require('amqplib/callback_api');

url = 'amqps://epryvnth:U21Lp1tn8pQfKtxzBS3CYmh61CJ1_jje@hawk.rmq.cloudamqp.com/epryvnth';

amqp.connect(url, function (error0, connection) {
	if (error0) {
		throw error0;
	}
	connection.createChannel(function (error1, channel) {
		if (error1) {
			throw error1;
		}

		var queue = '6666-transfer';

		console.log(' [*] Waiting for messages in %s. To exit press CTRL+C', queue);

		channel.consume(
			queue,
			function (msg) {
				console.log(' JSON?', JSON.parse(msg.content));
			},
			{
				noAck: true,
			}
		);
	});
});
