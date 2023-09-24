<script setup lang="ts">
import { IconBlur } from '@tabler/icons-vue';
import '@master/css';
import { useDark, useToggle, useLocalStorage } from '@vueuse/core/index.cjs';
import { ref } from 'vue';

import introduce from '@/components/introduce.vue';
import index from '@/components/index.vue';
import login from '@/components/login.vue';
import register from '@/components/register.vue';
import reset from './components/reset.vue';

const dark = useDark({
  valueDark: 'dark',
  valueLight: 'light',
});
const toggle = useToggle(dark);

const page = useLocalStorage('page', '');

const cEvent = (data: string) => {
  page.value = data;
}

</script>
<template>
  <nav class="m:30px f:20 color:white@dark">
    <div class="flex ai:center">
    <!-- <div v-if="page === 'rea'"> -->
      <span @click="page = 'index'" class="cursor:pointer ~300ms|ease-in mx:15px">
        <img class="top:20px z:2 h:50px w:50px" src="@/assets/icon.png">
        <a class="rel bottom:15px ml:10px">Healthyble </a><a class="rel bottom:15px color:beryl-76">健康寶</a></span>
      <span @click="page = 'introduce'" class="cursor:pointer ~300ms|ease-in mx:15px" >使用者頁面</span>
      <!-- </div> -->
    </div>
      <IconBlur @click="toggle()" class="rel bottom:40 ml:20px cursor:pointer float:right color:white@dark color:black@light"/>
      <!-- <span @click="page = 'singout'" class="cursor:pointer float:right ~300ms|ease-in" >登出</span> -->
      <span v-if="page !== 'rea'" @click="page = 'login'" class="rel bottom:40 float:right cursor:pointer ~300ms|ease-in" >登入</span>
  </nav>
  <Transition name="Transition" mode="out-in">
    <div v-if="page === 'introduce'">
    <introduce @c_page="cEvent"/>
    </div>
    <div v-else-if="page === 'index'">
      <index @c_page="cEvent"/>
    </div>
    <div v-else-if="page === 'login'">
      <login @c_page="cEvent"/>
    </div>
    <div v-else-if="page === 'register'">
      <register @c_page="cEvent"/>
    </div>
    <div v-else-if="page === 'reset'">
      <reset @c_page="cEvent"/>
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