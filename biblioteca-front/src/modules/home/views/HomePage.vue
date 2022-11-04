<template>
  <biblioteca-single-content-layout container-size="lg">
    <template #content>
      <biblioteca-home-tabs />
    </template>
  </biblioteca-single-content-layout>
</template>

<script>
import BibliotecaSingleContentLayout from '@/layouts/SingleContentLayout.vue';
import * as authStore from '@/modules/auth/auth.store';
import { goToLoginPage } from '@/router/route.service';
import BibliotecaHomeTabs from '@/modules/home/components/HomeTabs.vue';

export default {
  name: 'BibliotecaHomeLayout',
  components: {
    BibliotecaSingleContentLayout,
    BibliotecaHomeTabs,
  },
  beforeCreate() {
    if (!authStore.getters.getToken()) {
      goToLoginPage();
    }
  },
};
</script>
