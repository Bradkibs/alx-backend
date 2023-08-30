import { createClient } from 'redis';
const redis = require('redis');
import { promisify } from 'util';
const client = createClient({
host: 'localhost',
port: 6379,
});
const modGet = promisify(client.get).bind(client);
function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}
async function displaySchoolValue(schoolName) {
	try {
		const schoolVal = await modGet(schoolName);
		console.log(schoolVal);
	}
	catch (error) {
		console.error(error);
	}
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
