<script setup lang="ts">
import '@master/css';
import axios from 'axios';
import {getCookie, setCookie} from 'typescript-cookie';
import { url } from '@/assets/conf/url';

import { ref } from 'vue'

const username = ref('')
const password = ref('')
const emits = defineEmits(['lo_c_page'])

const cpage = (page: string) => {
  emits('lo_c_page', page);
  setTimeout(() => {
    window.location.reload();
  }, 300)
}

const token = getCookie('token')
if (token !== undefined) {
  cpage('index')
}

const login = async() =>{
  const data = new URLSearchParams();
  data.append('username', username.value);
  data.append('password', password.value);

  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  };
  try {
    const response = await axios.post(url+'/logon', data, config);
    const token = response.data.access_token;
    const expirationDate = new Date();
    expirationDate.setTime(expirationDate.getTime() + 30 * 60 * 1000);
    setCookie('token', token, { expires: expirationDate });
    cpage('index')
  }catch(error){
    console.error(error)
  }
}

</script>
<template>
  <div class="mt:15vh flex justify-content:center w:100%">
    <div class="w:250 h:400 text:center r:10px b:3|solid|beryl-76 shadow:5|6|teal-68:hover ~300ms|ease-in">
      <h2 class="color:white@dark mt:30">登入</h2>
      <input v-model="username"  class="mt:30px w:200px h:25px m:10px b:none r:5" type="text" placeholder="使用者名稱">
      <input v-model="password" class="w:200px h:25px m:10px b:none r:5" type="password" placeholder="使用者密碼">
      <button @click="login()" class="w:200px h:25px m:10px b:none r:5 cursor:pointer">確定</button>
      <div class="color:white@dark text:center mt:120">
        <h3 @click="cpage('register')" class="inline-block cursor:pointer ">註冊</h3> |
        <h3 @click="cpage('reset')" class="inline-block cursor:pointer">忘記密碼</h3>
      </div>
    </div>
  </div>

</template>
<style scoped></style>