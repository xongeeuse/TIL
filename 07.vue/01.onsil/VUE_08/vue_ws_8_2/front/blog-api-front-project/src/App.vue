<template>
  <nav>
    <RouterLink to="/">Main</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
nav {
  background-color: black;
  color: white;
  text-align: center;
  padding: 20px;
}
nav a {
  color: white;
  text-decoration: none;
}
</style>
