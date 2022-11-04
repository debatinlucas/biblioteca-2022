export const USUARIOS_URL = Object.freeze({
  path: '/usuarios',
  view: {
    name: 'usuario.view',
    path: '/usuarios/ver/:id',
  },
  edit: {
    name: 'usuario.edit',
    path: '/usuarios/editar/:id',
  },
  create: {
    name: 'usuario.create',
    path: '/usuarios/criar',
  },
  notfound: {
    name: 'usuario.notfound',
    path: '/usuarios/nao-encontrado',
  },
});

export const USUARIO_ERRORS = {
  404: 'USUARIO_NOT_FOUND',
  401: 'PERMISSION_DENIED',
};
