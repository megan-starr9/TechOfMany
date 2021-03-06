import type { BaseSchema } from '@techofmany/storage';

export type UserSchema = BaseSchema & {
  name: string,
  email: string,
  password: string,
};

export type UserRegistration = {
  name: string,
  email: string,
  password: string,
  passwordConfirm: string,
};

export type UserAuthentication = {
  name: string,
  password: string,
};

export type Validation<T> = Partial<T> & {
  error: boolean,
};
