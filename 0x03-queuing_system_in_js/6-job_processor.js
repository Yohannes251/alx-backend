import { createQueue } from 'kue';

const queue = createQueue();

const sampleData = {
  phoneNumber: '0911223344',
  message: 'Sample message'
}

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});
