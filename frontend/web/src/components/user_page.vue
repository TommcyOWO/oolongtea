<script setup lang="ts">
import '@master/css';

</script>
<template>
  <div class="flex mt:50px justify-content:center w:100%">
    <div class="flex ai:center h:450px w:900px r:20px bg:beryl-68 display:none@<md">
      <ul class="rel f:25 font:semibold color:white ml:10px list-style:none h:10px bottom:25%">
        <li class="m:10px my:20px shadow:0|4|white:hover cursor:pointer ~300ms|ease-in">帳號資訊</li>
        <li class="m:10px my:20px shadow:0|4|white:hover cursor:pointer ~300ms|ease-in">資料檢索</li>
        <li class="m:10px my:20px shadow:0|4|white:hover cursor:pointer ~300ms|ease-in">管理裝置</li>
        <li class="m:10px my:20px shadow:0|4|white:hover cursor:pointer ~300ms|ease-in">帳號設定</li>
      </ul>
      <div class="flex bottom:10px float:right h:400 w:700px bg:white r:15px m:25px"></div>
    </div>
  </div>
  <div class="rel float:right top:65 h:30 w:60% bg:beryl-76"></div>
</template>
<style scoped>
</style>