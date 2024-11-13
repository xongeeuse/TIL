<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'TodoView' }">할 일 목록</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped></style>
