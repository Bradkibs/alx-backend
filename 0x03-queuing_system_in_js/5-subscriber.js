import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();

const subscriber = client.duplicate();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

subscriber.subscribe('holberton school channel');
subscriber.on('message', (channel, message) => {
	if (message === 'KILL_SERVER') {
		console.log(message);
		subscriber.unsubscribe();
		subscriber.quit();
		process.exit();
	}
	else {
	console.log(message);
	}
});
