<template>
  <main class="container">
    <h1 class="singerlist-title">가수 목록</h1>
    <div class="singer-grid">
      <SingerDetail v-for="_ in numberOfItems" :key="index" />
    </div>
  </main>
</template>

<script setup>
import SingerDetail from "@/components/singers/SingerDetail.vue";
const numberOfItems = 4;
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
