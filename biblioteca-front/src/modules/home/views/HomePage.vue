<template>
  <biblioteca-single-content-layout container-size="lg">
    <template #content>
      <h1>Logado</h1>
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';
import * as authStore from '@/modules/auth/auth.store';
import { goToLoginPage } from '@/router/route.service';

export default {
  name: 'BibliotecaHomeLayout',
  components: {
    BibliotecaSingleContentLayout,
  },
  beforeCreate() {
    if (!authStore.getters.getToken()) {
      goToLoginPage();
    }
  },
};
</script>
