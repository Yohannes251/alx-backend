import redis from 'redis';
import { createClient } from 'redis';

const util = require('util');

const client = createClient();

const clientGet = util.promisify(client.get).bind(client);

client.on('error', (err) => console.log('Redis client not connected to the server: ' + err));
client.on('ready', () => console.log('Redis client connected to the server'));

const values = {'Portland': 50,
                'Seattle': 80,
                'New York': 20,
                'Bogota': 20,
                'Cali': 40,
                'Paris': 2 }

for (const [key, value] of Object.entries(values)) {
  client.hset('HolbertonSchools', key, value, (error, reply) =>
    redis.print((`Reply: ${reply}`))
  );
}

client.hgetall('HolbertonSchools', (error, hash) => console.log(hash));
