class itemsRepo {
	constructor(dao) {
		this.dao = dao;
	}
	createTable() {
		const sql = `
        CREATE TABLE IF NOT EXISTS items (
            itemId INTEGER PRIMARY KEY,
            itemName Text,
            itemDesc Text,
            price INTEGER)`;
		return this.dao.run(sql);
	}

	// itemId, itemName, itemDesc, price
	getAll() {
		return this.dao.all(`SELECT * FROM items`);
	}

	getById(id) {
		return this.dao.get(`SELECT * FROM items WHERE itemId = ?`, [id]);
	}

	delete(id) {
		return this.dao.run(`DELETE FROM items WHERE itemId = ?`, [id]);
	}

	create(id, name, desc, price) {
		return this.dao.run(
			'INSERT INTO items (itemId, itemName, itemDesc, price) VALUES (?, ?, ?, ?)',
			[id, name, desc, price]
		);
	}

	update(id, name, desc, price) {
		return this.dao.run(
			`UPDATE items
            SET itemName = ?,
                itemDesc = ?,
                price = ?
            WHERE itemId = ?`,
			[name, desc, price, id]
		);
	}
}

module.exports = itemsRepo;
