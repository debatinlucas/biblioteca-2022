import { post } from '@/helpers/http';

export function login(email, senha) {
  return post('/login', { email, senha });
}

export function registrar(usuario) {
  return post('/signup', usuario);
}
