<template>
  <el-tabs v-model="tabActive" @tab-click="fetch">
    <el-tab-pane label="Últimos Empréstimos" name="emprestimos">
      <div v-if="emprestimoList.length">
        <div
          v-for="emprestimo in emprestimoList"
          :key="emprestimo.id"
          class="mb--xl">
          <biblioteca-emprestimo-card :emprestimo="emprestimo" />
        </div>
      </div>
      <div v-else>
        <biblioteca-p class="opacity--50 my--md">( Sem empréstimos )</biblioteca-p>
      </div>
    </el-tab-pane>
    <el-tab-pane label="Últimos livros" name="livros">
      <div v-if="livroList.length">
        <div
          v-for="livro in livroList"
          :key="livro.id"
          class="mb--xl">
          <biblioteca-livro-card :livro="livro" />
        </div>
      </div>
      <div v-else>
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
import { fetchLivros } from '@/modules/livro/livro.service';
import { fetchEmprestimos } from '@/modules/emprestimo/emprestimo.service';

import BibliotecaUsuarioCard from '@/modules/usuario/components/UsuarioCard.vue';
import BibliotecaLivroCard from '@/modules/livro/components/LivroCard.vue';
import BibliotecaEmprestimoCard from '@/modules/emprestimo/components/EmprestimoCard.vue';

export default {
  name: 'BibliotecaHomeTabs',
  components: {
    BibliotecaUsuarioCard,
    BibliotecaLivroCard,
    BibliotecaEmprestimoCard,
  },
  data() {
    return {
      tabActive: 'emprestimos',
      usuarioList: [],
      livroList: [],
      emprestimoList: [],
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
      fetchLivros()
        .then(({ data }) => {
          this.livroList = data.data;
        })
        .catch(() => {
          this.livroList = [];
        });
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
      fetchEmprestimos()
        .then(({ data }) => {
          this.emprestimoList = data.data;
        })
        .catch(() => {
          this.emprestimoList = [];
        });
    },
  },
};
</script>
