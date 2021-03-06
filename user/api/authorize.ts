import type { Request, Response } from 'express';
import {
  validateAuthUser,
  authUser,
} from '../service/authUser';

export default async function authorize(req: Request, res: Response) {
  const validation = validateAuthUser(req.body);
  if (validation.error) {
    return res.status(400).json(validation);
  }
  const user = await authUser(req.body);
  if (!user) {
    return res.status(400).json({
      error: true,
      password: "Invalid user/password combination",
    });
  }
  return res.status(200).json(user);
}
