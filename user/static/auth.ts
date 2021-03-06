import type { Response, NextFunction } from 'express';
import {
  validateAuthUser,
  authUser,
} from '../service/authUser';
import type { UserSessionRequest } from './types';

export async function submitAuth(req: UserSessionRequest, res: Response, next: NextFunction) {
  const validation = validateAuthUser(req.body);
  if (validation.error) {
    res.locals.errors = validation;
    return next();
  }
  const user = await authUser(req.body);
  if (!user) {
    res.locals.errors = {
      error: true,
      password: "Invalid user/password combination",
    };
  } else {
    req.session.user = user;
  }
  return next();
}

export function viewAuth(req: UserSessionRequest, res: Response) {
  if (req.session.user) {
    // If we are logged in, we don't need to view this
    return res.redirect('/');
  }

  res.render(`${__dirname}/views/auth.twig`);
}

export function destroyAuth(req: UserSessionRequest, res: Response) {
  req.session.destroy(() => {
    return res.redirect('/');
  });
}
