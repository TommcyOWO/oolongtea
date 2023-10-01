<script setup lang="ts">
import { IconBlur,IconMenu2 } from '@tabler/icons-vue';
import '@master/css';
import { useDark, useToggle, useLocalStorage } from '@vueuse/core';
import { getCookie, removeCookie } from 'typescript-cookie';
import { ref } from 'vue';

import user_page from '@/components/user_page.vue'
import index from '@/components/index.vue';
import logon from '@/components/logon.vue';
import register from '@/components/register.vue';
import reset from '@/components/reset.vue';

const token = ref(getCookie('token'))

const dark = useDark({
  valueDark: 'dark',
  valueLight: 'light',
});
const toggle = useToggle(dark);

const page = useLocalStorage('page', 'index');

const cEvent = (data: string) => {  
  page.value = data;
}

const singout = () => {
  removeCookie('token')
  token.value = 'null';
  console.log(token.value)
  cEvent('logon')
}

</script>
<template>
  <div class="flex jc:space-between ai:center color:white@dark mt:20px p:10px f:20 f:semibold">
      <IconMenu2 class="hide@>md mx:20px"/>
          <ul class="lt:none hide@<md flex ai:center mx:20px">
              <li @click="page = 'index'" class="cursor:pointer inline ml:5px">
                <img src="@/assets/icon.png" class="h:50 w:50 float:left">
              <a class="rel top:12px">Healthyble</a><a class="rel top:12px color:beryl-76">健康寶</a></li>
              <li v-if="token" @click="page = 'user_page'" class="cursor:pointer inline mx:20px">使用者頁面</li>
          </ul>
          <div class="rel flex right:35px text:center">
              <a v-if="token" @click="singout()" :key="token" class="cursor:pointer mx:30px">登出</a>
              <a v-else @click="page = 'logon'" class="cursor:pointer mx:30px">登入</a>
            <IconBlur class="cursor:pointer" @click="toggle()"/>
          </div>
  </div>
  <Transition name="Transition" mode="out-in">
      <div v-if="page === 'user_page'">
      <user_page/>
      </div>
      <div v-else-if="page === 'index'">
        <index @i_c_page="cEvent"/>
      </div>
      <div v-else-if="page === 'logon'">
        <logon @lo_c_page="cEvent"/>
      </div>
      <div v-else-if="page === 'register'">
        <register @reg_c_page="cEvent"/>
      </div>
      <div v-else-if="page === 'reset'">
        <reset @res_c_page="cEvent"/>
      </div>
  </Transition>
</template>
<style scoped>
.Transition-enter-active {
  transition: all 0.4s ease-out;
}

.Transition-leave-active {
  transition: all 0.6s cubic-bezier(1, 0.5, 0.8, 1);
}

.Transition-enter-from,
.Transition-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
</style>