<template>
  <ul>
    <ProductListItem
      v-for="product in products"
      :key="product.id"
      :product="product"
      @add-to-cart="addToCart"
    />
  </ul>
</template>

<script setup>
import ProductListItem from "@/components/ProductListItem.vue";

defineProps({
  products: Array,
});

const emit = defineEmits("addToCart");
const addToCart = function (product) {
  emit("addToCart", product);
};
</script>
