<template>
  <el-tabs v-model="tabActive" @tab-click="fetch">
    <el-tab-pane label="Últimos Empréstimos" name="emprestimos">
      <div>
        <biblioteca-p class="opacity--50 my--md">( Sem empréstimos )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="Últimos livros" name="livros">
      <div>
        <biblioteca-p class="opacity--50 my--md">( Sem livros )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="Últimos usuários" name="usuarios">
      <div v-if="usuarioList.length">
        <div
          v-for="usuario in usuarioList"
          :key="usuario.id"
          class="mb--xl">
          <biblioteca-usuario-card :usuario="usuario" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem usuários )</biblioteca-p>
      </div>
    </el-tab-pane>
  </el-tabs>
</template>

<script>
import { fetchUsuarios } from '@/modules/usuario/usuario.service';

import BibliotecaUsuarioCard from '@/modules/usuario/components/UsuarioCard.vue';

export default {
  name: 'BibliotecaHomeTabs',
  components: {
    BibliotecaUsuarioCard,
  },
  data() {
    return {
      tabActive: 'emprestimos',
      usuarioList: [],
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    fetch() {
      if (this.tabActive === 'emprestimos') {
        this.fetchEmprestimos();
      } else if (this.tabActive === 'livros') {
        this.fetchLivros();
      } else if (this.tabActive === 'usuarios') {
        this.fetchUsuarios();
      }
    },
    fetchLivros() {
    },
    fetchUsuarios() {
      fetchUsuarios()
        .then(({ data }) => {
          this.usuarioList = data.data;
        })
        .catch(() => {
          this.usuarioList = [];
        });
    },
    fetchEmprestimos() {
    },
  },
};
</script>
