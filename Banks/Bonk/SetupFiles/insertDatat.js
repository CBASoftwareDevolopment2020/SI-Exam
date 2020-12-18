//https://stackabuse.com/a-sqlite-tutorial-with-node-js/

const Promise = require('bluebird');
const AppDAO = require('../dao');
const accountsRepo = require('../accounts');
const fs = require('fs');

async function main() {
	const dao = new AppDAO('./db/bonk');
	const accounts = new accountsRepo(dao);
	let newAccs = [];
	// await accounts.create(12322222321, 122343466664321, 8818, 10);
	// await accounts.getByAn(123321).then((acc) => console.log("by aN:", acc));
	// await accounts.getByCnCvc(123466664321, 888).then((acc) => console.log(acc));
	// await accounts.update(123321, 100).then((acc) => console.log(acc));
	accounts.createTable();

	fs.readFile('SetupFiles/data.json', 'utf8', (err, jsonString) => {
		if (err) {
			console.log('File read failed:', err);
			return;
		}
		newAccs = JSON.parse(jsonString);
		newAccs.forEach((acc) => {
			console.log(acc);
			accounts.create(acc.aN, acc.cN, acc.cvc, acc.bal);
		});
	});

	// await accounts.getAll().then((accs) => console.log(accs));

	// projectRepo
	// 	.createTable()
	// 	.then(() => taskRepo.createTable())
	// 	.then(() => projectRepo.create(blogProjectData.name))
	// 	.then((data) => {
	// 		projectId = data.id;
	// 		const tasks = [
	// 			{
	// 				name: 'Outline',
	// 				description: 'High level overview of sections',
	// 				isComplete: 1,
	// 				projectId,
	// 			},
	// 			{
	// 				name: 'Write',
	// 				description: 'Write article contents and code examples',
	// 				isComplete: 0,
	// 				projectId,
	// 			},
	// 		];
	// 		return Promise.all(
	// 			tasks.map((task) => {
	// 				const { name, description, isComplete, projectId } = task;
	// 				return taskRepo.create(name, description, isComplete, projectId);
	// 			})
	// 		);
	// 	})
	// 	.then(() => projectRepo.getById(projectId))
	// 	.then((project) => {
	// 		console.log(`\nRetreived project from database`);
	// 		console.log(`project id = ${project.id}`);
	// 		console.log(`project name = ${project.name}`);
	// 		return projectRepo.getTasks(project.id);
	// 	})
	// 	.then((tasks) => {
	// 		console.log('\nRetrieved project tasks from database');
	// 		return new Promise((resolve, reject) => {
	// 			tasks.forEach((task) => {
	// 				console.log(`task id = ${task.id}`);
	// 				console.log(`task name = ${task.name}`);
	// 				console.log(`task description = ${task.description}`);
	// 				console.log(`task isComplete = ${task.isComplete}`);
	// 				console.log(`task projectId = ${task.projectId}`);
	// 			});
	// 		});
	// 		resolve('success');
	// 	})
	// 	.catch((err) => {
	// 		console.log('Error: ');
	// 		console.log(JSON.stringify(err));
	// 	});
}

main();
