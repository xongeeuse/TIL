<template>
  <div>
    <span>{{ product.title }}</span>
    <button @click="deleteProduct(product.id)">삭제</button>
  </div>
</template>

<script setup>
import { useProductStore } from "@/stores/product";

const store = useProductStore();

defineProps({
  product: Object,
});

const deleteProduct = function (id) {
  store.deleteTodo(id);
};
</script>

<style scoped></style>
