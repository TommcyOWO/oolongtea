<script setup lang="ts">
import '@master/css';
import axios from 'axios';

const login = async() =>{

}

import { defineEmits } from 'vue'

const emits = defineEmits(['c_page'])

const cpage = () => {
  emits('c_page', 'register');
}

</script>
<template>
  <div class="mt:15vh flex justify-content:center w:100%">
    <div class="w:250 h:400 text:center r:10px b:3|solid|beryl-76 shadow:5|6|teal-68:hover ~300ms|ease-in">
      <h2 class="color:white@dark mt:50">登入</h2>
      <input class="mt:50px w:200px h:20px m:10px b:none r:5" type="text" placeholder="使用者名稱">
      <input class="w:200px h:20px m:10px b:none r:5" type="password" placeholder="使用者密碼">
      <button class="w:200px h:20px m:10px b:none r:5 cursor:pointer">確定</button>
    
      <h3 @click="cpage()" class="color:white@dark text:center mt:100 cursor:pointer">註冊</h3>
    </div>
  </div>

</template>
<style scoped></style>