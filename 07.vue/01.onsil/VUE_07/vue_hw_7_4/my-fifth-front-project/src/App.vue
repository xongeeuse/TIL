<template>
  <RouterLink :to="{ name: 'main' }">Main</RouterLink>
  <h1>PINIA / ROUTER 연습!</h1>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
