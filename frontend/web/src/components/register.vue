<script setup lang="ts">
import '@master/css';
import axios from 'axios';
import { url } from '@/assets/conf/url';

import { ref } from 'vue'
import { getCookie } from 'typescript-cookie';

let error_content: any = ref('')
const email = ref('')
const username = ref('')
const password = ref('')
const emits = defineEmits(['reg_c_page'])

const cpage = (page: string) => {
  emits('reg_c_page', page);
}

const token = getCookie('token')
if (token !== undefined) {
  cpage('index')
}

const register = async () => {
  const userData = {
    username: username.value,
    email: email.value,
    password: password.value
  };
  try {
    await axios.post(url + '/register', userData);
    cpage('logon')
  } catch (error:any) {
    if (error.code === 'ERR_BAD_REQUEST'){
      error_content.value = '已經註冊過了'
    }
  }
}

</script>
<template>
  <div class="mt:15vh flex justify-content:center w:100%">
    <div class="w:250 h:400 text:center r:10px b:3|solid|beryl-76 shadow:5|6|teal-68:hover ~300ms|ease-in">
      <h2 class="color:white@dark mt:30">註冊</h2>
      <input v-model="email" class="mt:30px w:200px h:25px m:10px b:none r:5" type="email" placeholder="電子郵件">
      <input v-model="username" class="w:200px h:25px m:10px b:none r:5" type="text" placeholder="使用者名稱">
      <input v-model="password" class="w:200px h:25px m:10px b:none r:5" type="password" placeholder="使用者密碼">
      <button @click="register()" class="w:200px h:25px m:10px b:none r:5 cursor:pointer">確定</button>
      <div class="color:white@dark text:center mt:75">
        <h3 @click="cpage('logon')" class="inline-block cursor:pointer ">登入</h3> |
        <h3 @click="cpage('reset')" class="inline-block cursor:pointer">忘記密碼</h3>
      </div>
      <a class="f:semibold block color:red mt:5px">{{ error_content }}</a>
    </div>
  </div>
</template>
<style scoped></style>@/url@/assets/url