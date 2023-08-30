import { createClient } from 'redis';
const redis = require('redis');
const client = createClient({
host: 'localhost',
port: 6379,
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}
function displaySchoolValue(schoolName) {
	client.get(schoolName, (err, val) => {
		if (err) {
			console.log(err);
		}
		console.log(val);
	});
}
client.on('error', (error) => {
		console.log(`Redis client not connected to the server: ${error}`);
	});
client.on('connect', () => {
	console.log("Redis client connected to the server");
});
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
client.quit();
