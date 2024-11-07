<template>
  <li v-for="product in products" :key="product.id">
    <ProductListItem :product="product" />
  </li>
</template>

<script setup>
import ProductListItem from "@/components/ProductListItem.vue";
defineProps({
  products: Array,
});
</script>
