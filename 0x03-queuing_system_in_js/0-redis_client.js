import { createClient } from 'redis';
const client = createClient({
host: 'localhost',
port: 6379,
});

client.ping((error, result) => {
	if (error) {
		console.log(`Redis client not connected to the server: ${error}`);
	}
	else if (result === 'PONG') {
		console.log("Redis client connected to the server");
	}
});
client.quit();
