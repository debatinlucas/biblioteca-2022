<template>
  <biblioteca-navbar>
    <template #right>
      <div class="d-flex align-items--center">
        <biblioteca-button @click="onLivros">
          Livros
        </biblioteca-button>
        <biblioteca-button @click="onEmprestimos">
          Empréstimos
        </biblioteca-button>
        <biblioteca-button @click="onUsuarios">
          Usuários
        </biblioteca-button>
        <biblioteca-button @click="onLogout">
          Sair
        </biblioteca-button>
      </div>
    </template>
  </biblioteca-navbar>
</template>

<script>
import { removeCookie } from '@/helpers/cookies/cookie';
import { goToLoginPage } from '@/router/route.service';
import { goToLivros, goToEmprestimos, goToUsuarios } from '@/modules/gerenciar/gerenciar.routes';

export default {
  name: 'BibliotecaTopbar',
  data() {
    return {
    };
  },
  methods: {
    removeCookie,
    onLogout() {
      removeCookie('session_id');
      goToLoginPage();
    },
    onLivros() {
      goToLivros(this.$router);
    },
    onEmprestimos() {
      goToEmprestimos(this.$router);
    },
    onUsuarios() {
      goToUsuarios(this.$router);
    },
  },
};
</script>
