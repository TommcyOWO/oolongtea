<script setup lang="ts">
import '@master/css';
import { defineEmits } from 'vue';

const emits = defineEmits(['i_c_page'])

const cpage = (page: string) => {
  emits('i_c_page', page);
}

</script>
<template>

<div class="rel inline-block top:100 left:100px f:25">
  <h1 class="inline color:white@dark color:black@light">HEALTHYBLE</h1>
  <h1 class="inline color:beryl-76">健康寶</h1>
  <div class="rel bg:beryl-76 h:20px w:225px bottom:20px z-index:-1"/>
    <button @click="cpage('login')" class="color:white cursor:pointer f:18 f:semibold h:50px w:120 mr:10px b:none bg:beryl-76"><b>登入</b></button>
    <button @click="cpage('register')" class=" cursor:pointer f:18 f:semibold h:50px w:120 b:4|solid|white@dark b:4|solid|black@light color:white@dark bg:none">註冊</button>
  </div>
  <div class="rel float:right top:450 h:30 w:60% bg:beryl-76"></div>

</template>
<style scoped>
</style>