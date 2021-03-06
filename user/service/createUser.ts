import { hash } from 'bcrypt';
import { insert } from '@techofmany/storage';
import type {
  UserSchema,
  UserRegistration,
  Validation,
} from './types';

export function validateCreateUser(registration: UserRegistration): Validation<UserRegistration> {
  const result = { error: false } as any;
  if (!registration.name) {
    result.error = true;
    result.name = "Name is required.";
  }
  if (!registration.email) {
    result.error = true;
    result.name = "Email is required.";
  }
  if (!registration.password) {
    result.error = true;
    result.password = "Password is required.";
  } else if (registration.password !== registration.passwordConfirm) {
    result.error = true;
    result.password = "Password and confirmation must match.";
  }
  return result;
}

export async function createUser(registration: UserRegistration): Promise<UserSchema> {
  const encryptedPass = await hash(registration.password, 10);

  const users = await insert<UserSchema>('users', {
    name: registration.name,
    email: registration.email,
    password: encryptedPass,
  });
  return users[0];
}
