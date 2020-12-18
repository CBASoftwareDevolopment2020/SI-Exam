class accountsRepo {
	constructor(dao) {
		this.dao = dao;
	}

	createTable() {
		const sql = `
        CREATE TABLE IF NOT EXISTS accounts (
        accountNumber INTEGER PRIMARY KEY,
        cardNumber INTEGER,
        cvc INTEGER,
        balance INTEGER)`;
		return this.dao.run(sql);
	}

	create(aN, cN, cvc, bal) {
		return this.dao.run(
			'INSERT INTO accounts (accountNumber, cardNumber, cvc, balance) VALUES (?, ?, ?, ?)',
			[aN, cN, cvc, bal]
		);
	}

	update(aN, bal) {
		return this.dao.run(
			`UPDATE accounts
            SET balance = balance + ?
            WHERE accountNumber = ?`,
			[bal, aN]
		);
	}

	delete(id) {
		return this.dao.run(`DELETE FROM accounts WHERE id = ?`, [id]);
	}

	getByAn(aN) {
		return this.dao.get(`SELECT * FROM accounts WHERE accountNumber = ?`, [aN]);
	}

	getByCnCvc(cN, cvc) {
		return this.dao.get(`SELECT * FROM accounts WHERE cardNumber = ? AND cvc = ?`, [cN, cvc]);
	}

	getAll() {
		return this.dao.all(`SELECT * FROM accounts`);
	}
}

module.exports = accountsRepo;
