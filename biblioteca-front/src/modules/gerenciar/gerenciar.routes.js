import { GERENCIAR_URL } from '@/modules/gerenciar/gerenciar.constants';

export default [
  {
    ...GERENCIAR_URL.usuarios,
    component: () => import('@/modules/gerenciar/views/GerenciarUsuarios.vue'),
  },
];

export function goToUsuarios($router) {
  $router.push({
    name: GERENCIAR_URL.usuarios.name,
  });
}
