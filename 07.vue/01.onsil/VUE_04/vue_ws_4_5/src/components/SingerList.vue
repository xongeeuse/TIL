<template>
  <main class="container">
    <h1 class="singerlist-title">가수 목록</h1>
    <div class="singer-grid">
      <SingerDetail v-for="_ in numberOfSingers" :key="index" />
    </div>
  </main>
</template>

<script setup>
import { ref } from "vue";
import SingerDetail from "@/components/singers/SingerDetail.vue";
const singers = [{ name: "adele" }, { name: "maroon 5" }, { name: "Dua Lipa" }];
const numberOfSingers = singers.length;
</script>

<style scoped>
.singerlist-title {
  color: orangered;
  text-align: center;
}
.container {
  max-width: 1200px;
  margin: 0 auto;
}

/* .singer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  justify-content: center;
} */
</style>
