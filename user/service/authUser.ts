import { compare } from 'bcrypt';
import { find } from '@techofmany/storage';
import type {
  UserSchema,
  UserAuthentication,
  Validation,
} from './types';

export function validateAuthUser(auth: UserAuthentication): Validation<UserAuthentication> {
  const result = { error: false } as any;
  if (!auth.name) {
    result.error = true;
    result.name = "Name is required.";
  }
  if (!auth.password) {
    result.error = true;
    result.password = "Password is required.";
  }
  return result;
}

export async function authUser(auth: UserAuthentication): Promise<UserSchema | false> {
  const users = await find<UserSchema>('users', { name: auth.name });
  if (users && users.length > 0) {
    const validPass = await compare(auth.password, users[0].password);
    if (validPass) {
      return users[0];
    }
  }
  return false;
}
