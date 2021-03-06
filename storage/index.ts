import type { ObjectId } from 'mongodb';
import {
  connect as connectDB,
  disconnect,
  insert,
  update,
  remove,
  find,
  findPage,
  addIndex,
} from './store';

export async function connect(): Promise<void> {
  await connectDB();

  // disconnect if node exits
  process.on('SIGINT', async () => {
    await disconnect();
    process.exit(0);
  });
}

export {
  insert,
  update,
  remove,
  find,
  findPage,
  addIndex,
};

export type BaseSchema = {
  _id: ObjectId,
};
