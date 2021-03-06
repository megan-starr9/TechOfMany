import type { Response, NextFunction } from 'express';
import {
  validateCreateUser,
  createUser,
} from '../service/createUser';
import type { UserSessionRequest } from './types';

export async function submitRegister(req: UserSessionRequest, res: Response, next: NextFunction) {
  const validation = validateCreateUser(req.body);
  if (validation.error) {
    res.locals.errors = validation;
    return next();
  }
  const user = await createUser(req.body);
  req.session.user = user;
  return next();
}

export function viewRegister(req: UserSessionRequest, res: Response) {
  if (req.session.user) {
    // If we are logged in, we don't need to view this
    return res.redirect('/');
  }

  res.render(`${__dirname}/views/register.twig`);
}
