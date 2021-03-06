import type { Request, Response } from 'express';
import {
  validateCreateUser,
  createUser,
} from '../service/createUser';

export default async function register(req: Request, res: Response) {
  const validation = validateCreateUser(req.body);
  if (validation.error) {
    return res.status(400).json(validation);
  }
  const user = await createUser(req.body);
  return res.status(200).json(user);
}
