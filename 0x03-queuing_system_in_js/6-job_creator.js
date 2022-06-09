import { createQueue } from 'kue';

const queue = createQueue();

const sampleData = {
  phoneNumber: '0911223344',
  message: 'This is a sample message'
}

const job = queue.create('push_notification_code', sampleData)
            .save(function(err){
                if (!err) console.log(`Notification job created: ${job.id}`);
            });

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
