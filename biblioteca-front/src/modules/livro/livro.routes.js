import { LIVROS_URL } from '@/modules/livro/livro.constants';
import { createEmptyComponent } from '@/router/route.service';

export default [
  {
    path: LIVROS_URL.path,
    redirect: '/',
    component: { render: createEmptyComponent },
    children: [
      {
        ...LIVROS_URL.view,
        component: () => import('@/modules/livro/views/LivroViewPage.vue'),
      },
      {
        ...LIVROS_URL.edit,
        component: () => import('@/modules/livro/views/LivroEditPage.vue'),
      },
      {
        ...LIVROS_URL.create,
        component: () => import('@/modules/livro/views/LivroEditPage.vue'),
      },
      {
        ...LIVROS_URL.notfound,
        component: () => import('@/modules/livro/views/LivroNotFound.vue'),
      },
    ],
  },
];

export function goToLivroNotFound($router) {
  $router.push({
    name: LIVROS_URL.notfound.name,
  });
}

export function goToOpenLivro($router, livro) {
  $router.push({
    name: LIVROS_URL.view.name,
    params: { id: livro.id },
  });
}

export function goToCreateLivro($router) {
  $router.push({
    name: LIVROS_URL.create.name,
  });
}
