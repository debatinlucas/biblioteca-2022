import authRoutes from '@/modules/auth/auth.routes';
import homeRoutes from '@/modules/home/home.routes';
import usuarioRoutes from '@/modules/usuario/usuario.routes';
import livroRoutes from '@/modules/livro/livro.routes';
import emprestimoRoutes from '@/modules/emprestimo/emprestimo.routes';
import gerenciarRoutes from '@/modules/gerenciar/gerenciar.routes';
import errorRoutes from '@/modules/error/error.routes';

const routes = [
  {
    path: '*',
    redirect: '/',
  },
];

// ... representa que serão obtidos todos os dados dos arquivos de rotas e empilhá-los em uma única lista
export default [
  ...routes,
  ...homeRoutes,
  ...authRoutes,
  ...usuarioRoutes,
  ...emprestimoRoutes,
  ...livroRoutes,
  ...gerenciarRoutes,
  ...errorRoutes,
];
