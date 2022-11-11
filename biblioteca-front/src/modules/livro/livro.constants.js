export const LIVROS_URL = Object.freeze({
  path: '/livros',
  view: {
    name: 'livro.view',
    path: '/livros/ver/:id',
  },
  edit: {
    name: 'livro.edit',
    path: '/livros/editar/:id',
  },
  create: {
    name: 'livro.create',
    path: '/livros/criar',
  },
  notfound: {
    name: 'livro.notfound',
    path: '/livros/nao-encontrado',
  },
});

export const LIVRO_ERRORS = {
  404: 'LIVRO_NOT_FOUND',
  401: 'PERMISSION_DENIED',
};
