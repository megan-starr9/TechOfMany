import type { Request } from 'express';
import type { Session } from 'express-session';
import type { UserSchema } from '../service/types';

export type UserSessionRequest = Request & {
  session: Session & {
      user?: UserSchema,
  },
};
