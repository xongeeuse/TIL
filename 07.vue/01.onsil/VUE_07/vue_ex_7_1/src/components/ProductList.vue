<template>
  <div><h1>ProductList</h1></div>
  <ul>
    <li v-for="product in store.products">
      {{ product.id }} - {{ product.title }} - {{ product.body }}
    </li>
  </ul>
</template>

<script setup>
import { useProductStore } from "@/stores/product";
const store = useProductStore();
console.log(store.products);
</script>

<style scoped></style>
