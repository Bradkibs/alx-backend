const kue = require('kue');
const jobData = {
  phoneNumber: '+1234567890',
  message: 'Hello, this is a test message.'
};
const queue = kue.createQueue();
const job = queue.create('push_notification_code', jobData).save(err=> {
	if (!err) {
		console.log(`Notification job created: ${job.id}`);
	}
});
job.on('complete', () => {
	console.log('Notification job completed');
});
job.on('error', () => {
	console.log('Notification job failed');
});
