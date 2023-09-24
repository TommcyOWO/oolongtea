<script setup lang="ts">
import '@master/css';
import { useLocalStorage } from '@vueuse/core';

</script>
<template>
  <div class="mt:15vh flex justify-content:center w:100%">
    <div class="w:250 h:400 text:center r:10px b:3|solid|beryl-76 shadow:5|6|teal-68:hover ~300ms|ease-in">
      <h2 class="color:white@dark mt:50">登入</h2>
      <input class="w:200px h:20px m:10px b:none r:5" type="text" placeholder="text">
      <input class="w:200px h:20px m:10px b:none r:5" type="text" placeholder="text">
      <input class="w:200px h:20px m:10px b:none r:5" type="password" placeholder="password">
      <button class="w:200px h:20px m:10px b:none r:5">ddd</button>
    </div>
  </div>

</template>
<style scoped></style>